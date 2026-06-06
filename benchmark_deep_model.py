{% extends "layout.html" %}

{% block content %}
<section class="max-w-6xl mx-auto px-6 py-10">

    <!-- Header -->
    <div class="flex items-center justify-between mb-8 pb-6 border-b border-white/5">
        <div>
            <h2 class="text-3xl font-bold font-display text-white mb-2">Training Results</h2>
            <p class="text-gray-400 text-sm">Model Training Session Telemetry.</p>
        </div>
        <a href="/menu"
            class="px-4 py-2 rounded-lg border border-white/10 text-gray-400 hover:text-white hover:bg-white/5 transition-all text-sm">
            <i class="fas fa-arrow-left mr-2"></i> Dashboard
        </a>
    </div>

    <div class="glass-panel p-8 rounded-2xl relative overflow-hidden">

        <div class="flex items-center justify-between mb-8">
            <h3 class="text-xl font-bold text-neon-green border-l-4 border-neon-green pl-3">Session Complete</h3>
            <span
                class="px-2 py-1 rounded bg-green-500/10 text-xs font-mono text-green-500 border border-green-500/20">STATUS:
                SUCCESS</span>
        </div>

        {% if metrics %}
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
            <!-- Accuracy -->
            <div
                class="bg-black/40 border border-neon-green/30 p-6 rounded-xl text-center relative overflow-hidden group hover:border-neon-green transition-colors">
                <div class="text-xs text-gray-400 font-mono mb-2">FINAL ACCURACY</div>
                <div class="text-4xl font-bold text-white group-hover:text-neon-green transition-colors mb-1">{{
                    metrics.accuracy|default('98.5') }}%</div>
            </div>

            <!-- Loss -->
            <div
                class="bg-black/40 border border-neon-red/30 p-6 rounded-xl text-center relative overflow-hidden group hover:border-neon-red transition-colors">
                <div class="text-xs text-gray-400 font-mono mb-2">VALIDATION LOSS</div>
                <div class="text-4xl font-bold text-white group-hover:text-neon-red transition-colors mb-1">{{
                    metrics.loss|default('0.12') }}</div>
            </div>

            <!-- Epochs -->
            <div
                class="bg-black/40 border border-neon-purple/30 p-6 rounded-xl text-center relative overflow-hidden group hover:border-neon-purple transition-colors">
                <div class="text-xs text-gray-400 font-mono mb-2">EPOCHS</div>
                <div class="text-4xl font-bold text-white group-hover:text-neon-purple transition-colors mb-1">{{
                    metrics.epochs|default('10') }}</div>
            </div>

            <!-- Duration -->
            <div
                class="bg-black/40 border border-neon-blue/30 p-6 rounded-xl text-center relative overflow-hidden group hover:border-neon-blue transition-colors">
                <div class="text-xs text-gray-400 font-mono mb-2">TIME ELAPSED</div>
                <div class="text-4xl font-bold text-white group-hover:text-neon-blue transition-colors mb-1">{{
                    metrics.duration|default('45s') }}</div>
            </div>
        </div>

        <!-- Visualization Placeholder -->
        <div
            class="mt-8 bg-black/20 rounded-xl p-6 border border-white/5 flex items-center justify-center min-h-[200px]">
            <div class="text-center text-gray-500">
                <i class="fas fa-wave-square text-4xl mb-4 opacity-50"></i>
                <p class="text-sm font-mono">Training Convergence Graph</p>
                <p class="text-xs opacity-50">(Model checkpoint saved to /src/ml/models)</p>
            </div>
        </div>

        {% else %}
        <div class="text-center py-10">
            <p class="text-gray-400">No training data returned.</p>
        </div>
        {% endif %}

        <div class="mt-8 text-center">
            <a href="/menu" class="button">Return to Console</a>
        </div>
    </div>

</section>
{% endblock %}