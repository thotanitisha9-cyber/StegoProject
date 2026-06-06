{% extends "layout.html" %}

{% block content %}
<section class="max-w-7xl mx-auto px-6 py-10">

    <!-- Hero Header -->
    <div class="text-center mb-16 relative">
        <h1 class="text-4xl md:text-5xl font-bold font-display text-white mb-4">Forensic <span
                class="text-neon-cyan">Modules</span></h1>
        <p class="text-gray-400 max-w-2xl mx-auto">Select a specialized module to initialize steganographic protocols.
        </p>

        <!-- Decoration -->
        <div
            class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 w-64 h-64 bg-neon-cyan/20 blur-[100px] -z-10 rounded-full">
        </div>
    </div>

    <!-- Modules Grid -->
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">

        <!-- Image Steganography -->
        <a href="/image"
            class="group glass-card p-8 rounded-2xl relative overflow-hidden transition-all hover:scale-[1.02]">
            <div
                class="absolute -right-10 -top-10 w-32 h-32 bg-neon-green/20 rounded-full blur-2xl group-hover:bg-neon-green/30 transition-all">
            </div>

            <div class="flex items-center justify-between mb-6">
                <div
                    class="w-14 h-14 rounded-xl bg-gray-800/50 flex items-center justify-center border border-gray-700 group-hover:border-neon-green/50 transition-colors">
                    <i class="fas fa-image text-2xl text-neon-green" style="color: #4ade80;"></i>
                </div>
                <div
                    class="px-3 py-1 rounded-full border border-gray-700 bg-gray-900/50 text-xs text-gray-400 font-mono">
                    IMG-FORENSICS</div>
            </div>

            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-green-400 transition-colors">Image Forensics
            </h3>
            <p class="text-gray-400 text-sm mb-6">LSB (Least Significant Bit) encoding and extraction analysis for
                PNG/BMP formats.</p>

            <div class="flex items-center text-sm text-green-400 font-medium">
                Initialize <i
                    class="fas fa-arrow-right ml-2 transform group-hover:translate-x-1 transition-transform"></i>
            </div>
        </a>

        <!-- Audio Steganography -->
        <a href="/audio"
            class="group glass-card p-8 rounded-2xl relative overflow-hidden transition-all hover:scale-[1.02]">
            <div
                class="absolute -right-10 -top-10 w-32 h-32 bg-neon-purple/20 rounded-full blur-2xl group-hover:bg-neon-purple/30 transition-all">
            </div>

            <div class="flex items-center justify-between mb-6">
                <div
                    class="w-14 h-14 rounded-xl bg-gray-800/50 flex items-center justify-center border border-gray-700 group-hover:border-neon-purple/50 transition-colors">
                    <i class="fas fa-file-audio text-2xl text-neon-purple"></i>
                </div>
                <div
                    class="px-3 py-1 rounded-full border border-gray-700 bg-gray-900/50 text-xs text-gray-400 font-mono">
                    AUD-FORENSICS</div>
            </div>

            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-neon-purple transition-colors">Audio Forensics
            </h3>
            <p class="text-gray-400 text-sm mb-6">WAV audio signal analysis using LSB encoding techniques.</p>

            <div class="flex items-center text-sm text-neon-purple font-medium">
                Initialize <i
                    class="fas fa-arrow-right ml-2 transform group-hover:translate-x-1 transition-transform"></i>
            </div>
        </a>

        <!-- Video Steganography -->
        <a href="/video"
            class="group glass-card p-8 rounded-2xl relative overflow-hidden transition-all hover:scale-[1.02]">
            <div
                class="absolute -right-10 -top-10 w-32 h-32 bg-neon-red/20 rounded-full blur-2xl group-hover:bg-neon-red/30 transition-all">
            </div>

            <div class="flex items-center justify-between mb-6">
                <div
                    class="w-14 h-14 rounded-xl bg-gray-800/50 flex items-center justify-center border border-gray-700 group-hover:border-neon-red/50 transition-colors">
                    <i class="fas fa-video text-2xl text-neon-red"></i>
                </div>
                <div
                    class="px-3 py-1 rounded-full border border-gray-700 bg-gray-900/50 text-xs text-gray-400 font-mono">
                    VID-FORENSICS</div>
            </div>

            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-neon-red transition-colors">Video Forensics
            </h3>
            <p class="text-gray-400 text-sm mb-6">Frame-based LSB encoding and extraction for AVI/MP4 video streams.</p>

            <div class="flex items-center text-sm text-neon-red font-medium">
                Initialize <i
                    class="fas fa-arrow-right ml-2 transform group-hover:translate-x-1 transition-transform"></i>
            </div>
        </a>

        <!-- Text Steganography -->
        <a href="/text"
            class="group glass-card p-8 rounded-2xl relative overflow-hidden transition-all hover:scale-[1.02]">
            <div
                class="absolute -right-10 -top-10 w-32 h-32 bg-neon-blue/20 rounded-full blur-2xl group-hover:bg-neon-blue/30 transition-all">
            </div>

            <div class="flex items-center justify-between mb-6">
                <div
                    class="w-14 h-14 rounded-xl bg-gray-800/50 flex items-center justify-center border border-gray-700 group-hover:border-neon-blue/50 transition-colors">
                    <i class="fas fa-file-alt text-2xl text-neon-blue"></i>
                </div>
                <div
                    class="px-3 py-1 rounded-full border border-gray-700 bg-gray-900/50 text-xs text-gray-400 font-mono">
                    TXT-FORENSICS</div>
            </div>

            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-neon-blue transition-colors">Text Forensics
            </h3>
            <p class="text-gray-400 text-sm mb-6">Hidden data embedding using Zero-Width Characters (ZWC) in plain text.
            </p>

            <div class="flex items-center text-sm text-neon-blue font-medium">
                Initialize <i
                    class="fas fa-arrow-right ml-2 transform group-hover:translate-x-1 transition-transform"></i>
            </div>
        </a>

        <!-- AI Detection -->
        <a href="/detect"
            class="group glass-card p-8 rounded-2xl relative overflow-hidden transition-all hover:scale-[1.02] border-neon-cyan/30 shadow-[0_0_20px_rgba(0,242,254,0.1)] col-span-1 md:col-span-2 lg:col-span-1">
            <div
                class="absolute -right-10 -top-10 w-32 h-32 bg-neon-cyan/20 rounded-full blur-2xl group-hover:bg-neon-cyan/30 transition-all">
            </div>

            <div class="flex items-center justify-between mb-6">
                <div
                    class="w-14 h-14 rounded-xl bg-gray-800/50 flex items-center justify-center border border-neon-cyan/50 group-hover:border-neon-cyan transition-colors">
                    <i class="fas fa-radar text-2xl text-neon-cyan animate-pulse"></i>
                </div>
                <div
                    class="px-3 py-1 rounded-full border border-neon-cyan/30 bg-neon-cyan/10 text-xs text-neon-cyan font-mono animate-pulse">
                    ACTIVE SCAN</div>
            </div>

            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-neon-cyan transition-colors">AI Steganalysis
            </h3>
            <p class="text-gray-400 text-sm mb-6">Run deep learning diagnostics using Ensemble Fusion models to detect
                hidden payloads.</p>

            <div class="flex items-center text-sm text-neon-cyan font-medium">
                Run Diagnostics <i
                    class="fas fa-arrow-right ml-2 transform group-hover:translate-x-1 transition-transform"></i>
            </div>
        </a>

        <!-- Pixel Comparison -->
        <a href="/compare"
            class="group glass-card p-8 rounded-2xl relative overflow-hidden transition-all hover:scale-[1.02]">
            <div
                class="absolute -right-10 -top-10 w-32 h-32 bg-orange-500/20 rounded-full blur-2xl group-hover:bg-orange-500/30 transition-all">
            </div>

            <div class="flex items-center justify-between mb-6">
                <div
                    class="w-14 h-14 rounded-xl bg-gray-800/50 flex items-center justify-center border border-gray-700 group-hover:border-orange-500/50 transition-colors">
                    <i class="fas fa-not-equal text-2xl text-orange-500"></i>
                </div>
                <div
                    class="px-3 py-1 rounded-full border border-gray-700 bg-gray-900/50 text-xs text-gray-400 font-mono">
                    DIFF-CHECK</div>
            </div>

            <h3 class="text-xl font-bold text-white mb-2 group-hover:text-orange-500 transition-colors">Pixel Comparison
            </h3>
            <p class="text-gray-400 text-sm mb-6">Bit-level visual analysis between original and suspect images.</p>

            <div class="flex items-center text-sm text-orange-500 font-medium">
                Analyze <i class="fas fa-arrow-right ml-2 transform group-hover:translate-x-1 transition-transform"></i>
            </div>
        </a>

        <!-- Benchmark Metrics -->


    </div>
</section>
{% endblock %}