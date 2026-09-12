# 🖥️ Module `os` Trong Python (Miscellaneous Operating System Interfaces)

Module `os` cung cấp hàng trăm hàm giúp lập trình viên tương tác trực tiếp với **Hệ điều hành (Operating System)** một cách độc lập với nền tảng (chạy mượt mà trên cả Windows, Linux và macOS).

---

## 🧠 1. Nguyên Lý Hoạt Động Của `os`

- `os` đóng vai trò là một lớp trừu tượng (Abstraction Layer) bọc quanh các **System Calls (lời gọi hệ thống)** cấp thấp viết bằng ngôn ngữ C của nhân hệ điều hành (như POSIX API trên Linux/macOS hay Win32 API trên Windows).
- Khi bạn gọi `os.mkdir()`, Python sẽ tự động dịch sang lời gọi API tạo thư mục tương ứng của hệ điều hành đó.
- Module con `os.path` xử lý việc ghép nối đường dẫn với dấu phân cách phù hợp (`\` trên Windows, `/` trên Linux).

---

## 🎯 2. Khi Nào Nên Sử Dụng `os`? (Use Cases Thực Tế)

1. **Quản lý Thư mục & Tệp tin**: Tạo thư mục mới (`mkdir`, `makedirs`), đổi tên, xóa file rác, lấy kích thước file.
2. **Xử lý Biến môi trường (Environment Variables)**: Đọc các cấu hình bí mật như `API_KEY`, `DATABASE_URL`, `PORT` từ file `.env` hoặc hệ điều hành qua `os.getenv()`.
3. **Quét và Duyệt Cây Thư Mục Đệ Quy (`os.walk`)**: Tìm kiếm tất cả các file ảnh `.png`, file log `.log` trong hàng nghìn thư mục con để nén hoặc sao lưu.
4. **Xử lý Đường dẫn An Toàn (`os.path`)**: Ghép nối đường dẫn với `os.path.join()` để tránh lỗi gãy đường dẫn khi chuyển code từ Windows sang server Linux.

---

## 📚 3. Danh Sách Các Bài Thực Hành Trong Thư Mục

| File | Nội Dung Trọng Tâm |
| :--- | :--- |
| [`01_directory_and_navigation.py`](01_directory_and_navigation.py) | Lấy thư mục hiện tại (`getcwd`), chuyển thư mục (`chdir`), tạo thư mục đơn & lồng nhau (`mkdir`, `makedirs`) |
| [`02_file_operations.py`](02_file_operations.py) | Đổi tên tệp (`rename`), xóa tệp an toàn (`remove`), đọc metadata của file (`stat`) |
| [`03_os_path_manipulation.py`](03_os_path_manipulation.py) | Ghép đường dẫn đa nền tảng (`join`), kiểm tra tồn tại (`exists`, `isfile`, `isdir`), tách đuôi mở rộng (`splitext`) |
| [`04_environment_and_walk.py`](04_environment_and_walk.py) | Quản lý biến môi trường (`os.getenv`, `os.environ`), duyệt toàn bộ cây thư mục với `os.walk()` |
