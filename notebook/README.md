# 📚 Bộ Tài Liệu & Notebook Xử Lý Dữ Liệu Thực Tế Trong Pandas (Data Cleaning & Preprocessing)

Chào mừng bạn đến với bộ tài liệu thực hành xử lý dữ liệu (Data Cleaning & Preprocessing) trong Python & Pandas. Thư mục này cung cấp các notebook mẫu cùng dữ liệu thực tế giúp bạn thành thạo từ cơ bản đến nâng cao mọi kỹ thuật tiền xử lý dữ liệu.

---

## 📂 Cấu Trúc Thư Mục

```text
notebook/
├── data/
│   ├── customer_orders_raw.csv           # Tập dữ liệu thô mô phỏng các lỗi thực tế
│   └── customer_orders_cleaned.csv       # Tập dữ liệu sạch sau khi qua pipeline
├── 01_handling_duplicates.ipynb          # Phần 1: Xử lý dữ liệu trùng lặp (Duplicates)
├── 02_handling_missing_values.ipynb      # Phần 2: Xử lý dữ liệu khuyết thiếu (Null / NaN / Imputation)
├── 03_handling_data_types.ipynb          # Phần 3: Ép kiểu và chuẩn hóa kiểu dữ liệu (Data Types)
├── 04_text_and_outlier_processing.ipynb  # Phần 4: Chuẩn hóa chuỗi ký tự & xử lý ngoại lai (Text & Outliers)
├── 05_comprehensive_pipeline.ipynb       # Phần 5: Pipeline tự động hóa toàn bộ từ A đến Z
└── README.md                             # Hướng dẫn tổng quan
```

---

## 🎯 Chi Tiết Từng Bài Học

### 1. [01_handling_duplicates.ipynb](01_handling_duplicates.ipynb)
- Phát hiện trùng lặp hoàn toàn trên tất cả các cột (`df.duplicated()`).
- Phát hiện trùng lặp theo khóa chính (`order_id`, `email`) với tham số `subset`.
- Ứng dụng các chế độ `keep='first'`, `keep='last'`, `keep=False`.
- Nhận diện trùng lặp tiềm ẩn do lỗi hoa/thường hoặc khoảng trắng thừa.
- Khử trùng lặp an toàn với `drop_duplicates()`.

### 2. [02_handling_missing_values.ipynb](02_handling_missing_values.ipynb)
- Phát hiện và thống kê missing value (`isna()`, `isnull()`, tỉ lệ %).
- Chuẩn hóa các chuỗi rỗng (`"N/A"`, `"?"`, `"-"`, `"null"`) về `np.nan`.
- Xóa dòng/cột chứa dữ liệu rỗng với `dropna()` (`how`, `thresh`, `subset`).
- Kỹ thuật điền khuyết thiếu (Imputation): Cố định, Mean, Median (cho dữ liệu có outlier), Mode (cho danh mục), Forward Fill, Backward Fill, Linear Interpolation.
- Tạo cờ báo hiệu khuyết thiếu (`is_missing`) phục vụ Machine Learning.

### 3. [03_handling_data_types.ipynb](03_handling_data_types.ipynb)
- Kiểm tra kiểu dữ liệu và tối ưu bộ nhớ RAM (`dtypes`, `info()`, `memory_usage()`).
- Làm sạch và ép kiểu số an toàn: Loại bỏ ký tự tiền tệ (`$`), dấu phẩy (`,`), phần trăm (`%`) kết hợp `pd.to_numeric(errors='coerce')`.
- Xử lý ngày tháng linh hoạt: `pd.to_datetime(format='mixed', errors='coerce')` và trích xuất năm, tháng, thứ trong tuần, ngày cuối tuần.
- Tối ưu hóa bộ nhớ lên đến 90% với kiểu `category`.
- Sử dụng kiểu số nguyên có chứa NaN (`Int64` Nullable Integer).
- Bảo toàn chuỗi số điện thoại và mã bưu điện (tránh mất số `0` ở đầu).

### 4. [04_text_and_outlier_processing.ipynb](04_text_and_outlier_processing.ipynb)
- Chuẩn hóa chuỗi văn bản: Xóa khoảng trắng thừa (`.str.strip()`), chuẩn hóa hoa/thường (`.str.title()`).
- Chuẩn hóa tên địa danh/danh mục lộn xộn bằng bảng ánh xạ (Dictionary Mapping).
- Xác thực định dạng email bằng biểu thức chính quy (Regex).
- Phát hiện giá trị ngoại lai bằng phương pháp **IQR (Interquartile Range)** và **Z-Score**.
- Xử lý Outlier: Loại bỏ (Trimming), Giới hạn biên (Capping / Winsorizing với `.clip()`).

### 5. [05_comprehensive_pipeline.ipynb](05_comprehensive_pipeline.ipynb)
- Đóng gói toàn bộ các kỹ thuật trên vào một class `DataCleaningPipeline` chuẩn mực.
- Tự động hóa xử lý từ dữ liệu thô đến dữ liệu sạch sẵn sàng cho phân tích và Machine Learning.
- Tạo báo cáo so sánh trước và sau khi làm sạch (Data Quality Audit).

---

## 🛠️ Hướng Dẫn Chạy Trên Jupyter / VS Code / Cursor
1. Cài đặt các thư viện cần thiết:
   ```bash
   pip install pandas numpy jupyter
   ```
2. Mở file `.ipynb` tương ứng và chọn kernel Python đã cài đặt để chạy từng cell (khối mã).
