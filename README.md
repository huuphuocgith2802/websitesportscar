# 🏎️ ĐINH HỮU PHƯỚC — Private Supercar Garage

> Awwwards-style 3D Landing Page · Lamborghini Aventador SV · WebGL + Three.js

## ✦ Stack
| Layer | Tech |
|-------|------|
| 3D Engine | Three.js r165 (WebGL2) |
| Animation | GSAP 3.12 + ScrollTrigger |
| Smooth Scroll | Lenis 1.0 |
| Styling | Tailwind CSS CDN + Custom CSS |
| Post-FX | UnrealBloomPass |
| Audio | Web Audio API (V12 synth) |

## ✦ Pages
- `index.html`: Trang đích phong cách Awwwards (Scrollytelling 3D, cốt truyện, telemetry trực tiếp, thẻ VIP Owner).
- `showroom.html`: **Trang Toàn Cảnh 360° Độc Lập** — Showroom tương tác 3D thuần túy, hỗ trợ xoay tự do, zoom pinch, tùy biến màu sơn, mở cửa cắt kéo, đổi môi trường studio và điểm chú thích kỹ thuật (Hotspots), tối ưu tuyệt đối cho **Mobile, iPad và Laptop**.

## ✦ Features
- **Procedural Lamborghini Aventador SV** — fully built in Three.js, no external .glb needed
- **Diamond-grid LED ceiling** — 120 spotlights in offset-column pattern, subtle flicker
- **PBR Materials** — matte body (roughness 0.85), gloss carbon, chrome rims, physical glass
- **UnrealBloomPass** — Y-LED headlights + ceiling LEDs bloom at 60fps
- **Scissor Door animation** — GSAP-driven hinge with physics easing
- **V12 engine sound** — layered Web Audio API oscillators with distortion
- **ScrollTrigger camera path** — 5-phase 360° orbit: front → wheel → rear wing → top → hero
- **Mouse Parallax** — real-time camera tilt + keylight shift
- **Glassmorphism UI** — dark mode, gold accents, Bebas Neue + Space Grotesk
- **Live Location Widget** — real-time clock, Đồng Nai coordinates
- **Custom cursor** — gold dot + ring, hover expand

## ✦ How to Use
Simply open `index.html` in any modern browser (Chrome 110+, Edge, Firefox 110+).
No build step, no npm install — all deps from CDN.

### Adding a Real .glb Model
Replace the procedural car block in `index.html` (marked `// ─── BUILD LAMBORGHINI ───`)
with:
```js
const loader = new THREE.GLTFLoader();
loader.load('./assets/models/aventador_sv.glb', (gltf) => {
  carGroup.add(gltf.scene);
  // configure PBR materials here
});
```

## ✦ Owner
**ĐINH HỮU PHƯỚC** · Đồng Nai, Việt Nam · 10.9602°N 106.8272°E
