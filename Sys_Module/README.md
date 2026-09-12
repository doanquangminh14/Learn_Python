# 💻 Module `sys` Trong Python (System-Specific Parameters and Functions)

Module `sys` cung cấp các biến và hàm giúp chương trình Python tương tác trực tiếp với **Trình thông dịch Python (Python Interpreter)** và môi trường Runtime của nó.

---

## 🧠 1. Nguyên Lý Hoạt Động Của `sys`

- `sys` không tương tác sâu vào phần cứng hay thao tác file cấp thấp như `os`, mà nó quản lý **trạng thái nội bộ của Python Interpreter**.
- Khi một tiến trình Python khởi chạy, `sys` được nạp tự động vào bộ nhớ để lưu giữ:
  1. Các tham số dòng lệnh được truyền vào (`sys.argv`).
  2. Danh sách các thư mục mà Python sẽ tìm kiếm khi bạn gõ lệnh `import` (`sys.path`).
  3. Các luồng vào/ra tiêu chuẩn của hệ thống (`sys.stdin`, `sys.stdout`, `sys.stderr`).
  4. Thông tin về phiên bản Python, hệ điều hành nền tảng (`sys.version`, `sys.platform`).
  5. Quản lý vòng đời của tiến trình: Thoát chương trình với mã trạng thái (`sys.exit()`) và quản lý giới hạn đệ quy (`sys.setrecursionlimit()`).

---

## 🎯 2. Khi Nào Nên Sử Dụng `sys`? (Use Cases Thực Tế)

1. **Xây dựng ứng dụng dòng lệnh (CLI Tools / Automation Scripts)**: Nhận tham số từ terminal, xử lý cờ tùy chọn (`--input`, `--mode`).
2. **Quản lý Import & Modular Code**: Khi import module ở các thư mục cha hoặc thư mục con bị lỗi (`ModuleNotFoundError`), bạn có thể thêm đường dẫn vào `sys.path`.
3. **Chuyển hướng Output / Ghi Log Lỗi (Streams Redirection)**: Ghi log lỗi riêng biệt sang `stderr` hoặc chuyển hướng toàn bộ `stdout` vào file log.
4. **Kiểm tra tương thích môi trường**: Đảm bảo code chỉ chạy trên Python >= 3.10 hoặc chỉ chạy trên Windows / Linux.
5. **Đo lường bộ nhớ (Memory Profiling)**: Kiểm tra dung lượng RAM mà một object (dict, list, string) đang chiếm dụng bằng `sys.getsizeof()`.

---

## 📚 3. Danh Sách Các Bài Thực Hành Trong Thư Mục

| File | Nội Dung Trọng Tâm |
| :--- | :--- |
| [`01_command_line_args.py`](01_command_line_args.py) | Xử lý tham số dòng lệnh với `sys.argv`, viết CLI parser mini có kiểm tra lỗi |
| [`02_system_info_and_paths.py`](02_system_info_and_paths.py) | Khám phá `sys.version`, `sys.platform`, cơ chế tìm kiếm module với `sys.path` |
| [`03_standard_streams.py`](03_standard_streams.py) | Làm chủ `sys.stdin`, `sys.stdout`, `sys.stderr`, chuyển hướng output vào file |
| [`04_memory_and_exit.py`](04_memory_and_exit.py) | Đo dung lượng object với `sys.getsizeof()`, mã thoát `sys.exit()`, cấu hình đệ quy |
