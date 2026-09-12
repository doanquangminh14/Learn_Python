"""
=============================================================================
BÀI 1: XỬ LÝ THAM SỐ DÒNG LỆNH VỚI sys.argv (Command Line Arguments)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `sys.argv` là một danh sách (list) chứa tất cả các tham số được truyền vào từ
  dòng lệnh (terminal / command prompt) khi bạn chạy lệnh: `python script.py arg1 arg2`
- Phần tử đầu tiên `sys.argv[0]` LUÔN LUÔN là tên hoặc đường dẫn của chính file script đang chạy.
- Các phần tử tiếp theo `sys.argv[1]`, `sys.argv[2]`, ... là các đối số truyền vào (luôn ở dạng STRING).

💡 TRƯỜNG HỢP SỬ DỤNG:
- Viết các tool tự động hóa (Automation Script), CLI tools nhận file đầu vào/ra.
- Truyền cấu hình (ví dụ: `--env=production`, `--port=8080`).
=============================================================================
"""

import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("THÔNG TIN THAM SỐ DÒNG LỆNH (sys.argv)")
    print("=" * 60)

    # 1. Hiển thị toàn bộ danh sách tham số
    print(f"Toàn bộ sys.argv: {sys.argv}")
    print(f"Tổng số lượng tham số truyền vào: {len(sys.argv)}")
    print(f"Tên file script đang chạy (sys.argv[0]): {sys.argv[0]}\n")

    # 2. Xử lý kịch bản thực tế: Máy tính mini qua dòng lệnh
    # Cú pháp mong muốn: python 01_command_line_args.py <so_1> <phep_tinh: +|-|*|/> <so_2>
    if len(sys.argv) < 4:
        print("💡 [HƯỚNG DẪN SỬ DỤNG]:")
        print("   Vui lòng truyền thêm tham số khi chạy:")
        print("   Ví dụ: python 01_command_line_args.py 10 + 20")
        print("   Ví dụ: python 01_command_line_args.py 50 * 3")
        print("\n-> Đang chạy chế độ demo mặc định với tham số mẫu (100 / 4)...")
        
        # Giả lập tham số mẫu để script chạy được ngay
        num1, op, num2 = 100.0, "/", 4.0
    else:
        try:
            num1 = float(sys.argv[1])
            op = sys.argv[2]
            num2 = float(sys.argv[3])
        except ValueError:
            print("❌ Lỗi: Tham số thứ nhất và thứ ba phải là số hợp lệ!")
            sys.exit(1)

    # 3. Tính toán kết quả
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("❌ Lỗi: Không thể chia cho 0!")
            sys.exit(1)
        result = num1 / num2
    else:
        print(f"❌ Phép tính '{op}' không được hỗ trợ! Chỉ hỗ trợ +, -, *, /")
        sys.exit(1)

    print(f"✅ Kết quả tính toán: {num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()
