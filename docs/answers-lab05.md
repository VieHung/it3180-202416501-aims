# Thảo luận: Ưu, nhược điểm của upstream first so với release first? Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?

## 1. Upstream first so với release first

Upstream first sửa trên dòng phát triển chính trước, sau đó đưa bản sửa về các nhánh release bị ảnh hưởng.

Ưu điểm là dòng phát triển chính nhận bản sửa sớm, giảm nguy cơ quên cập nhật. Tuy nhiên, bản sửa có thể cần điều chỉnh khi đưa về phiên bản cũ.

Release first sửa trực tiếp trên dòng phiên bản đang gặp lỗi, phù hợp với việc vá gấp bản đã phát hành. Sau đó phải chủ động đưa bản sửa sang master và các release khác bị ảnh hưởng.

## 2. Nếu quên sửa release/lab05, phát hiện bằng cách nào?

Theo ví dụ trong slide, kiểm tra hành vi trên cả v1.0.1, v1.1.0 và master.
Trong repo này, mốc hoàn chỉnh thay thế là v1.1.1 (giải thích ở mục 4).
Nếu mốc Lab 05 vẫn tìm "lion" ra 0 kết quả thì bản sửa chưa có.

Có thể kiểm tra thêm lịch sử các commit cherry-pick.
Không chỉ dựa vào tag --contains vì cherry-pick tạo SHA mới.

## 3. Vì sao tách commit sửa lỗi và nâng phiên bản?

Để đưa riêng mã sửa lỗi cùng regression test sang các dòng phiên bản khác, không làm chúng bị đổi về phiên bản 1.0.1.

## 4. Mốc phát hành cuối cùng của bài nộp

Tag v1.1.0 đã được đẩy lên trước khi hoàn tất bản sửa và còn khai báo
phiên bản 1.0.0. Không xóa hoặc di chuyển tag này. Bản hoàn chỉnh dùng
v1.1.1 trên release/lab05; đây là thay đổi mốc định danh so với ví dụ
v1.1.0 trong slide, nhằm giữ nguyên lịch sử đã công bố.

Hai commit cherry-pick từ bản sửa gốc
`eaab7f90b030d1bbdffd8b9db1cdbdf271b48554` được giữ nguyên:

- `a988eae`: đưa vào master qua PR #20.
- `2497553`: đã đưa vào release/lab05 qua PR #21.

## 5. Kiểm toán và tiêu chí nghiệm thu

| Dòng phiên bản | Version trong mã | Kết quả tìm "lion" | Số test |
| --- | --- | --- | --- |
| v1.0.0 (đối chứng cũ) | 1.0.0 | 0 | 4 |
| v1.0.1 / release/lab04 | 1.0.1 | 1 | 5 |
| v1.1.1 / release/lab05 | 1.1.1 | 1 | 8 |
| master | 1.1.1 | 1 | 8 |

Lệnh kiểm toán sau khi tạo tag phát hành:

```bash
git diff --stat v1.0.0 v1.0.1
git log --all --oneline --grep="cherry picked from commit eaab7f90b030d1bbdffd8b9db1cdbdf271b48554"
git cherry -v origin/master origin/release/lab04
git rev-parse 'v1.0.1^{commit}' origin/release/lab04
git rev-parse 'v1.1.1^{commit}' origin/release/lab05
```

Chênh lệch v1.0.0..v1.0.1 chỉ gồm aims/search.py, tests/test_search.py,
aims/__init__.py và CHANGELOG.md. Hai cặp SHA cuối phải bằng nhau.
Tag --contains kiểm tra quan hệ tổ tiên, không thay thế kiểm tra hành vi
khi bản sửa đã được cherry-pick sang commit có SHA khác.

## 6. CI mở rộng

Workflow `.github/workflows/ci.yml` chạy unittest với Python 3.12.
Job `test` dùng làm required status check trên master. PR thử nghiệm
`bugfix/lab05-ci-demo` cố ý làm total_cost trả về 0 để chứng minh CI
phát hiện lỗi; đóng PR này sau khi kiểm tra, không merge mã sai.

Bài thực hiện cá nhân: mọi thay đổi vào master và release/lab05 đi qua
PR, không tự tạo approval bằng tài khoản tác giả.
