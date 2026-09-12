"""
=============================================================================
BÀI 4: THAY THẾ VĂN BẢN VÀ TÁCH CHUỖI VỚI re.sub & re.split
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `re.sub(pattern, repl, string, count=0)`: Tìm tất cả các đoạn khớp với pattern và thay thế bằng `repl`.
  - `repl` có thể là một chuỗi văn bản thông thường.
  - `repl` có thể chứa tham chiếu nhóm `\1`, `\2` (Backreferences).
  - `repl` có thể là một **Hàm Callback** (nhận `MatchObject` và trả về chuỗi thay thế).
- `re.subn(...)`: Tương tự `re.sub()` nhưng trả về một tuple `(chuỗi_mới, số_lượng_thay_thế)`.
- `re.split(pattern, string)`: Tách chuỗi dựa trên biểu thức chính quy (vượt trội hơn hẳn hàm `str.split()` thông thường khi cần tách theo nhiều ký tự phân tách khác nhau).

💡 TRƯỜNG HỢP SỬ DỤNG:
- Che giấu thông tin bảo mật / nhạy cảm (Masking PII: Số thẻ ngân hàng, số điện thoại).
- Làm sạch văn bản: Loại bỏ thẻ HTML, chuyển đổi định dạng ngày `YYYY-MM-DD` sang `DD/MM/YYYY`.
- Tách danh sách từ dựa trên dấu phẩy, chấm phẩy, khoảng trắng, gạch nối cùng lúc.
=============================================================================
"""

import re
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def mask_phone_number(match):
    """Callback function: Che 4 số giữa của số điện thoại"""
    full_phone = match.group(0)
    # Giữ 3 số đầu, 3 số cuối, che 4 số ở giữa bằng ****
    return f"{full_phone[:3]}****{full_phone[-3:]}"

def main():
    print("=" * 60)
    print("1. THAY THẾ VỚI re.sub & BACKREFERENCES")
    print("=" * 60)

    # Đổi định dạng ngày từ YYYY-MM-DD sang DD/MM/YYYY
    raw_text = "Hợp đồng ký ngày 2026-09-12 và gia hạn vào ngày 2027-09-12."
    # Dùng \3 (ngày), \2 (tháng), \1 (năm)
    formatted_text = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3/\2/\1", raw_text)
    print(f"Văn bản gốc:      {raw_text}")
    print(f"Đã đổi định dạng: {formatted_text}")

    print("\n" + "=" * 60)
    print("2. CHE GIẤU DỮ LIỆU NHẠY CẢM BẰNG CALLBACK FUNCTION")
    print("=" * 60)

    customer_info = "Liên hệ: Anh Minh (0901234567) hoặc Chị Lan (0987654321) để tư vấn."
    masked_info, count = re.subn(r"0\d{9}", mask_phone_number, customer_info)
    print(f"Thông tin trước khi che: {customer_info}")
    print(f"Thông tin sau khi che:   {masked_info}")
    print(f"Tổng số vị trí đã che:  {count}")

    print("\n" + "=" * 60)
    print("3. TÁCH CHUỖI PHỨC TẠP VỚI re.split")
    print("=" * 60)

    # Chuỗi có các ký tự phân cách hỗn loạn: phẩy, chấm phẩy, gạch đứng, khoảng trắng
    messy_list_str = "Táo, Cam; Chuối | Dưa Hấu   Xoài,Lê"
    clean_items = re.split(r"[,;|\s]+", messy_list_str.strip())
    print(f"Chuỗi đầu vào: '{messy_list_str}'")
    print(f"Danh sách sau khi tách sạch: {clean_items}")

if __name__ == "__main__":
    main()
