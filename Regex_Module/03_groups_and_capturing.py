"""
=============================================================================
BÀI 3: NHÓM BẮT GIỮ (CAPTURING GROUPS) VÀ NHÓM CÓ TÊN (NAMED GROUPS)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- Cặp ngoặc đơn `(pattern)` tạo ra một **Capturing Group** (Nhóm bắt giữ).
  - Giúp trích xuất riêng từng phần nhỏ trong một mẫu khớp lớn.
  - `match.group(1)`: Lấy giá trị của nhóm thứ nhất, `match.group(2)`: Nhóm thứ hai...
  - `match.group(0)` hoặc `match.group()`: Lấy toàn bộ chuỗi khớp.
- **Named Groups `(?P<name>pattern)`**: Đặt tên cho nhóm giúp code dễ đọc, dễ bảo trì và có thể truy xuất qua `match.group('name')` hoặc `match.groupdict()`.
- **Non-capturing Groups `(?:pattern)`**: Gom nhóm logic nhưng không lưu vào bộ nhớ bắt giữ (giúp tăng tốc độ).

💡 TRƯỜNG HỢP SỬ DỤNG:
- Bóc tách ngày tháng: Phân tách ngày, tháng, năm từ chuỗi `2026-09-12`.
- Phân tích cú pháp URL: Tách riêng Protocol (`https`), Domain (`google.com`), Port (`443`), Path (`/search`).
- Phân tích Log Server Apache / Nginx.
=============================================================================
"""

import re
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. NHÓM ĐÁNH SỐ THỨ TỰ (Numbered Capturing Groups)")
    print("=" * 60)

    date_str = "Hạn nộp hồ sơ là ngày 2026-09-12 tại văn phòng."
    # Pattern bóc tách Năm-Tháng-Ngày: (YYYY)-(MM)-(DD)
    date_pattern = r"(\d{4})-(\d{2})-(\d{2})"

    match = re.search(date_pattern, date_str)
    if match:
        print(f"Chuỗi khớp toàn bộ (group 0): {match.group(0)}")
        print(f"Năm (group 1):               {match.group(1)}")
        print(f"Tháng (group 2):             {match.group(2)}")
        print(f"Ngày (group 3):              {match.group(3)}")
        print(f"Tất cả các groups (tuple):   {match.groups()}")

    print("\n" + "=" * 60)
    print("2. NHÓM CÓ ĐẶT TÊN (Named Capturing Groups: (?P<name>...))")
    print("=" * 60)

    # Phân tích log server
    log_line = "GET /api/v1/users?id=100 200 45ms"
    log_pattern = r"(?P<method>GET|POST|PUT|DELETE)\s+(?P<path>[^\s]+)\s+(?P<status_code>\d{3})\s+(?P<response_time>\d+ms)"

    log_match = re.search(log_pattern, log_line)
    if log_match:
        # Truy xuất qua tên
        print(f"HTTP Method:   {log_match.group('method')}")
        print(f"Endpoint Path: {log_match.group('path')}")
        print(f"Status Code:   {log_match.group('status_code')}")
        print(f"Response Time: {log_match.group('response_time')}")

        # Trích xuất toàn bộ sang Python Dictionary cực kỳ tiện lợi
        log_dict = log_match.groupdict()
        print(f"\nChuyển đổi thành Dictionary:\n{log_dict}")

if __name__ == "__main__":
    main()
