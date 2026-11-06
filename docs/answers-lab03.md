# Merge base là gì? Vì sao master/release/* phải dùng revert?

## 1. Merge base là gì?

Merge base là tổ tiên chung tốt nhất của hai commit hoặc hai đầu nhánh. Trong trường hợp phân nhánh thông thường, đó là commit chung gần nhất trước khi hai nhánh tách ra.

Git dùng mốc này để xác định thay đổi của từng phía khi merge.

## 2. Vì sao master và release/* phải dùng revert?

Đây là các nhánh có lịch sử đã chia sẻ.

Revert tạo commit mới đảo ngược thay đổi, giữ nguyên các commit cũ và giúp truy vết nguyên nhân hoàn tác.

Reset có thể dời đầu nhánh và khi ép cập nhật remote sẽ làm thay đổi lịch sử mà người khác đang sử dụng.