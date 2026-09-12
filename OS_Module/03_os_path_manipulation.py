"""
=============================================================================
BÀI 3: XỬ LÝ ĐƯỜNG DẪN AN TOÀN VÀ ĐA NỀN TẢNG VỚI os.path
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- Đường dẫn file trên các hệ điều hành sử dụng dấu phân cách khác nhau:
  - Windows: Dấu gạch chéo ngược `\` (Backslash).
  - Linux / macOS: Dấu gạch chéo xuôi `/` (Forward slash).
- `os.path.join(*paths)`: Tự động ghép các thành phần đường dẫn bằng dấu phân cách chuẩn của hệ điều hành hiện tại.
- `os.path.abspath(path)`: Chuyển đổi đường dẫn tương đối thành đường dẫn tuyệt đối đầy đủ.
- `os.path.split(path)`: Tách đường dẫn thành `(thư_mục_cha, tên_file)`.
- `os.path.splitext(path)`: Tách tên file và phần mở rộng (đuôi file như `.csv`, `.png`).
- `os.path.exists()`, `os.path.isfile()`, `os.path.isdir()`: Các hàm kiểm tra boolean.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Đảm bảo code chạy trên máy tính cá nhân Windows và khi deploy lên server Ubuntu Linux đều không bị crash.
- Phân loại file theo đuôi mở rộng (ảnh, video, văn bản, mã nguồn).
=============================================================================
"""

import os
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("XỬ LÝ ĐƯỜNG DẪN VỚI os.path")
    print("=" * 60)

    # 1. Ghép nối đường dẫn an toàn
    folder = "dataset"
    subfolder = "images"
    filename = "avatar_user.png"

    safe_path = os.path.join(folder, subfolder, filename)
    print(f"1. Đường dẫn ghép bằng os.path.join: \n   -> {safe_path}")

    # 2. Lấy đường dẫn tuyệt đối
    abs_path = os.path.abspath(safe_path)
    print(f"\n2. Đường dẫn tuyệt đối (os.path.abspath): \n   -> {abs_path}")

    # 3. Tách đường dẫn (split & splitext)
    dir_name, base_name = os.path.split(abs_path)
    file_title, file_ext = os.path.splitext(base_name)

    print("\n3. Bóc tách thành phần đường dẫn:")
    print(f"   - Thư mục chứa (os.path.dirname):  {dir_name}")
    print(f"   - Tên file kèm đuôi (os.path.basename): {base_name}")
    print(f"   - Tên gốc (không kèm đuôi):         {file_title}")
    print(f"   - Đuôi mở rộng (Extension):         {file_ext}")

    # 4. Kiểm tra sự tồn tại và loại tệp
    test_path = "notebook"
    print(f"\n4. Kiểm tra thư mục '{test_path}':")
    print(f"   - Có tồn tại không? (os.path.exists): {os.path.exists(test_path)}")
    print(f"   - Có phải là thư mục? (os.path.isdir): {os.path.isdir(test_path)}")
    print(f"   - Có phải là file? (os.path.isfile):   {os.path.isfile(test_path)}")

if __name__ == "__main__":
    main()
