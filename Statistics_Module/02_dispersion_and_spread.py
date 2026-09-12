"""
=============================================================================
BÀI 2: CÁC ĐỘ ĐO ĐỘ PHÂN TÁN VÀ BIẾN THIÊN (Measures of Dispersion)
=============================================================================

🎯 NGUYÊN LÝ HOẠT ĐỘNG:
- **Phương sai (Variance)**: Đo lường mức độ phân tán của các điểm dữ liệu so với giá trị trung bình.
  - `statistics.variance(data)`: Phương sai mẫu (Sample Variance $s^2$, mẫu số $n - 1$).
  - `statistics.pvariance(data)`: Phương sai tổng thể (Population Variance $\sigma^2$, mẫu số $N$).
- **Độ lệch chuẩn (Standard Deviation)**: Căn bậc hai của phương sai, cùng đơn vị đo với dữ liệu ban đầu.
  - `statistics.stdev(data)`: Độ lệch chuẩn mẫu $s$.
  - `statistics.pstdev(data)`: Độ lệch chuẩn tổng thể $\sigma$.
- **Phân vị (Quantiles)**:
  - `statistics.quantiles(data, n=4)`: Chia tập dữ liệu thành `n` khoảng có xác suất bằng nhau.
  - Mặc định `n=4` trả về 3 điểm cắt của Tứ phân vị: `[Q1 (25%), Q2 (50% - Median), Q3 (75%)]`.

💡 TRƯỜNG HỢP SỬ DỤNG:
- Đo lường mức độ rủi ro / biến động giá cổ phiếu (Độ lệch chuẩn cao = Rủi ro cao).
- Phân loại học sinh hoặc khách hàng theo phân vị top 25%, top 50%.
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
    print("1. PHƯƠNG SAI VÀ ĐỘ LỆCH CHUẨN (VARIANCE & STDEV)")
    print("=" * 60)

    # Hiệu suất ghi điểm của 2 cầu thủ bóng rổ trong 6 trận đấu
    player_a_scores = [20, 21, 19, 20, 22, 18] # Thi đấu rất ổn định
    player_b_scores = [5, 35, 10, 40, 0, 30]   # Phong độ thất thường

    print(f"Cầu thủ A: {player_a_scores}")
    print(f" -> Điểm trung bình: {statistics.mean(player_a_scores):.1f}")
    print(f" -> Độ lệch chuẩn (stdev): {statistics.stdev(player_a_scores):.2f} điểm")

    print(f"\nCầu thủ B: {player_b_scores}")
    print(f" -> Điểm trung bình: {statistics.mean(player_b_scores):.1f}")
    print(f" -> Độ lệch chuẩn (stdev): {statistics.stdev(player_b_scores):.2f} điểm")

    print("\n👉 Nhận xét: Mặc dù cùng điểm trung bình là 20.0, Cầu thủ A ổn định hơn nhiều vì độ lệch chuẩn nhỏ (1.41 so với 16.73).")

    print("\n" + "=" * 60)
    print("2. TÍNH TỨ PHÂN VỊ VỚI statistics.quantiles")
    print("=" * 60)

    # Điểm thi đánh giá năng lực của 12 thí sinh (thang 100)
    exam_scores = [45, 52, 60, 68, 72, 75, 78, 82, 85, 90, 94, 98]

    # Chia làm 4 phần (Tứ phân vị Q1, Q2, Q3)
    q1, q2, q3 = statistics.quantiles(exam_scores, n=4)
    print(f"Danh sách điểm thi: {exam_scores}")
    print(f"-> Q1 (25% thí sinh đạt dưới mức này): {q1:.2f}")
    print(f"-> Q2 (50% thí sinh đạt dưới mức này): {q2:.2f} (Median)")
    print(f"-> Q3 (75% thí sinh đạt dưới mức này): {q3:.2f}")
    print(f"-> Khoảng tứ phân vị IQR (Q3 - Q1):    {q3 - q1:.2f}")

    # Chia làm 10 phần (Thập phân vị - Deciles)
    deciles = statistics.quantiles(exam_scores, n=10)
    print(f"\nĐiểm top 10% cao nhất (Decile 9): >= {deciles[-1]:.2f}")

if __name__ == "__main__":
    main()
