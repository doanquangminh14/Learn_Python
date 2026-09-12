"""
=============================================================================
BÀI 2: THAO TÁC TỆP TIN & ĐỌC METADATA TRONG OS MODULE
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `os.rename(src, dst)`: Đổi tên tệp hoặc thư mục.
- `os.replace(src, dst)`: Đổi tên hoặc di chuyển tệp (ghi đè nguyên tử - Atomic overwrite nếu đích đã tồn tại).
- `os.remove(path)` / `os.unlink(path)`: Xóa một tệp tin. (Lưu ý: Không dùng hàm này để xóa thư mục).
- `os.rmdir(path)`: Xóa một thư mục RỖNG.
- `os.stat(path)`: Truy xuất metadata của tệp từ File System (kích thước `st_size`, thời gian tạo `st_ctime`, thời gian sửa đổi gần nhất `st_mtime`).

💡 TRƯỜNG HỢP SỬ DỤNG:
- Tự động đổi tên hàng loạt file ảnh theo ngày chụp (`IMG_001.jpg` -> `2026_09_12_IMG_001.jpg`).
- Xóa các file log tạm thời (temporary files) cũ hơn 30 ngày.
- Kiểm tra dung lượng file trước khi tải lên Cloud Storage.
=============================================================================
"""

import os
import sys
import time

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("THAO TÁC FILE: TẠO, ĐỔI TÊN, METADATA VÀ XÓA")
    print("=" * 60)

    original_file = "sample_raw.txt"
    renamed_file = "sample_processed.txt"

    # 1. Tạo một file mẫu để thao tác
    with open(original_file, "w", encoding="utf-8") as f:
        f.write("Dữ liệu thử nghiệm xử lý file với os module.\n")
        f.write("Học Python căn bản đến nâng cao.\n")
    print(f"1. ✅ Đã tạo file: {original_file}")

    # 2. Đọc Metadata của file bằng os.stat()
    file_info = os.stat(original_file)
    print("\n2. 📊 Thông tin Metadata của file (os.stat):")
    print(f"   - Kích thước: {file_info.st_size} bytes")
    print(f"   - Thời gian sửa đổi cuối (st_mtime): {time.ctime(file_info.st_mtime)}")
    print(f"   - Quyền truy cập (Mode): {oct(file_info.st_mode)}")

    # 3. Đổi tên file bằng os.rename() / os.replace()
    os.replace(original_file, renamed_file)
    print(f"\n3. 🔄 Đã đổi tên file thành: {renamed_file}")
    print(f"   - '{original_file}' còn tồn tại? {os.path.exists(original_file)}")
    print(f"   - '{renamed_file}' tồn tại? {os.path.exists(renamed_file)}")

    # 4. Xóa file an toàn với os.remove()
    if os.path.exists(renamed_file):
        os.remove(renamed_file)
        print(f"\n4. 🗑️ Đã xóa file: {renamed_file}")

if __name__ == "__main__":
    main()
