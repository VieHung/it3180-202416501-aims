# Changelog

## [Unreleased]

## [1.1.1] - 2026-11-07

### Fixed

- Tìm DVD theo tiêu đề không phân biệt chữ hoa và chữ thường (#18).
- Đồng bộ số phiên bản, tài liệu và baseline Lab 05.

### Added

- Chạy unittest tự động bằng GitHub Actions cho PR vào master và release/**.

### Release notes

- Thay thế mốc v1.1.0 đã được gắn trước khi tích hợp đủ bản sửa.
- Giữ nguyên tag v1.1.0 đã công bố; dùng v1.1.1 làm mốc nộp hoàn chỉnh.

## [1.1.0] - 2026-11-07

### Added

- Tìm DVD theo thể loại bằng search_by_category().
- Sắp xếp giỏ hàng theo tiêu đề bằng sort_by_title().
- Sắp xếp giỏ hàng theo giá bằng sort_by_cost().

### Known issues

- Tag v1.1.0 được tạo sớm: mã còn khai báo 1.0.0 và chưa có bản sửa #18.
- Bản phát hành hoàn chỉnh được định danh lại bằng v1.1.1.

## [1.0.1] - 2026-11-07

### Fixed

- Tìm DVD theo tiêu đề không phân biệt chữ hoa và chữ thường (#18).

## [1.0.0] - 2026-11-06

### Added

- In danh sách DVD và tổng tiền bằng Cart.print_cart().
- Tìm DVD theo tiêu đề bằng search_by_title().
- Tính tổng tiền sau giảm giá bằng total_cost_with_discount().
- Khai báo và hiển thị phiên bản ứng dụng.

### Fixed

- Từ chối DVD thứ 21 khi giỏ đã chứa 20 DVD.
- Sửa công thức tính tiền sau giảm giá.
- Từ chối phần trăm giảm giá ngoài khoảng 0 đến 100.
