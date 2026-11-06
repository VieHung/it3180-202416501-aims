# Thảo luận: Ưu, nhược điểm của upstream first so với release first? Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?

## 1. Upstream first so với release first

Upstream first sửa trên dòng phát triển chính trước, sau đó đưa bản sửa về các nhánh release bị ảnh hưởng.

Ưu điểm là dòng phát triển chính nhận bản sửa sớm, giảm nguy cơ quên cập nhật. Tuy nhiên, bản sửa có thể cần điều chỉnh khi đưa về phiên bản cũ.

Release first sửa trực tiếp trên dòng phiên bản đang gặp lỗi, phù hợp với việc vá gấp bản đã phát hành. Sau đó phải chủ động đưa bản sửa sang master và các release khác bị ảnh hưởng.

## 2. Nếu quên sửa release/lab05, phát hiện bằng cách nào?

Chạy kiểm tra hành vi trên cả v1.0.1, v1.1.0 và master.
Nếu v1.1.0 vẫn tìm "lion" ra 0 kết quả thì bản sửa chưa có.

Có thể kiểm tra thêm lịch sử các commit cherry-pick.
Không chỉ dựa vào tag --contains vì cherry-pick tạo SHA mới.

## 3. Vì sao tách commit sửa lỗi và nâng phiên bản?

Để đưa riêng mã sửa lỗi cùng regression test sang các dòng phiên bản khác, không làm chúng bị đổi về phiên bản 1.0.1.
