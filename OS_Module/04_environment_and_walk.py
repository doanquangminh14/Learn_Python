"""
=============================================================================
BÀI 4: QUẢN LÝ BIẾN MÔI TRƯỜNG VÀ DUYỆT CÂY THƯ MỤC VỚI os.walk
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `os.environ`: Đối tượng dạng mapping (tương tự dict) chứa tất cả các biến môi trường của hệ điều hành.
- `os.getenv(key, default=None)`: Phương thức an toàn để đọc biến môi trường (không gây KeyError nếu biến chưa tồn tại).
- `os.walk(top, topdown=True)`: Hàm sinh (Generator) duyệt đệ quy qua toàn bộ cây thư mục.
  Ở mỗi thư mục nó ghé thăm, nó trả về một tuple gồm 3 phần tử:
  `(root, dirs, files)`:
  - `root`: Đường dẫn thư mục hiện tại đang đứng.
  - `dirs`: Danh sách tên các thư mục con trong `root`.
  - `files`: Danh sách tên các file nằm trong `root`.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Đọc `API_KEY`, cấu hình Database an toàn trong phát triển Web/Backend.
- Tìm kiếm tất cả các file Python (`.py`) hoặc file dữ liệu (`.csv`) trong toàn bộ dự án để phân tích.
=============================================================================
"""

import os
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def demo_environment_variables():
    """Đọc và thiết lập biến môi trường"""
    print("=" * 60)
    print("1. QUẢN LÝ BIẾN MÔI TRƯỜNG (os.environ & os.getenv)")
    print("=" * 60)

    # Đọc biến môi trường hệ thống phổ biến
    user_name = os.getenv("USERNAME") or os.getenv("USER", "Unknown")
    os_name = os.getenv("OS", "Unknown")
    home_path = os.getenv("USERPROFILE") or os.getenv("HOME", "Unknown")

    print(f"Tên người dùng hiện tại: {user_name}")
    print(f"Hệ điều hành:            {os_name}")
    print(f"Thư mục người dùng:      {home_path}")

    # Đọc biến môi trường tùy chỉnh với giá trị mặc định an toàn
    api_key = os.getenv("MY_SECRET_API_KEY", "default_secret_key_12345")
    print(f"Giá trị API Key (getenv an toàn): {api_key}")

    # Thiết lập biến môi trường tạm thời cho tiến trình hiện tại
    os.environ["APP_ENV"] = "development"
    print(f"Biến môi trường vừa đặt (APP_ENV): {os.environ.get('APP_ENV')}")

def demo_directory_tree_walk():
    """Duyệt đệ quy cây thư mục bằng os.walk"""
    print("\n" + "=" * 60)
    print("2. DUYỆT CÂY THƯ MỤC ĐỆ QUY (os.walk)")
    print("=" * 60)

    target_dir = "."
    py_files_count = 0
    total_files_count = 0

    print(f"Đang quét toàn bộ thư mục '{target_dir}'...\n")

    for root, dirs, files in os.walk(target_dir):
        # Bỏ qua thư mục ẩn của Git (.git) và cache để output gọn gàng
        if ".git" in root or "__pycache__" in root:
            continue
            
        print(f"📁 Thư mục: {root}")
        for filename in files:
            total_files_count += 1
            file_path = os.path.join(root, filename)
            if filename.endswith(".py"):
                py_files_count += 1
                print(f"   🐍 [Python Script] {filename}")
            else:
                print(f"   📄 [Tệp tin]       {filename}")

    print("\n" + "-" * 40)
    print(f"📊 Tổng kết quét thư mục:")
    print(f"   - Tổng số file:        {total_files_count}")
    print(f"   - Số file Python (.py): {py_files_count}")

if __name__ == "__main__":
    demo_environment_variables()
    demo_directory_tree_walk()
