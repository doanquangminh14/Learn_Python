"""
=============================================================================
BÀI 2: KÝ TỰ ĐẠI DIỆN, TẬP HỢP KÝ TỰ VÀ SỐ LƯỢNG LẶP (Quantifiers & Character Sets)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `\d`: Chữ số `[0-9]`, `\D`: Không phải số.
- `\w`: Ký tự chữ cái, chữ số và gạch dưới `[a-zA-Z0-9_]`, `\W`: Ký tự đặc biệt (dấu cách, chấm, phẩy...).
- `\s`: Khoảng trắng (space, tab `\t`, xuống dòng `\n`), `\S`: Ký tự nhìn thấy được.
- `[abc]`: Khớp một trong các ký tự a, b hoặc c.
- `[^abc]`: Khớp BẤT KỲ ký tự nào NGOẠI TRỪ a, b, c (Phủ định).
- `[a-z]`, `[A-Z]`, `[0-9]`: Dải ký tự (Ranges).
- **Lượng từ (Quantifiers)**:
  - `*`: 0 hoặc nhiều lần (Greedy).
  - `+`: 1 hoặc nhiều lần (Greedy).
  - `?`: 0 hoặc 1 lần (Tùy chọn - Optional).
  - `{n}`: Đúng `n` lần.
  - `{n,m}`: Từ `n` đến `m` lần.
- **Tham lam (Greedy) vs Lười biếng (Non-Greedy / Lazy)**:
  - Mặc định `.*` hoặc `.+` sẽ cố gắng nuốt càng nhiều ký tự càng tốt (Greedy).
  - Thêm dấu `?` phía sau (`.*?` hoặc `.+?`) để chuyển sang chế độ lười biếng (dừng lại ngay khi gặp ký tự khớp đầu tiên).

💡 TRƯỜNG HỢP SỬ DỤNG:
- Bóc tách nội dung giữa các thẻ HTML/XML (`<p>nội dung</p>`).
- Bóc tách số tiền có dấu thập phân (`$100.50`).
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
    print("1. KÝ TỰ ĐẠI DIỆN VÀ TẬP HỢP KÝ TỰ")
    print("=" * 60)

    log_sample = "IP: 192.168.1.100 - Status: 200 OK - Time: 154ms - User: admin_01"

    # Trích xuất tất cả các số nguyên
    numbers = re.findall(r"\d+", log_sample)
    print(f"Các số nguyên tìm được (\\d+): {numbers}")

    # Trích xuất tất cả các từ (từ khóa chữ & số)
    words = re.findall(r"\w+", log_sample)
    print(f"Các từ (\\w+): {words[:6]}...")

    print("\n" + "=" * 60)
    print("2. THAM LAM (GREEDY) VS LƯỜI BIẾNG (LAZY)")
    print("=" * 60)

    html_content = "<div><b>Tiêu đề 1</b> và <b>Tiêu đề 2</b></div>"
    print(f"Chuỗi HTML: {html_content}")

    # Chế độ tham lam (Greedy): Khớp từ <b> đầu tiên đến </b> cuối cùng!
    greedy_match = re.findall(r"<b>.*</b>", html_content)
    print(f"\n- Tham lam (r'<b>.*</b>'):\n  -> {greedy_match}")

    # Chế độ lười biếng (Lazy): Thêm dấu '?' để khớp từng thẻ riêng biệt
    lazy_match = re.findall(r"<b>.*?</b>", html_content)
    print(f"\n- Lười biếng (r'<b>.*?</b>'):\n  -> {lazy_match}")

    print("\n" + "=" * 60)
    print("3. PHẠM VI SỐ LƯỢNG LẶP {n, m}")
    print("=" * 60)

    codes_text = "Mã PIN: 12, 1234, 123456, 12345678, ABC"
    # Tìm các chuỗi số có độ dài từ 4 đến 6 chữ số
    pins = re.findall(r"\b\d{4,6}\b", codes_text)
    print(f"Mã PIN hợp lệ 4-6 chữ số: {pins}")

if __name__ == "__main__":
    main()
