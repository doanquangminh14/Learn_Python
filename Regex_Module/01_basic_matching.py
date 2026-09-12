"""
=============================================================================
BÀI 1: CÁC HÀM TÌM KIẾM CƠ BẢN TRONG MODULE re
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `re.search(pattern, string)`: Quét TOÀN BỘ chuỗi và trả về vị trí khớp ĐẦU TIÊN (dưới dạng `MatchObject`), nếu không thấy trả về `None`.
- `re.match(pattern, string)`: CHỈ kiểm tra xem chuỗi có khớp ngay tại KÝ TỰ ĐẦU TIÊN hay không.
- `re.fullmatch(pattern, string)`: Yêu cầu TOÀN BỘ chuỗi từ đầu đến cuối phải khớp 100% với pattern (thích hợp validate form).
- `re.findall(pattern, string)`: Trả về một danh sách (list) chứa TẤT CẢ các chuỗi con khớp với pattern.
- `re.finditer(pattern, string)`: Trả về một iterator gồm các `MatchObject` cho từng kết quả tìm được (giúp lấy được cả vị trí bắt đầu `start()` và kết thúc `end()`).

💡 TRƯỜNG HỢP SỬ DỤNG:
- Trích xuất tất cả mã đơn hàng, số điện thoại, giá tiền từ email hoặc văn bản thô.
=============================================================================
"""

import re
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    text = "Khách hàng Minh (Mã: KH-1092) đã mua sản phẩm tại quầy 03 vào ngày 12/09/2026. Mã phụ: KH-8812."

    print("=" * 60)
    print("VĂN BẢN MẪU:")
    print(text)
    print("=" * 60)

    # 1. re.search: Tìm kiếm kết quả đầu tiên xuất hiện ở bất cứ đâu
    pattern_code = r"KH-\d{4}" # Mẫu: chữ KH- theo sau bởi đúng 4 chữ số
    search_result = re.search(pattern_code, text)

    if search_result:
        print("\n1. 🔍 re.search() tìm thấy kết quả đầu tiên:")
        print(f"   - Nội dung khớp: {search_result.group()}")
        print(f"   - Vị trí bắt đầu: {search_result.start()}, kết thúc: {search_result.end()}")
        print(f"   - Đoạn vị trí (span): {search_result.span()}")

    # 2. re.match vs re.search
    match_result = re.match(pattern_code, text)
    print(f"\n2. ❓ re.match() có tìm thấy không? -> {match_result}")
    print("   (Lý do: re.match chỉ kiểm tra từ đầu chuỗi, mà đầu chuỗi là chữ 'Khách')")

    # 3. re.findall: Tìm tất cả các kết quả
    all_codes = re.findall(pattern_code, text)
    print(f"\n3. 📋 re.findall() lấy danh sách tất cả các mã: {all_codes}")

    # 4. re.finditer: Duyệt qua từng kết quả kèm vị trí
    print("\n4. 🔄 re.finditer() duyệt chi tiết từng kết quả:")
    for match in re.finditer(pattern_code, text):
        print(f"   * Tìm thấy '{match.group()}' tại vị trí {match.span()}")

    # 5. re.fullmatch: Kiểm tra khớp toàn bộ chuỗi
    sample_id = "KH-5566"
    invalid_id = "KH-5566-EXTRA"
    print(f"\n5. 🎯 re.fullmatch:")
    print(f"   - '{sample_id}' có khớp chuẩn toàn bộ? -> {bool(re.fullmatch(pattern_code, sample_id))}")
    print(f"   - '{invalid_id}' có khớp chuẩn toàn bộ? -> {bool(re.fullmatch(pattern_code, invalid_id))}")

if __name__ == "__main__":
    main()
