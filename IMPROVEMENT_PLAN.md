# 🚀 Project Improvement Plan: From "Roast" to "Research Grade"

To impress a strict reviewer and align with your abstract, you must implement the following features. These directly address the weaknesses identified in the technical review.

## 1. The "Multiple CNNs" Requirement (Crucial for Abstract)
**Reviewer Roast:** "You only have one CNN. That's not an ensemble."
**Abstract Promise:** "Uses multiple convolutional neural networks (CNNs)..."

### ✅ Implementation Plan: Add a Second CNN (`ShallowNet`)
*   **What:** Create a new, lighter CNN architecture (e.g., 3 layers instead of 5) trained on the same data.
*   **Why:** This proves you have "Multiple Base Learners."
*   **Impression Factor:** Shows you understand that different architectures capture different feature levels (e.g., one captures high-frequency noise, one captures texture anomalies).
*   **Actionable Step:**
    1.  Create `src/ml/shallow_net.py`.
    2.  Train it alongside `ProposedNet`.
    3.  Save `shallow_net.pth`.

## 2. The "Ensemble Fusion" Requirement (Crucial for Innovation)
**Reviewer Roast:** "Averaging probabilities is lazy."
**Abstract Promise:** "Employ a second-level classifier to learn from fused features..."

### ✅ Implementation Plan: Meta-Classifier (Stacking)
*   **What:** Train a **Logistic Regression** model that takes both CNN outputs as *input*.
*   **Why:** Instead of `(A+B)/2`, the meta-classifier learns `0.7*A + 0.3*B` (trusting the better model).
*   **Impression Factor:** This is true "Stacking Ensemble Learning." It mathematically proves your ensemble is smarter than individual models.
*   **Actionable Step:**
    1.  Extract probabilities from `ProposedNet` and `ShallowNet` for the test set.
    2.  Train `sklearn.linear_model.LogisticRegression` on these pairs.
    3.  Use this for the final decision.

## 3. The "Multimedia" Requirement (Crucial for Title)
**Reviewer Roast:** "Audio/Text detection is fake (random numbers)."
**Abstract Promise:** "Steganography detection in multimedia data..."

### ✅ Implementation Plan: Real Audio Steganalysis
*   **What:** Implement a statistical attack for WAV files.
*   **Why:** You cannot claim "Multimedia framework" if you only detect images.
*   **Impression Factor:** Even a simple real detection algorithm (e.g., checking LSB entropy) puts you miles ahead of projects that just simulate it.
*   **Actionable Step:**
    1.  Create `src/ml/audio_detect.py`.
    2.  Calculate **Entropy** of the LSBs in audio samples.
    3.  High entropy -> Stego suspicion.

## 4. The "Security" Requirement (Crucial for Cryptography)
**Reviewer Roast:** "You removed encryption. This is just hiding plaintext."

### ✅ Implementation Plan: Re-enable AES Encryption
*   **What:** Uncomment/fix the encryption code. Use a hashed password.
*   **Why:** Steganography without cryptography is insecure.
*   **Impression Factor:** Demonstrates "Defense in Depth." You hide the data (Stego) AND lock it (Crypto).
*   **Actionable Step:**
    1.  Restore `src/core/security.py`.
    2.  Ensure every `encode` action requires a password.

## 5. Visual "Wow" Factors (For the Demo)
**Reviewer Roast:** "The dashboard just shows a percentage."

### ✅ Implementation Plan: Heatmap Visualization
*   **What:** Visualizing *where* the model thinks the data is hidden.
*   **Why:** "Explainable AI" (XAI) is a hot topic.
*   **Impression Factor:** Showing a heatmap overlay on the image during the demo looks extremely professional and advanced.
*   **Actionable Step:**
    1.  Use `Grad-CAM` or simple patch-based probability mapping.
    2.  Overlay this on the uploaded image in the web UI.

---

## Summary of New Features to Add:
1.  **Second CNN (`ShallowNet`)** -> Fixes "Single Model" issue.
2.  **Meta-Classifier (`LogisticRegression`)** -> Fixes "Lazy Fusion" issue.
3.  **Audio LSB Analysis** -> Fixes "Fake Multimedia" issue.
4.  **AES Encryption** -> Fixes "Security" issue.
5.  **Stego Heatmap** -> Adds "Explainable AI" bonus.
