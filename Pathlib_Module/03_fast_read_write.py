"""
=============================================================================
BÀI 3: ĐỌC VÀ GHI FILE SIÊU TỐC 1 DÒNG LỆNH (Fast File I/O)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `path.read_text(encoding='utf-8')`: Tự động mở file, đọc toàn bộ nội dung thành chuỗi string và tự động đóng file an toàn.
- `path.write_text(data, encoding='utf-8')`: Ghi đè chuỗi dữ liệu vào file và tự động đóng file.
- `path.read_bytes()` & `path.write_bytes()`: Dành cho tệp nhị phân (Binary: Ảnh, file PDF, âm thanh).
- `path.open(mode='r', encoding='utf-8')`: Mở file với Context Manager `with` khi cần đọc từng dòng (Line-by-line) cho các file dung lượng lớn hàng GB.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Đọc file `.env`, file cấu hình, ghi log nhanh mà không cần viết các khối `with open(...)` 4 dòng.
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
    print("ĐỌC GHI FILE 1 DÒNG LỆNH VỚI PATHLIB")
    print("=" * 60)

    demo_file = Path("demo_fast_notes.txt")

    # 1. Ghi nội dung văn bản chỉ với 1 dòng lệnh
    demo_content = (
        "Xin chào từ Pathlib trong Python 3!\n"
        "Đọc và ghi file chưa bao giờ đơn giản và tiện lợi đến thế.\n"
        "Thời gian: 2026-09-12"
    )
    demo_file.write_text(demo_content, encoding="utf-8")
    print(f"1. ✅ Đã ghi dữ liệu vào '{demo_file}' bằng .write_text()")

    # 2. Đọc lại nội dung văn bản chỉ với 1 dòng lệnh
    retrieved_content = demo_file.read_text(encoding="utf-8")
    print(f"\n2. 📖 Nội dung đọc được bằng .read_text():")
    print("-" * 40)
    print(retrieved_content)
    print("-" * 40)

    # 3. Đọc từng dòng cho file lớn với .open()
    print("\n3. 🔄 Đọc từng dòng với .open():")
    with demo_file.open("r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            print(f"   [Dòng {idx}] {line.strip()}")

    # 4. Dọn dẹp file demo
    if demo_file.exists():
        demo_file.unlink() # Xóa file
        print(f"\n4. 🧹 Đã xóa file demo '{demo_file}' bằng .unlink()!")

if __name__ == "__main__":
    main()
