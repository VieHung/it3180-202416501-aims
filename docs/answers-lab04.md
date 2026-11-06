# Vì sao release/* không merge vào master? So sánh với GitFlow. Vì sao lên 1.0.0 mà không phải 0.4.0?

## Vì sao release/* không merge ngược vào master?

Theo Release Flow của học phần, master là dòng phát triển chính, còn release/* giữ dòng phiên bản đã nộp hoặc phát hành.

Khi có bản sửa trên release, đưa đúng phần sửa cần thiết về master theo quy trình hotfix, tránh kéo cả thay đổi riêng của phiên bản cũ vào dòng phát triển mới.

## So sánh với GitFlow

Release Flow của học phần phát triển trên master và tạo release/* từ master.

GitFlow có hai nhánh chính master và develop. Nhánh release được tạo từ develop; khi hoàn tất, thay đổi được merge vào master và trở lại develop.


## Vì sao dùng 1.0.0 thay vì 0.4.0?

Học phần chọn Lab 4 làm mốc phát hành ổn định đầu tiên. Số phiên bản biểu thị mức độ ổn định và tương thích, không phải số thứ tự bài lab.