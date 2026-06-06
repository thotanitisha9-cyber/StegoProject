{% extends "layout.html" %}

{% block body_class %}bg-gradient-text{% endblock %}

{% block content %}
<section class="max-w-7xl mx-auto px-6 py-10">

    <!-- Header -->
    <div class="flex items-center justify-between mb-8 pb-6 border-b border-white/5">
        <div>
            <h2 class="text-3xl font-bold font-display text-white mb-2">Text Forensics</h2>
            <p class="text-gray-400 text-sm">Zero-Width Character (ZWC) Embedding.</p>
        </div>
        <a href="/menu"
            class="px-4 py-2 rounded-lg border border-white/10 text-gray-400 hover:text-white hover:bg-white/5 transition-all text-sm">
            <i class="fas fa-arrow-left mr-2"></i> Dashboard
        </a>
    </div>

    <div class="grid lg:grid-cols-2 gap-8">

        <!-- ENCODE CARD -->
        <div class="glass-panel p-8 rounded-2xl relative group hover:border-neon-blue/30 transition-all">
            <h3 class="text-xl font-bold text-white mb-6 flex items-center gap-3">
                <span class="w-8 h-8 rounded bg-neon-blue/20 flex items-center justify-center text-neon-blue text-sm"><i
                        class="fas fa-lock"></i></span>
                Encode Text Stream
            </h3>

            <form method="POST" action="/encode_text" class="space-y-6">
                <!-- Cover Text Input -->
                <div>
                    <label class="block text-xs font-mono text-gray-400 mb-2">PUBLIC COVER TEXT</label>
                    <textarea name="cover_text" rows="3" placeholder="Enter visible public text..." required
                        class="w-full bg-black/30 border border-white/10 rounded-lg p-4 text-white focus:border-neon-blue focus:ring-1 focus:ring-neon-blue outline-none transition-all placeholder-gray-600 font-mono text-sm"></textarea>
                </div>

                <!-- Message Input -->
                <div>
                    <label class="block text-xs font-mono text-gray-400 mb-2">SECRET PAYLOAD</label>
                    <textarea name="secret_message" rows="3" placeholder="Enter hidden message..." required
                        class="w-full bg-black/30 border border-white/10 rounded-lg p-4 text-white focus:border-neon-blue focus:ring-1 focus:ring-neon-blue outline-none transition-all placeholder-gray-600 font-mono text-sm"></textarea>
                </div>

                <button type="submit"
                    class="w-full py-3 rounded-lg bg-gradient-to-r from-blue-600 to-cyan-500 text-white font-bold hover:shadow-[0_0_20px_rgba(59,130,246,0.3)] transition-all transform hover:-translate-y-1">
                    <i class="fas fa-paragraph mr-2"></i> Embed Hidden Characters
                </button>
            </form>

            <!-- Encoding Results -->
            {% if mode == 'encode' and result_text %}
            <div class="mt-8 pt-6 border-t border-white/10">
                <div class="bg-blue-500/10 border border-blue-500/30 p-4 rounded-lg">
                    <div class="flex justify-between items-center mb-2">
                        <div class="text-xs text-blue-400 font-mono">STEGO TEXT OUTPUT:</div>
                        <button onclick="copyToClipboard('stegoOutput')"
                            class="text-xs text-gray-400 hover:text-white"><i class="fas fa-copy"></i> Copy</button>
                    </div>
                    <p id="stegoOutput"
                        class="text-white font-mono text-sm break-all bg-black/50 p-3 rounded border border-white/5">{{
                        result_text }}</p>
                </div>
                <div class="mt-2 text-xs text-gray-500 text-center">
                    <i class="fas fa-info-circle"></i> Hidden ZWC data is invisible to standard viewers.
                </div>
            </div>
            {% endif %}
        </div>

        <!-- DECODE CARD -->
        <div class="glass-panel p-8 rounded-2xl relative group hover:border-gray-500/30 transition-all">
            <h3 class="text-xl font-bold text-white mb-6 flex items-center gap-3">
                <span class="w-8 h-8 rounded bg-gray-700 flex items-center justify-center text-gray-300 text-sm"><i
                        class="fas fa-unlock"></i></span>
                Decode Text Stream
            </h3>

            <form method="POST" action="/decode_text" class="space-y-6">
                <!-- Stego Input -->
                <div>
                    <label class="block text-xs font-mono text-gray-400 mb-2">SUSPECT TEXT INPUT</label>
                    <textarea name="stego_text" rows="3" placeholder="Paste text containing hidden ZWC..." required
                        class="w-full bg-black/30 border border-white/10 rounded-lg p-4 text-white focus:border-gray-500 focus:ring-1 focus:ring-gray-500 outline-none transition-all placeholder-gray-600 font-mono text-sm"></textarea>
                </div>

                <button type="submit"
                    class="w-full py-3 rounded-lg border border-gray-500 text-gray-400 hover:bg-gray-700 hover:text-white transition-all font-bold">
                    <i class="fas fa-search mr-2"></i> Scan for Invisible Data
                </button>
            </form>

            <!-- Decoding Results -->
            {% if mode == 'decode' and result_text %}
            <div class="mt-8 pt-6 border-t border-white/10">
                <div class="bg-neon-green/10 border border-neon-green/30 p-4 rounded-lg">
                    <div class="text-xs text-neon-green mb-2 font-mono">REVEALED PAYLOAD:</div>
                    <p class="text-white font-mono text-sm break-all font-bold">{{ result_text }}</p>
                </div>
            </div>
            {% endif %}
        </div>

    </div>

</section>

<script>
    function copyToClipboard(elementId) {
        var copyText = document.getElementById(elementId).innerText;
        navigator.clipboard.writeText(copyText).then(function () {
            alert("Stego Text copied to clipboard!");
        });
    }
</script>
{% endblock %}