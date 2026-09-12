"""
=============================================================================
BÀI 4: QUẢN LÝ THƯ MỤC VÀ TÌM KIẾM ĐỆ QUY VỚI .glob() & .rglob()
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `path.mkdir(parents=True, exist_ok=True)`: Tạo thư mục đơn hoặc đa cấp an toàn.
- `path.rmdir()`: Xóa thư mục rỗng.
- `path.unlink(missing_ok=True)`: Xóa file, không báo lỗi nếu file không tồn tại.
- `path.rename(target)`: Đổi tên hoặc di chuyển tệp.
- `path.iterdir()`: Lặp qua các mục con trực tiếp (tương tự `os.listdir()`).
- `path.glob(pattern)`: Tìm kiếm các file khớp mẫu (Wildcard `*.py`, `data_*.csv`) trong thư mục hiện tại.
- `path.rglob(pattern)`: (Recursive Glob) Tìm kiếm đệ quy qua TOÀN BỘ cây thư mục con cháu (thay thế hoàn hảo cho `os.walk()` phức tạp).

💡 TRƯỜNG HỢP SỬ DỤNG:
- Tìm kiếm tất cả file `.ipynb` hoặc `.py` trong kho mã nguồn để kiểm tra cú pháp.
- Thu gom tất cả ảnh `.png`, `.jpg` từ nhiều thư mục con vào một nơi.
=============================================================================
"""

from pathlib import Path
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. TẠO VÀ XÓA CÂY THƯ MỤC VỚI PATHLIB")
    print("=" * 60)

    demo_dir = Path("pathlib_demo_folder/nested_sub_folder")
    
    # Tạo cây thư mục đa cấp
    demo_dir.mkdir(parents=True, exist_ok=True)
    print(f"✅ Đã tạo cây thư mục: {demo_dir}")

    # Tạo một file tạm bên trong
    sample_file = demo_dir / "temp_log.txt"
    sample_file.write_text("Dữ liệu tạm thời", encoding="utf-8")

    # Xóa file và dọn dẹp thư mục
    sample_file.unlink(missing_ok=True)
    demo_dir.rmdir()
    demo_dir.parent.rmdir()
    print("🧹 Đã dọn dẹp thư mục tạm thành công!")

    print("\n" + "=" * 60)
    print("2. TÌM KIẾM ĐỆ QUY VỚI .rglob() TRONG DỰ ÁN")
    print("=" * 60)

    project_root = Path(".")

    # Tìm kiếm tất cả file Python (.py) trong toàn bộ dự án
    python_files = list(project_root.rglob("*.py"))
    # Lọc bỏ các file trong .git nếu có
    clean_py_files = [f for f in python_files if ".git" not in str(f)]

    print(f"Tổng số file Python (.py) tìm thấy: {len(clean_py_files)}")
    print("Một số file tiêu biểu:")
    for py_file in clean_py_files[:8]:
        print(f" 🐍 {py_file}")

    # Tìm kiếm tất cả file Notebook (.ipynb)
    notebooks = list(project_root.rglob("*.ipynb"))
    print(f"\nTổng số Jupyter Notebooks (.ipynb) tìm thấy: {len(notebooks)}")
    for nb in notebooks:
        print(f" 📓 {nb.name} (tại thư mục: {nb.parent})")

if __name__ == "__main__":
    main()
