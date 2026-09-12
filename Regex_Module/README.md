# 🔍 Module `re` Trong Python (Regular Expression Operations)

Module `re` cung cấp các công cụ xử lý **Biểu thức chính quy (Regular Expressions / Regex)** – một ngôn ngữ mẫu cực mạnh để tìm kiếm, trích xuất, xác thực và biến đổi văn bản.

---

## 🧠 1. Nguyên Lý Hoạt Động Của `re`

- `re` hoạt động dựa trên cơ chế **Máy tự động hữu hạn bất định (NFA - Non-deterministic Finite Automaton)**.
- Khi bạn định nghĩa một mẫu chuỗi (pattern), Python sẽ biên dịch mẫu này thành mã byte bytecode và khớp từng ký tự trên chuỗi đầu vào theo trạng thái.
- Để tăng tốc độ thực thi khi tái sử dụng một mẫu nhiều lần, bạn nên dùng `re.compile(pattern)` trước.

### 📑 Bảng Tra Cứu Ký Tự Đại Diện Thường Dùng:

| Ký Tự / Mẫu | Ý Nghĩa |
| :--- | :--- |
| `.` | Bất kỳ ký tự nào (trừ ký tự xuống dòng `\n`) |
| `^` / `$` | Khớp với đầu chuỗi / cuối chuỗi |
| `\d` / `\D` | Ký tự số `[0-9]` / Không phải số |
| `\w` / `\W` | Ký tự chữ & số & gạch dưới `[a-zA-Z0-9_]` / Ký tự đặc biệt |
| `\s` / `\S` | Khoảng trắng, tab, xuống dòng / Ký tự không phải khoảng trắng |
| `\b` | Ranh giới từ (Word boundary) |
| `*` / `+` / `?` | Lặp 0+ lần / Lặp 1+ lần / Xuất hiện 0 hoặc 1 lần |
| `{n, m}` | Lặp từ `n` đến `m` lần |
| `(...)` | Nhóm bắt giữ (Capturing Group) |
| `(?P<name>...)` | Nhóm có đặt tên (Named Capturing Group) |

---

## 🎯 2. Khi Nào Nên Sử Dụng `re`? (Use Cases Thực Tế)

1. **Xác thực Dữ liệu Người Dùng (Data Validation)**: Kiểm tra email, số điện thoại, số thẻ căn cước, mật khẩu mạnh trong form đăng ký.
2. **Khai phá & Bóc tách Dữ liệu (Information Extraction / Web Scraping)**: Trích xuất tất cả giá tiền, ngày tháng, đường link URL từ văn bản HTML/PDF.
3. **Làm sạch & Chuẩn hóa Văn bản (Text Preprocessing / NLP)**: Loại bỏ các ký tự rác, dấu câu, thẻ HTML, khoảng trắng dư thừa trước khi huấn luyện mô hình ngôn ngữ.
4. **Tìm kiếm & Thay thế Nâng cao (Advanced Search & Replace)**: Ẩn thông tin nhạy cảm (che 4 số cuối thẻ tín dụng, che số điện thoại).

---

## 📚 3. Danh Sách Các Bài Thực Hành Trong Thư Mục

| File | Nội Dung Trọng Tâm |
| :--- | :--- |
| [`01_basic_matching.py`](01_basic_matching.py) | Phân biệt `search()`, `match()`, `fullmatch()`, `findall()`, `finditer()`, đối tượng `MatchObject` |
| [`02_metacharacters_and_quantifiers.py`](02_metacharacters_and_quantifiers.py) | Các ký tự đại diện `\d, \w, \s`, tập ký tự `[]`, số lượng lặp, cơ chế Tham lam (Greedy) vs Lười biếng (Lazy) |
| [`03_groups_and_capturing.py`](03_groups_and_capturing.py) | Nhóm `()`, nhóm có tên `(?P<name>)`, trích xuất thông tin ngày tháng, họ tên |
| [`04_substitution_and_split.py`](04_substitution_and_split.py) | Thay thế với `re.sub()`, sử dụng hàm callback để biến đổi dữ liệu, tách chuỗi phức tạp với `re.split()` |
| [`05_real_world_validators.py`](05_real_world_validators.py) | Bộ thư viện kiểm tra thực tế: Email, SĐT di động Việt Nam, Mật khẩu bảo mật, URL, IPv4 |
