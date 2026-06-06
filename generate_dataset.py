{% extends "layout.html" %}

{% block body_class %}bg-gradient-video{% endblock %}

{% block content %}
<section class="max-w-7xl mx-auto px-6 py-10">

    <!-- Header -->
    <div class="flex items-center justify-between mb-8 pb-6 border-b border-white/5">
        <div>
            <h2 class="text-3xl font-bold font-display text-white mb-2">Video Forensics</h2>

        </div>
        <a href="/menu"
            class="px-4 py-2 rounded-lg border border-white/10 text-gray-400 hover:text-white hover:bg-white/5 transition-all text-sm">
            <i class="fas fa-arrow-left mr-2"></i> Dashboard
        </a>
    </div>

    <div class="grid lg:grid-cols-2 gap-8">

        <!-- ENCODE CARD -->
        <div class="glass-panel p-8 rounded-2xl relative group hover:border-neon-red/30 transition-all">
            <h3 class="text-xl font-bold text-white mb-6 flex items-center gap-3">
                <span class="w-8 h-8 rounded bg-neon-red/20 flex items-center justify-center text-neon-red text-sm"><i
                        class="fas fa-lock"></i></span>
                Encode Payload
            </h3>

            <form method="POST" action="/encode_video" enctype="multipart/form-data" class="space-y-6">
                <!-- File Input -->
                <div class="relative">
                    <label class="block text-xs font-mono text-gray-400 mb-2">SOURCE VIDEO (MP4/AVI)</label>
                    <input type="file" name="video" accept="video/*" required class="block w-full text-sm text-gray-400
                        file:mr-4 file:py-2 file:px-4
                        file:rounded-full file:border-0
                        file:text-sm file:font-semibold
                        file:bg-neon-red/10 file:text-neon-red
                        hover:file:bg-neon-red/20 cursor-pointer bg-black/20 rounded-lg border border-white/10 p-2">
                </div>

                <!-- Message Input -->
                <div>
                    <label class="block text-xs font-mono text-gray-400 mb-2">SECRET PAYLOAD</label>
                    <textarea name="message" rows="4" placeholder="Enter confidential data stream..." required
                        class="w-full bg-black/30 border border-white/10 rounded-lg p-4 text-white focus:border-neon-red focus:ring-1 focus:ring-neon-red outline-none transition-all placeholder-gray-600 font-mono text-sm"></textarea>
                </div>

                <button type="submit"
                    class="w-full py-3 rounded-lg bg-gradient-to-r from-red-600 to-red-400 text-white font-bold hover:shadow-[0_0_20px_rgba(248,113,113,0.3)] transition-all transform hover:-translate-y-1">
                    <i class="fas fa-video mr-2"></i> Inject Frame Data
                </button>
            </form>

            <!-- Encoding Results -->
            {% if mode == 'encode' and message %}
            <div class="mt-8 pt-6 border-t border-white/10">
                <div class="bg-red-500/10 border border-red-500/30 p-4 rounded-lg flex items-start gap-3">
                    <i class="fas fa-check-circle text-red-500 mt-1"></i>
                    <div>
                        <p class="text-red-400 font-mono text-sm">{{ message }}</p>
                    </div>
                </div>

                {% if download %}
                <a href="/download_stego_video"
                    class="mt-4 block w-full py-2 text-center rounded-lg border border-red-500 text-red-500 hover:bg-red-500 hover:text-white transition-all font-bold text-sm">
                    <i class="fas fa-download mr-2"></i> Download Video (.avi)
                </a>
                <p class="text-xs text-gray-500 text-center mt-2">Format: Lossless AVI (FFV1 Codec)</p>
                {% endif %}
            </div>
            {% endif %}
        </div>

        <!-- DECODE CARD -->
        <div class="glass-panel p-8 rounded-2xl relative group hover:border-gray-500/30 transition-all">
            <h3 class="text-xl font-bold text-white mb-6 flex items-center gap-3">
                <span class="w-8 h-8 rounded bg-gray-700 flex items-center justify-center text-gray-300 text-sm"><i
                        class="fas fa-unlock"></i></span>
                Extract Payload
            </h3>

            <form method="POST" action="/decode_video" enctype="multipart/form-data" class="space-y-6">
                <!-- File Input -->
                <div class="relative">
                    <label class="block text-xs font-mono text-gray-400 mb-2">STEGO VIDEO</label>
                    <input type="file" name="video" accept="video/*" required class="block w-full text-sm text-gray-400
                        file:mr-4 file:py-2 file:px-4
                        file:rounded-full file:border-0
                        file:text-sm file:font-semibold
                        file:bg-gray-700 file:text-gray-300
                        hover:file:bg-gray-600 cursor-pointer bg-black/20 rounded-lg border border-white/10 p-2">
                </div>

                <button type="submit"
                    class="w-full py-3 rounded-lg border border-gray-500 text-gray-400 hover:bg-gray-700 hover:text-white transition-all font-bold">
                    <i class="fas fa-search mr-2"></i> Extract Sequence
                </button>
            </form>

            <!-- Decoding Results -->
            {% if mode == 'decode' and message %}
            <div class="mt-8 pt-6 border-t border-white/10">
                <div class="bg-blue-500/10 border border-blue-500/30 p-4 rounded-lg">
                    <div class="text-xs text-blue-400 mb-2 font-mono">DECRYPTED STREAM:</div>
                    <p class="text-white font-mono text-sm break-all">{{ message }}</p>
                </div>
            </div>
            {% endif %}
        </div>

    </div>

</section>
{% endblock %}