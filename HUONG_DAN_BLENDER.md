# HƯỚNG DẪN IMPORT MODEL 3D TỪ BLENDER VÀO WEB SHOWROOM
## DÀNH CHO: ĐINH HỮU PHƯỚC — PRIVATE SUPERCAR GARAGE

Trang web đã được tích hợp sẵn bộ đọc **THREE.GLTFLoader**, cho phép bạn đưa bất kỳ chiếc Lamborghini Aventador SV nào từ **Blender** vào thẳng website với đầy đủ ánh sáng, vật liệu PBR và hiệu ứng trần đèn kim cương!

---

### CÁCH 1: KÉO THẢ TRỰC TIẾP VÀO TRÌNH DUYỆT (NHANH NHẤT)
1. Mở trang web `http://127.0.0.1:5500/index.html` trên trình duyệt.
2. Bấm nút **"📁 TẢI MODEL BLENDER (.GLB)"** ở góc trên màn hình, HOẶC **kéo thả trực tiếp file `.glb`** vào giữa màn hình.
3. Website sẽ tự động căn giữa xe, tối ưu kích thước, gắn shader Matte Grigio Titans và ánh sáng phản chiếu trần đèn!

---

### CÁCH 2: CÁCH TẢI MODEL LAMBORGHINI AVENTADOR SV MIỄN PHÍ TỪ BLENDER

#### Bước 1: Tải model Aventador SV (.blend hoặc .glb)
Bạn có thể tải các bản 3D Aventador SV miễn phí chất lượng cao từ:
- **Sketchfab**: Tìm từ khóa `"Lamborghini Aventador SV"`, chọn filter `Downloadable` (định dạng GLTF/GLB có sẵn).
- **BlenderKit** (Addon miễn phí trong Blender): Tìm `"Aventador"`, kéo thả vào Blender trong 1 click.
- **Free3D / CGTrader**: Tải file `.blend` hoặc `.obj`.

#### Bước 2: Thiết lập tên bộ phận trong Blender (Để nhận diện cửa cắt kéo)
Nếu bạn muốn nút **"MỞ CỬA CẮT KÉO"** trên web tự động điều khiển 2 cánh cửa:
1. Mở file xe trong Blender.
2. Đổi tên object cánh cửa bên trái thành: `Door_L` hoặc `door_left`.
3. Đổi tên object cánh cửa bên phải thành: `Door_R` hoặc `door_right`.
4. Đặt tâm xoay (Origin Point) của cánh cửa tại chân bản lề phía trước (để cửa xoay chéo lên trời chuẩn Lambo).

#### Bước 3: Xuất file từ Blender sang Three.js (.glb)
1. Trong Blender: Chọn **File** → **Export** → **glTF 2.0 (.glb/.gltf)**.
2. Ở bảng thiết lập bên phải:
   - **Format**: `glTF Binary (.glb)` (file đơn duy nhất, chứa cả model + texture).
   - **Include**: Tích chọn `Selected Objects` (nếu chỉ muốn xuất xe).
   - **Geometry**: Tích chọn `Apply Modifiers`.
3. Bấm **Export glTF 2.0** và lưu thành `aventador_sv.glb`.
4. Đặt file vào thư mục `c:\Users\huuph\OneDrive\Desktop\websitesportscar\assets\aventador_sv.glb` hoặc kéo thả trực tiếp vào web!

---

### CÁCH 3: SỬ DỤNG FILE SCRIPT BLENDER TỰ ĐỘNG
Trong thư mục dự án đã có sẵn file `export_aventador_for_web.py`. Bạn chỉ cần mở Blender, vào tab **Scripting**, mở file này và bấm **Run Script** để tự động tối ưu hóa và xuất file `.glb` chuẩn WebGL.
