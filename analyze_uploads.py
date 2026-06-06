<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}StegaShield | Advanced Forensics{% endblock %}</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Custom Theme & Overrides -->
    <link rel="stylesheet" href="{{ url_for('static', filename='css/modern_tailwind.css') }}">

    <!-- FontAwesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Three.js (Vanilla) -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>

    <!-- Background Animation -->
    <script src="{{ url_for('static', filename='js/three_bg.js') }}" defer></script>

    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        cyber: {
                            dark: '#050510',
                            glass: 'rgba(255, 255, 255, 0.05)',
                        },
                        neon: {
                            cyan: '#00f2fe',
                            blue: '#4facfe',
                            purple: '#a18cd1',
                            red: '#ff5f6d'
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        display: ['Space Grotesk', 'sans-serif'],
                        mono: ['Fira Code', 'monospace'],
                    }
                }
            }
        }
    </script>
</head>

<body
    class="bg-[#050510] text-gray-200 overflow-x-hidden relative min-h-screen flex flex-col {% block body_class %}{% endblock %}">

    <!-- 3D Background Container -->
    <div id="three-bg" class="fixed top-0 left-0 w-full h-full -z-10 opacity-40 pointer-events-none"></div>

    <!-- Navigation -->
    <nav class="fixed top-0 w-full z-50 glass-panel border-b border-white/5 bg-opacity-80 backdrop-blur-md">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <!-- Logo -->
            <a href="/" class="flex items-center gap-3 group">
                <div
                    class="w-10 h-10 rounded-lg bg-gradient-to-tr from-neon-blue to-neon-cyan flex items-center justify-center shadow-lg shadow-neon-blue/20 group-hover:shadow-neon-cyan/40 transition-all">
                    <i class="fas fa-shield-alt text-black text-xl"></i>
                </div>
                <div>
                    <h1
                        class="font-display font-bold text-xl tracking-wide text-white group-hover:text-neon-cyan transition-colors">
                        STEGA<span class="text-neon-blue">SHIELD</span></h1>
                    <p class="text-[0.65rem] text-gray-400 uppercase tracking-widest">Forensic AI Framework</p>
                </div>
            </a>

            <!-- Links -->
            <div class="hidden md:flex items-center gap-8">
                <a href="/"
                    class="text-sm font-medium text-gray-300 hover:text-white hover:text-glow transition-all">Home</a>
                <a href="/menu"
                    class="text-sm font-medium text-gray-300 hover:text-white hover:text-glow transition-all">Modules</a>
                <a href="/detect"
                    class="text-sm font-medium text-gray-300 hover:text-white hover:text-glow transition-all">AI
                    Detection</a>
                <a href="/benchmark"
                    class="text-sm font-medium text-gray-300 hover:text-white hover:text-glow transition-all">Metrics</a>

                <a href="/menu"
                    class="px-5 py-2 rounded-full border border-neon-cyan/30 text-neon-cyan text-sm font-semibold hover:bg-neon-cyan hover:text-black transition-all shadow-md hover:shadow-neon-cyan/20">
                    Launch Console
                </a>
            </div>

            <!-- Mobile Menu Button (Placeholder) -->
            <button class="md:hidden text-gray-300 text-xl">
                <i class="fas fa-bars"></i>
            </button>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-grow pt-24 pb-12 px-4 relative z-10">
        {% block content %}{% endblock %}
    </main>

    <!-- Footer -->
    <footer class="border-t border-white/5 bg-black/20 backdrop-blur-sm mt-auto">
        <div class="max-w-7xl mx-auto px-6 py-8">
            <div class="flex flex-col md:flex-row justify-between items-center gap-4">
                <p class="text-gray-500 text-sm">© 2026 Advanced Multimedia Forensics Lab. All rights reserved.</p>
                <div class="flex gap-6 text-gray-400">
                    <a href="#" class="hover:text-neon-cyan transition-colors"><i class="fab fa-github"></i></a>
                    <a href="#" class="hover:text-neon-blue transition-colors"><i class="fab fa-twitter"></i></a>
                    <a href="#" class="hover:text-neon-purple transition-colors"><i class="fas fa-envelope"></i></a>
                </div>
            </div>
        </div>
    </footer>

</body>

</html>