# 🛣️ Module `pathlib` Trong Python (Object-Oriented Filesystem Paths)

Module `pathlib` (chuẩn hóa từ Python 3.4+) cung cấp cách tiếp cận **Hướng đối tượng (Object-Oriented Programming)** để làm việc với đường dẫn hệ thống tệp tin, thay thế hoàn toàn cách xử lý chuỗi ký tự thủ công truyền thống của `os.path`.

---

## 🧠 1. Nguyên Lý Hoạt Động Của `pathlib`

- Trong `os.path`, mọi đường dẫn chỉ là các chuỗi văn bản đơn thuần (`str`). Bạn phải nhớ hàng chục hàm rời rạc như `os.path.join()`, `os.path.exists()`, `os.path.splitext()`.
- Trong `pathlib`, mỗi đường dẫn là một **Đối tượng (Object `Path`)** thực thụ. Đối tượng này tự mang theo tất cả các phương thức và thuộc tính cần thiết:
  - Ghép nối đường dẫn bằng toán tử trực quan: `path = folder / "subfolder" / "file.txt"`
  - Tự kiểm tra: `path.exists()`, `path.is_file()`
  - Đọc ghi file trực tiếp chỉ trong 1 dòng: `content = path.read_text()`
  - Tìm kiếm tệp đệ quy: `path.rglob("*.py")`

### 🔄 Bảng So Sánh Cú Pháp: `os.path` (Cũ) vs `pathlib` (Hiện Đại Pythonic)

| Tác Vụ | Cách Viết Cũ (`os.path`) | Cách Viết Hiện Đại (`pathlib`) |
| :--- | :--- | :--- |
| **Ghép đường dẫn** | `os.path.join(a, b, c)` | `Path(a) / b / c` |
| **Lấy thư mục hiện tại** | `os.getcwd()` | `Path.cwd()` |
| **Lấy thư mục người dùng**| `os.path.expanduser("~")` | `Path.home()` |
| **Lấy đường dẫn tuyệt đối**| `os.path.abspath(p)` | `Path(p).resolve()` |
| **Kiểm tra tồn tại** | `os.path.exists(p)` | `Path(p).exists()` |
| **Tách tên file không đuôi**| `os.path.splitext(os.path.basename(p))[0]` | `Path(p).stem` |
| **Lấy đuôi mở rộng** | `os.path.splitext(p)[1]` | `Path(p).suffix` |
| **Lấy thư mục cha** | `os.path.dirname(p)` | `Path(p).parent` |
| **Tạo cây thư mục** | `os.makedirs(p, exist_ok=True)` | `Path(p).mkdir(parents=True, exist_ok=True)` |
| **Đọc toàn bộ file** | `with open(p, 'r') as f: data = f.read()` | `Path(p).read_text(encoding='utf-8')` |
| **Ghi toàn bộ file** | `with open(p, 'w') as f: f.write(data)` | `Path(p).write_text(data, encoding='utf-8')` |
| **Xóa tệp tin** | `os.remove(p)` | `Path(p).unlink(missing_ok=True)` |
| **Tìm kiếm file đệ quy**| `os.walk()` kết hợp kiểm tra đuôi | `Path(p).rglob("*.csv")` |

---

## 🎯 2. Khi Nào Nên Sử Dụng `pathlib`? (Use Cases Thực Tế)

1. **Mọi dự án Python hiện đại (Python 3.8+)**: `pathlib` là tiêu chuẩn được khuyên dùng trong PEP 428 và cộng đồng Python toàn cầu.
2. **Xử lý tệp tin cấu hình & dữ liệu nhanh gọn**: Đọc file `.json`, `.txt`, `.csv` mà không cần viết các khối `with open(...)` rườm rà.
3. **Tìm kiếm và lọc file hàng loạt**: Sử dụng cú pháp Unix Glob `.glob()` và `.rglob()` để quét toàn bộ ảnh, video, dữ liệu trong dự án.

---

## 📚 3. Danh Sách Các Bài Thực Hành Trong Thư Mục

| File | Nội Dung Trọng Tâm |
| :--- | :--- |
| [`01_path_creation_and_parts.py`](01_path_creation_and_parts.py) | Khởi tạo `Path`, toán tử chia `/`, bóc tách `.stem`, `.suffix`, `.parent`, `.parts` |
| [`02_inspection_and_query.py`](02_inspection_and_query.py) | Kiểm tra thuộc tính: `exists()`, `is_file()`, `is_dir()`, `resolve()`, `stat()` |
| [`03_fast_read_write.py`](03_fast_read_write.py) | Đọc ghi tệp siêu tốc 1 dòng lệnh với `read_text()`, `write_text()`, `read_bytes()` |
| [`04_glob_and_directory_tree.py`](04_glob_and_directory_tree.py) | Tạo thư mục lồng nhau, tìm kiếm file đệ quy với `.rglob()`, đổi tên và xóa tệp an toàn |
| [`05_os_path_vs_pathlib.py`](05_os_path_vs_pathlib.py) | Bảng đối chiếu thực nghiệm trực tiếp giữa `os.path` và `pathlib.Path` |
