# Vì sao phải đồng bộ master trước khi PR? Khi nào không được rebase? feature/* khác topic/* ra sao?


## 1. Vì sao phải đồng bộ master trước khi PR?

Để kiểm tra tính năng trên mã nguồn mới nhất, phát hiện sớm
xung đột và lỗi tích hợp. Một nhánh chạy đúng riêng lẻ chưa
chứng minh nó tương thích với các thay đổi vừa được merge.

## 2. Khi nào không được rebase?

Theo quy ước học phần, không dùng rebase để viết lại các
commit đã push và chia sẻ, đặc biệt trên master và release/*.
Việc đổi SHA có thể làm lệch lịch sử của người khác.

Thao tác Rebase and merge trên GitHub trong bài là cách tích
hợp PR, khác với tự rebase rồi force-push lịch sử nhánh chung.

## 3. feature/* khác topic/* ra sao?

feature/* dùng cho tính năng, ví dụ in giỏ hàng và tìm kiếm.
topic/* dùng cho một chủ đề công việc, ví dụ PR template
hoặc tài liệu use case. Đây là quy ước đặt tên của dự án.

