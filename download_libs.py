"""Download all JS/CSS libraries to lib/ folder for offline use."""
import urllib.request, os, sys

LIB = os.path.join(os.path.dirname(__file__), 'lib')
os.makedirs(LIB, exist_ok=True)

FILES = [
    # Three.js r148 UMD
    ('three.min.js',           'https://unpkg.com/three@0.148.0/build/three.min.js'),
    # Three.js postprocessing (examples/js — available in r148)
    ('EffectComposer.js',      'https://unpkg.com/three@0.148.0/examples/js/postprocessing/EffectComposer.js'),
    ('RenderPass.js',          'https://unpkg.com/three@0.148.0/examples/js/postprocessing/RenderPass.js'),
    ('ShaderPass.js',          'https://unpkg.com/three@0.148.0/examples/js/postprocessing/ShaderPass.js'),
    ('CopyShader.js',          'https://unpkg.com/three@0.148.0/examples/js/shaders/CopyShader.js'),
    ('LuminosityHighPass.js',  'https://unpkg.com/three@0.148.0/examples/js/shaders/LuminosityHighPassShader.js'),
    ('UnrealBloomPass.js',     'https://unpkg.com/three@0.148.0/examples/js/postprocessing/UnrealBloomPass.js'),
    # GSAP
    ('gsap.min.js',            'https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js'),
    ('ScrollTrigger.min.js',   'https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js'),
    # Lenis
    ('lenis.min.js',           'https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.42/dist/lenis.min.js'),
]

total = len(FILES)
for i, (name, url) in enumerate(FILES, 1):
    dest = os.path.join(LIB, name)
    print(f'[{i}/{total}] Downloading {name} ...', end=' ', flush=True)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as r, open(dest, 'wb') as f:
            data = r.read()
            f.write(data)
        kb = len(data) // 1024
        print(f'OK  ({kb} KB)')
    except Exception as e:
        print(f'FAILED: {e}')
        sys.exit(1)

print('\nAll libraries downloaded successfully to lib/')
