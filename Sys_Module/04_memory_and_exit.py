"""
=============================================================================
BÀI 4: QUẢN LÝ BỘ NHỚ, MÃ THOÁT VÀ CẤU HÌNH ĐỆ QUY (Memory, sys.exit, Recursion)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `sys.getsizeof(object)`: Trả về kích thước bộ nhớ (tính bằng bytes) mà một object đang chiếm dụng trong RAM.
- `sys.exit([arg])`: Thoát chương trình một cách an toàn bằng cách raise ngoại lệ `SystemExit`.
  - `sys.exit(0)`: Báo hiệu cho Hệ điều hành rằng chương trình đã kết thúc THÀNH CÔNG.
  - `sys.exit(1)` (hoặc mã khác 0): Báo hiệu chương trình kết thúc vì có LỖI (giúp các tiến trình khác như Docker, Bash Script, CI/CD phát hiện thất bại).
- `sys.getrecursionlimit()` & `sys.setrecursionlimit()`: Kiểm soát độ sâu tối đa của hàm đệ quy để chống tràn ngăn xếp (Stack Overflow).

💡 TRƯỜNG HỢP SỬ DỤNG:
- So sánh hiệu năng và dung lượng bộ nhớ giữa List vs Generator, Dict vs Tuple.
- Dừng kịch bản tự động hóa và gửi Exit Code chuẩn cho CI/CD pipeline.
- Tăng giới hạn đệ quy khi giải các bài toán thuật toán đồ thị, DFS trên cây lớn.
=============================================================================
"""

import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def demo_memory_size():
    """Đo lường dung lượng bộ nhớ của các kiểu dữ liệu"""
    print("=" * 60)
    print("1. ĐO LƯỜNG DUNG LƯỢNG BỘ NHỚ (sys.getsizeof)")
    print("=" * 60)

    num = 42
    string_short = "Hello"
    string_long = "Hello" * 1000
    empty_list = []
    filled_list = list(range(1000))
    gen_exp = (x for x in range(1000))

    print(f"Số nguyên (42):                     {sys.getsizeof(num):>6} bytes")
    print(f"Chuỗi ngắn ('Hello'):               {sys.getsizeof(string_short):>6} bytes")
    print(f"Chuỗi dài (5000 ký tự):             {sys.getsizeof(string_long):>6} bytes")
    print(f"Danh sách rỗng []:                  {sys.getsizeof(empty_list):>6} bytes")
    print(f"Danh sách 1,000 phần tử (List):     {sys.getsizeof(filled_list):>6} bytes")
    print(f"Bộ sinh 1,000 phần tử (Generator):  {sys.getsizeof(gen_exp):>6} bytes  <-- Siêu tiết kiệm RAM!")

def demo_recursion_limit():
    """Kiểm tra và cấu hình giới hạn đệ quy"""
    print("\n" + "=" * 60)
    print("2. QUẢN LÝ ĐỘ SÂU ĐỆ QUY (Recursion Limit)")
    print("=" * 60)

    current_limit = sys.getrecursionlimit()
    print(f"Giới hạn đệ quy mặc định của Python: {current_limit}")

    # Tăng giới hạn đệ quy (chú ý: cần thận trọng để tránh crash tiến trình)
    new_limit = 2000
    sys.setrecursionlimit(new_limit)
    print(f"Đã nâng giới hạn đệ quy lên: {sys.getrecursionlimit()}")

    # Khôi phục về mặc định
    sys.setrecursionlimit(current_limit)

def demo_exit_status():
    """Giải thích cơ chế sys.exit và mã trả về"""
    print("\n" + "=" * 60)
    print("3. CƠ CHẾ sys.exit() VÀ EXIT CODES")
    print("=" * 60)
    print("Khi muốn dừng chương trình:")
    print("  -> sys.exit(0) : Hoàn thành xuất sắc, không có lỗi.")
    print("  -> sys.exit(1) : Dừng do lỗi chung (General error).")
    print("  -> sys.exit(2) : Dừng do truyền sai tham số dòng lệnh.")
    print("\nVí dụ minh họa cách bắt SystemExit an toàn:")
    
    try:
        print("Đang chuẩn bị thoát có kiểm soát...")
        # Giả lập lệnh exit để xem cách hoạt động
        # sys.exit(0)
    except SystemExit as e:
        print(f"Bắt được sự kiện thoát chương trình với mã code: {e.code}")

if __name__ == "__main__":
    demo_memory_size()
    demo_recursion_limit()
    demo_exit_status()
