"""
=============================================================================
BÀI 5: ĐỐI CHIẾU TRỰC TIẾP CÚ PHÁP: os.path vs pathlib.Path
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `os.path` dựa trên cách xử lý chuỗi (String-based): Bạn liên tục phải truyền chuỗi vào các hàm lồng nhau.
- `pathlib` dựa trên lập trình hướng đối tượng (Object-based): Bạn gọi phương thức và thuộc tính trực tiếp trên đối tượng đường dẫn (Method Chaining).

💡 BÀI TẬP THỰC HÀNH:
Chạy cùng một bài toán xử lý đường dẫn bằng cả 2 cách để thấy sự tinh gọn, trực quan và hiện đại của `pathlib`.
=============================================================================
"""

import os
from pathlib import Path
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def solve_with_os_module():
    """Giải quyết bài toán bằng cách viết truyền thống (os & os.path)"""
    print("--- 1. Cách Làm Cũ (os / os.path) ---")
    
    # 1. Ghép đường dẫn
    base = "project"
    sub = "data"
    filename = "sales_2026.csv"
    full_path = os.path.join(base, sub, filename)
    print(f"Ghép đường dẫn:     {full_path}")

    # 2. Lấy tên file và đuôi
    base_name = os.path.basename(full_path)
    stem_name, ext = os.path.splitext(base_name)
    parent_dir = os.path.dirname(full_path)

    print(f"Thư mục cha:        {parent_dir}")
    print(f"Tên file không đuôi: {stem_name}")
    print(f"Đuôi mở rộng:       {ext}")

    # 3. Đổi đuôi thành .json
    new_path = os.path.join(parent_dir, stem_name + ".json")
    print(f"Đường dẫn sau đổi đuôi: {new_path}")

def solve_with_pathlib_module():
    """Giải quyết bài toán bằng cách viết hiện đại (pathlib.Path)"""
    print("\n--- 2. Cách Làm Hiện Đại (pathlib.Path) ---")

    # 1. Ghép đường dẫn với toán tử /
    full_path = Path("project") / "data" / "sales_2026.csv"
    print(f"Ghép đường dẫn:     {full_path}")

    # 2. Lấy tên file và đuôi qua thuộc tính
    print(f"Thư mục cha:        {full_path.parent}")
    print(f"Tên file không đuôi: {full_path.stem}")
    print(f"Đuôi mở rộng:       {full_path.suffix}")

    # 3. Đổi đuôi chỉ với 1 phương thức
    new_path = full_path.with_suffix(".json")
    print(f"Đường dẫn sau đổi đuôi: {new_path}")

def main():
    print("=" * 60)
    print("SO SÁNH CÚ PHÁP: os.path VS pathlib.Path")
    print("=" * 60)
    solve_with_os_module()
    solve_with_pathlib_module()
    print("\n👉 Kết luận: 'pathlib' ngắn hơn, đọc tự nhiên hơn và hạn chế tối đa lỗi cú pháp chuỗi!")

if __name__ == "__main__":
    main()
