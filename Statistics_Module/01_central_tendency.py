"""
=============================================================================
BÀI 1: CÁC ĐỘ ĐO XU HƯỚNG TẬP TRUNG (Measures of Central Tendency)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- `statistics.mean(data)`: Giá trị trung bình cộng số học (Arithmetic Mean).
- `statistics.fmean(data)`: Chuyển dữ liệu sang float và tính trung bình với tốc độ cực nhanh (nhanh hơn `mean()` từ 2 đến 10 lần).
- `statistics.median(data)`: Trung vị - giá trị nằm chính giữa khi sắp xếp dữ liệu (miễn nhiễm với Outlier ngoại lai).
- `statistics.median_low(data)` & `statistics.median_high(data)`: Giá trị trung vị cận dưới / cận trên khi số lượng phần tử là chẵn.
- `statistics.mode(data)`: Yếu vị - giá trị xuất hiện nhiều lần nhất.
- `statistics.multimode(data)`: Trả về danh sách TẤT CẢ các yếu vị (khi có nhiều giá trị cùng có tần suất cao nhất).
- `statistics.geometric_mean(data)`: Trung bình nhân $\sqrt[n]{x_1 \cdot x_2 \dots x_n}$ (dùng cho lãi suất, tỷ lệ tăng trưởng).
- `statistics.harmonic_mean(data)`: Trung bình điều hòa (dùng cho vận tốc trung bình, tỷ số giá).

💡 TRƯỜNG HỢP SỬ DỤNG:
- Đo lường thu nhập trung bình (nên dùng Median vì tránh bị méo bởi tỷ phú).
- Tính tốc độ tăng trưởng doanh thu hàng năm CAGR (dùng Geometric Mean).
=============================================================================
"""

import statistics
import sys

# Cấu hình UTF-8 cho console Windows
if sys.platform.startswith("win"):
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    print("=" * 60)
    print("1. TRUNG BÌNH CỘNG (MEAN) VS TRUNG VỊ (MEDIAN)")
    print("=" * 60)

    # Lương hàng tháng của 6 nhân viên và 1 giám đốc (đơn vị: triệu VNĐ)
    salaries = [12, 14, 15, 15, 18, 20, 350] # 350 là giá trị ngoại lai (outlier)

    avg_mean = statistics.mean(salaries)
    fast_mean = statistics.fmean(salaries)
    med = statistics.median(salaries)

    print(f"Dữ liệu lương: {salaries}")
    print(f"-> Trung bình cộng (mean):  {avg_mean:.2f} triệu VNĐ  (Bị kéo lệch bởi mức lương 350tr)")
    print(f"-> Trung bình nhanh (fmean): {fast_mean:.2f} triệu VNĐ")
    print(f"-> Trung vị thực tế (median): {med:.2f} triệu VNĐ  (Phản ánh chính xác mức lương phổ thông)")

    print("\n" + "=" * 60)
    print("2. YẾU VỊ (MODE & MULTIMODE)")
    print("=" * 60)

    # Khảo sát size áo của khách hàng
    shirt_sizes = ["M", "L", "M", "S", "XL", "M", "L", "L", "XXL"]
    print(f"Dữ liệu size áo: {shirt_sizes}")
    
    # Có 2 size M và L đều xuất hiện 3 lần
    modes = statistics.multimode(shirt_sizes)
    print(f"-> Các size bán chạy nhất (multimode): {modes}")

    print("\n" + "=" * 60)
    print("3. TRUNG BÌNH NHÂN & ĐIỀU HÒA (GEOMETRIC & HARMONIC MEAN)")
    print("=" * 60)

    # Bài toán 1: Tỷ lệ tăng trưởng doanh thu 3 năm liên tiếp (5%, 15%, 25% tương ứng 1.05, 1.15, 1.25)
    growth_rates = [1.05, 1.15, 1.25]
    geo_mean = statistics.geometric_mean(growth_rates)
    print(f"Tốc độ tăng trưởng trung bình hàng năm: {(geo_mean - 1) * 100:.2f}%")

    # Bài toán 2: Xe đi từ A đến B với 40 km/h, quay về từ B về A với 60 km/h
    # Vận tốc trung bình cả chuyến đi không phải là (40+60)/2 = 50 mà phải tính theo Harmonic Mean!
    speeds = [40, 60]
    avg_speed = statistics.harmonic_mean(speeds)
    print(f"Vận tốc trung bình cả hành trình (Harmonic Mean): {avg_speed:.2f} km/h")

if __name__ == "__main__":
    main()
