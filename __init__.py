import sys
import os
import torch
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_curve, auc
from rich.console import Console
from rich.table import Table

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.ml.deep_stego import get_dataset, BasePaperSystem, train_proposed

console = Console()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
console.print(f"[bold green]System Initialized on {device}[/bold green]")

class TextStegoDetector:
    def check_text(self, text):
        zwc = ['\u200b', '\u200c', '\u200d']
        return 1 if any(z in text for z in zwc) else 0

def plot_results(y_test, base_probs, prop_probs, payload, save_path=None):
    fpr_b, tpr_b, _ = roc_curve(y_test, base_probs)
    roc_auc_b = auc(fpr_b, tpr_b)
    fpr_p, tpr_p, _ = roc_curve(y_test, prop_probs)
    roc_auc_p = auc(fpr_p, tpr_p)
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(fpr_b, tpr_b, label=f'Base (AUC={roc_auc_b:.2f})', linestyle='--')
    plt.plot(fpr_p, tpr_p, label=f'Proposed (AUC={roc_auc_p:.2f})', linewidth=2)
    plt.plot([0,1],[0,1], 'k--', alpha=0.3)
    plt.title(f'ROC Curve (Payload {payload} bpp)')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    cm = confusion_matrix(y_test, (prop_probs > 0.5).astype(int))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix (Proposed)')
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
        plt.close()
    else:
        plt.show()

def run_experiment():
    console.rule("[bold red]Multi-Modal Benchmark[/bold red]")
    
    # Text Check
    txt = TextStegoDetector()
    console.print(f"Text Check ('Hello World'): {txt.check_text('Hello World')==1}")
    
    payload = 0.1
    console.print(f"\n[yellow]Generating Data ({payload} bpp)...[/yellow]")
    X_train, X_test, y_train, y_test = get_dataset(num_samples=1500, payload=payload)
    
    console.print("[blue]Running Base Paper...[/blue]")
    base = BasePaperSystem()
    base_preds, base_probs = base.run(X_train, y_train, X_test)
    
    console.print("[green]Running Proposed System...[/green]")
    prop_preds, prop_probs, _ = train_proposed(X_train, y_train, X_test, epochs=20)
    
    acc_base = accuracy_score(y_test, base_preds)
    acc_prop = accuracy_score(y_test, prop_preds)
    
    table = Table(title=f"Results @ {payload} bpp")
    table.add_column("System", style="cyan")
    table.add_column("Accuracy", style="magenta")
    table.add_row("Base Paper", f"{acc_base:.2%}")
    table.add_row("Proposed", f"[bold green]{acc_prop:.2%}[/bold green]")
    console.print(table)
    
    plot_results(y_test, base_probs, prop_probs, payload)

def run_benchmark_web(save_dir):
    """Run benchmark for web app, returning dict of results and saving plots."""
    os.makedirs(save_dir, exist_ok=True)
    
    # 1. Generate Data
    payload = 0.1
    X_train, X_test, y_train, y_test = get_dataset(num_samples=1000, payload=payload)
    
    # 2. Run Models
    base = BasePaperSystem()
    base_preds, base_probs = base.run(X_train, y_train, X_test)
    
    prop_preds, prop_probs, _ = train_proposed(X_train, y_train, X_test, epochs=10)
    
    # 3. Compute Basic Accuracy
    acc_base = accuracy_score(y_test, base_preds)
    acc_prop = accuracy_score(y_test, prop_preds)
    
    # 4. Compute Detailed Metrics (Proposed)
    from sklearn.metrics import precision_score, recall_score, f1_score
    prec = precision_score(y_test, prop_preds, zero_division=0)
    rec = recall_score(y_test, prop_preds, zero_division=0)
    f1 = f1_score(y_test, prop_preds, zero_division=0)
    
    # 5. Generate Plots
    
    # Plot 1: ROC Curve Comparison
    plt.figure(figsize=(6, 4))
    fpr_b, tpr_b, _ = roc_curve(y_test, base_probs)
    roc_auc_b = auc(fpr_b, tpr_b)
    fpr_p, tpr_p, _ = roc_curve(y_test, prop_probs)
    roc_auc_p = auc(fpr_p, tpr_p)
    
    plt.plot(fpr_b, tpr_b, label=f'Base (AUC={roc_auc_b:.2f})', linestyle='--')
    plt.plot(fpr_p, tpr_p, label=f'Proposed (AUC={roc_auc_p:.2f})', linewidth=2)
    plt.plot([0,1],[0,1], 'k--', alpha=0.3)
    plt.title(f'ROC Curve')
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, "benchmark_roc.png"))
    plt.close()

    # Plot 2: Confusion Matrix
    plt.figure(figsize=(5, 4))
    cm = confusion_matrix(y_test, (prop_probs > 0.5).astype(int))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix (Proposed)')
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, "benchmark_cm.png"))
    plt.close()
    
    # Plot 3: Metrics Bar Chart
    plt.figure(figsize=(6, 4))
    metrics_vals = [acc_prop, prec, rec, f1]
    metrics_names = ['Accuracy', 'Precision', 'Recall', 'F1']
    colors = ['#007bff', '#28a745', '#ffc107', '#6f42c1']
    bars = plt.bar(metrics_names, metrics_vals, color=colors)
    plt.ylim(0, 1.1)
    plt.title('Proposed Model Metrics')
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f"{yval:.2f}", ha='center', va='bottom')
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, "benchmark_metrics.png"))
    plt.close()
    
    # Return Dictionary
    # REAL METRICS FROM TRAINING (No longer hardcoded)
    return {
        "acc_base": round(acc_base * 100, 2),
        "accuracy": round(acc_prop, 3),   
        "precision": round(prec, 3),   
        "recall": round(rec, 3),
        "f1": round(f1, 3),
        "n_test": len(y_test),
        "roc_url": "/static/analysis/benchmark_roc.png",
        "cm_url": "/static/analysis/benchmark_cm.png",
        "metrics_url": "/static/analysis/benchmark_metrics.png"
    }

if __name__ == "__main__":
    run_experiment()
