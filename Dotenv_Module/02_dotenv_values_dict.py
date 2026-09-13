"""
=============================================================================
BÀI 2: ĐỌC CẤU HÌNH VÀO DICTIONARY VỚI `dotenv_values`
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `dotenv_values(dotenv_path=None)`:
  + Phân tích cú pháp file `.env` và trả về một `OrderedDict` chứa toàn bộ cặp key-value.
  + **Đặc điểm quan trọng**: KHÔNG làm thay đổi biến môi trường hệ thống (`os.environ`).
  + Rất hữu ích khi bạn muốn:
    1. Kiểm tra/duyệt qua toàn bộ cấu hình một cách có kiểm soát.
    2. Tránh làm "ô nhiễm" (pollute) biến môi trường toàn cục của tiến trình.
    3. Kết hợp nhiều file config độc lập vào các dictionary khác nhau.
=============================================================================
"""

import os
import sys
from dotenv import dotenv_values

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. ĐỌC FILE .env TRỰC TIẾP VÀO DICTIONARY")
    print("=" * 60)

    demo_env_file = "demo_dict.env"
    with open(demo_env_file, "w", encoding="utf-8") as f:
        f.write("DB_HOST=192.168.1.100\n")
        f.write("DB_PORT=3306\n")
        f.write("DB_USER=admin\n")
        f.write("DB_PASS=secret123456\n")
        f.write("CACHE_ENABLED=true\n")

    # Đọc cấu hình vào dictionary
    config = dotenv_values(demo_env_file)
    print(f"Kiểu dữ liệu trả về: {type(config).__name__}")
    print(f"Số lượng biến đã đọc: {len(config)}\n")

    print("Danh sách các cấu hình:")
    for key, value in config.items():
        # Ẩn bớt mật khẩu khi log ra màn hình
        masked_val = "********" if "PASS" in key or "SECRET" in key else value
        print(f" - {key:15}: {masked_val}")

    print("\n" + "=" * 60)
    print("2. SO SÁNH VỚI os.environ (KHÔNG BỊ ẢNH HƯỞNG)")
    print("=" * 60)

    # Biến 'DB_HOST' không nằm trong os.environ vì dotenv_values không nạp vào hệ thống
    system_val = os.getenv("DB_HOST")
    print(f"Giá trị DB_HOST trong os.environ: {system_val} (None là đúng vì chưa nạp)")

    # Dọn dẹp file tạm
    if os.path.exists(demo_env_file):
        os.remove(demo_env_file)
    print("\n🧹 Đã dọn dẹp file demo thành công!")

if __name__ == "__main__":
    main()
