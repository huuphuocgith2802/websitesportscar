# ==============================================================================
# SCRIPT TỰ ĐỘNG TỐI ƯU & XUẤT MODEL TỪ BLENDER SANG THREE.JS CHO WEB SUPERCAR
# Dùng trong Blender 3.0+ / 4.0+
# ==============================================================================
import bpy
import os

def export_aventador_for_webgl():
    print("[DHP Garage] Bắt đầu tối ưu hóa model cho WebGL...")
    
    # 1. Đường dẫn xuất file ra thư mục website
    output_dir = os.path.dirname(bpy.data.filepath) if bpy.data.filepath else bpy.path.abspath("//")
    output_path = os.path.join(output_dir, "aventador_sv.glb")
    
    # 2. Thiết lập cấu hình xuất glTF 2.0 chuẩn WebGL hiệu năng cao
    bpy.ops.export_scene.gltf(
        filepath=output_path,
        export_format='GLB',
        use_selection=False,
        export_apply=True,          # Tự động apply all modifiers
        export_yup=True,            # Hệ tọa độ Y-Up chuẩn Three.js
        export_texcoords=True,
        export_normals=True,
        export_materials='EXPORT',  # Xuất đầy đủ PBR Materials
        export_colors=True,
        export_cameras=False,       # Không xuất camera blender (dùng camera website)
        export_lights=False         # Không xuất đèn (dùng trần đèn LED kim cương của website)
    )
    
    print(f"[DHP Garage] Xuất file thành công: {output_path}")
    print("[DHP Garage] Bạn có thể kéo thả file .glb này trực tiếp vào trình duyệt web!")

if __name__ == "__main__":
    export_aventador_for_webgl()
