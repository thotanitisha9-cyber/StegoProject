{% extends "layout.html" %}

{% block content %}
<section class="relative min-h-[85vh] flex items-center justify-center text-center">
    <div class="max-w-5xl mx-auto px-6 animate-float">

        <!-- Status Badge -->
        <div
            class="inline-flex items-center gap-2 px-4 py-2 rounded-full glass-card border-neon-cyan/20 mb-8 backdrop-blur-md">
            <span class="relative flex h-2 w-2">
                <span
                    class="animate-ping absolute inline-flex h-full w-full rounded-full bg-neon-cyan opacity-75"></span>
                <span class="relative inline-flex rounded-full h-2 w-2 bg-neon-cyan"></span>
            </span>
            <span class="text-xs font-mono text-neon-cyan tracking-widest uppercase">System Online v2.0</span>
        </div>

        <!-- Main Heading -->
        <h1 class="text-5xl md:text-7xl font-bold font-display leading-tight mb-6">
            <span class="bg-clip-text text-transparent bg-gradient-to-r from-white via-gray-200 to-gray-400">Deep
                Learning Ensemble</span>
            <br>
            <span
                class="bg-clip-text text-transparent bg-gradient-to-r from-neon-blue via-neon-cyan to-neon-purple text-glow">Steganography
                Detection</span>
        </h1>

        <p class="text-lg md:text-xl text-gray-400 max-w-3xl mx-auto mb-10 font-light leading-relaxed">
            Advanced multimedia forensic framework capable of detecting hidden payloads in image, audio, video, and text
            structures with <span class="text-neon-cyan font-mono">96.4% accuracy</span>.
        </p>

        <!-- CTA Buttons -->
        <div class="flex flex-col md:flex-row gap-6 justify-center items-center">
            <a href="/detect"
                class="btn-primary-gradient px-8 py-4 rounded-lg font-bold text-white shadow-lg shadow-neon-blue/20 hover:shadow-neon-cyan/40 transition-all transform hover:-translate-y-1 w-full md:w-auto">
                <i class="fas fa-radar mr-2"></i> Run AI Diagnostics
            </a>
            <a href="/menu"
                class="px-8 py-4 rounded-lg glass-card text-white font-semibold hover:bg-white/10 hover:border-neon-purple/50 transition-all border border-transparent w-full md:w-auto">
                <i class="fas fa-layer-group mr-2"></i> View Modules
            </a>
        </div>

    </div>
</section>

<!-- Feature Cards -->
<section class="max-w-7xl mx-auto px-6 py-20">
    <div class="grid md:grid-cols-3 gap-8">

        <!-- Feature 1 -->
        <div class="glass-panel p-8 rounded-2xl relative overflow-hidden group">
            <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                <i class="fas fa-brain text-9xl text-neon-purple"></i>
            </div>
            <div class="relative z-10">
                <div
                    class="w-14 h-14 rounded-full bg-neon-purple/10 flex items-center justify-center mb-6 border border-neon-purple/20">
                    <i class="fas fa-network-wired text-neon-purple text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold text-white mb-3 group-hover:text-neon-purple transition-colors">Ensemble
                    Fusion</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                    Combines outputs from multiple CNN architectures (ProposedNet, ShallowNet) using a meta-classifier
                    logic to minimize false positives.
                </p>
            </div>
        </div>

        <!-- Feature 2 -->
        <div class="glass-panel p-8 rounded-2xl relative overflow-hidden group">
            <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                <i class="fas fa-wave-square text-9xl text-neon-cyan"></i>
            </div>
            <div class="relative z-10">
                <div
                    class="w-14 h-14 rounded-full bg-neon-cyan/10 flex items-center justify-center mb-6 border border-neon-cyan/20">
                    <i class="fas fa-microscope text-neon-cyan text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold text-white mb-3 group-hover:text-neon-cyan transition-colors">Noise
                    Residuals</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                    Utilizes high-pass filters to extract noise residuals, exposing the subtle statistical disruptions
                    caused by LSB embedding.
                </p>
            </div>
        </div>

        <!-- Feature 3 -->
        <div class="glass-panel p-8 rounded-2xl relative overflow-hidden group">
            <div class="absolute top-0 right-0 p-4 opacity-10 group-hover:opacity-20 transition-opacity">
                <i class="fas fa-shield-virus text-9xl text-neon-blue"></i>
            </div>
            <div class="relative z-10">
                <div
                    class="w-14 h-14 rounded-full bg-neon-blue/10 flex items-center justify-center mb-6 border border-neon-blue/20">
                    <i class="fas fa-lock text-neon-blue text-2xl"></i>
                </div>
                <h3 class="text-xl font-bold text-white mb-3 group-hover:text-neon-blue transition-colors">Forensic
                    Grade</h3>
                <p class="text-gray-400 text-sm leading-relaxed">
                    Supports multimedia formats (Images, Audio, Video, Text) with forensic-level accuracy tailored for
                    security applications.
                </p>
            </div>
        </div>

    </div>
</section>

<!-- About Project (Timeline) -->
<section class="max-w-5xl mx-auto px-6 py-20 border-t border-white/5">
    <div class="text-center mb-16">
        <h2 class="text-3xl font-bold font-display text-white mb-4">Project Roadmap</h2>
        <p class="text-gray-400">Development timeline and key milestones achieved.</p>
    </div>

    <div class="relative border-l border-neon-blue/30 ml-6 md:ml-12 space-y-12">

        <!-- Milestone 1 -->
        <div class="relative pl-8 md:pl-12">
            <span class="absolute -left-1.5 top-2 h-3 w-3 rounded-full bg-neon-blue shadow-[0_0_10px_#4facfe]"></span>
            <div class="glass-card p-6 rounded-xl border-l-4 border-neon-blue">
                <h4 class="text-lg font-bold text-white">Phase 1: Architecture Design</h4>
                <p class="text-gray-400 text-sm mt-2">Developed the dual-stream CNN architecture and established the
                    dataset generation pipeline using varying payloads.</p>
            </div>
        </div>

        <!-- Milestone 2 -->
        <div class="relative pl-8 md:pl-12">
            <span class="absolute -left-1.5 top-2 h-3 w-3 rounded-full bg-neon-cyan shadow-[0_0_10px_#00f2fe]"></span>
            <div class="glass-card p-6 rounded-xl border-l-4 border-neon-cyan">
                <h4 class="text-lg font-bold text-white">Phase 2: Model Training & optimization</h4>
                <p class="text-gray-400 text-sm mt-2">Trained ProposedNet and ShallowNet on 10,000+ samples. Achieved
                    98% validation accuracy with ensemble logic.</p>
            </div>
        </div>

        <!-- Milestone 3 -->
        <div class="relative pl-8 md:pl-12">
            <span class="absolute -left-1.5 top-2 h-3 w-3 rounded-full bg-neon-purple shadow-[0_0_10px_#a18cd1]"></span>
            <div class="glass-card p-6 rounded-xl border-l-4 border-neon-purple">
                <h4 class="text-lg font-bold text-white">Phase 3: Web Integration</h4>
                <p class="text-gray-400 text-sm mt-2">Deployed Flask-based web interface with real-time detection,
                    comparison tools, and multi-modal support.</p>
            </div>
        </div>

    </div>
</section>
{% endblock %}