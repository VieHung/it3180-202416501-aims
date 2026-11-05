# Vì sao dùng git mv? release/lab01 có phải baseline? Vì sao không commit thẳng master dù làm một mình?

## Câu 1 — Vì sao nên dùng `git mv`?

`git mv` giúp đổi tên hoặc di chuyển tệp đang được Git theo dõi, đồng thời cập nhật vùng chuẩn bị commit (index). Việc gộp các thao tác này trong một lệnh giúp giảm sai sót khi tổ chức lại mã nguồn. Mặc định, lệnh từ chối ghi đè tệp đích đã tồn tại, trừ khi dùng tùy chọn ép buộc. Đây là sự tiện lợi trong thao tác, không phải cam kết rằng toàn bộ quá trình là một giao dịch nguyên tử. 

Git lưu các trạng thái của cây thư mục, không lưu riêng một sự kiện đổi tên trong commit. Khi so sánh các trạng thái, Git có thể suy luận việc đổi tên từ độ tương đồng giữa tệp cũ và tệp mới. Vì vậy, di chuyển tệp bằng công cụ khác rồi stage đầy đủ cả đường dẫn cũ và mới cũng có thể cho kết quả tương đương.

Khi bật nhận diện đổi tên bằng `git diff -M`, ngưỡng tương đồng mặc định là 50% và có thể điều chỉnh. Do đó, `git mv` không bảo đảm mọi công cụ luôn hiển thị thay đổi dưới dạng rename.

Về cách tổ chức công việc, nên tách thay đổi cấu trúc và thay đổi hành vi khi điều đó giúp người đọc hiểu rõ từng bước. Tuy nhiên, mỗi commit vẫn nên giữ trạng thái nhất quán; việc di chuyển mã nguồn có thể cần đi kèm cập nhật import hoặc cấu hình liên quan.

## Câu 2 — Release branch có phải là baseline không?

Trong quản lý cấu hình, baseline là một cấu hình đã được xem xét, chấp thuận và định danh để làm mốc tham chiếu. Những thay đổi tiếp theo đối với cấu hình đó phải được kiểm soát và truy vết. Baseline có thể bao gồm mã nguồn, tài liệu, cấu hình và các thành phần cần thiết để tái tạo một phiên bản.

Release branch và baseline có vai trò khác nhau. Release branch hỗ trợ chuẩn bị, ổn định hoặc bảo trì một phiên bản; đầu nhánh có thể tiếp tục dịch chuyển khi có commit mới. Vì vậy, chỉ tên nhánh chưa đủ để xác định chính xác cấu hình đã được chốt.

| Thành phần | Vai trò đối với baseline |
| --- | --- |
| Release branch | Tổ chức công việc liên quan đến một dòng phát hành |
| Commit cụ thể | Xác định chính xác trạng thái mã nguồn được chọn |
| Tag | Đặt tên dễ tra cứu cho mốc đã chốt |
| Hồ sơ phát hành và phê duyệt | Ghi nhận phạm vi, kết quả kiểm tra và việc chấp thuận mốc đó |

Trong Git, có thể ghi nhận baseline bằng một commit cụ thể, một tag và hồ sơ chấp thuận tương ứng. Annotated tag bổ sung người tạo, thời điểm và thông điệp; tag cũng có thể được ký để hỗ trợ xác minh. Tuy nhiên, tag vẫn có thể bị xóa hoặc tạo lại, nên tính ổn định cần được duy trì bằng quy ước và quyền bảo vệ phù hợp. Với tag đã công bố, nên tạo mốc mới khi cần điều chỉnh thay vì âm thầm thay thế mốc cũ. 

Việc tạo tag hoặc trang phát hành tự nó chưa chứng minh một cấu hình đã được chấp thuận làm baseline. Ngược lại, baseline cũng không bắt buộc phải được biểu diễn bằng tag nếu hệ thống quản lý cấu hình có cơ chế định danh và kiểm soát tương đương.

Kết luận: Release branch phục vụ quá trình phát hành; baseline là cấu hình cụ thể đã được chấp thuận làm mốc tham chiếu. Commit, tag và hồ sơ phát hành giúp định danh, công bố và truy vết mốc đó.

## Câu 3 — Vì sao nên qua nhánh và pull request dù làm một mình?

Khi nhánh chính được dùng làm phiên bản tham chiếu chung hoặc nguồn phát hành, nên có bước kiểm tra trước khi đưa thay đổi vào đó. Nhánh làm việc và pull request (PR) tạo một quy trình rõ ràng để chuẩn bị, đánh giá và hợp nhất thay đổi.

Quy trình này vẫn hữu ích với một người phát triển:

1. **Tạo điểm tự kiểm tra:** Xem lại toàn bộ diff, mô tả mục đích và kiểm tra kết quả trước khi hợp nhất.
2. **Cô lập công việc đang làm:** Thử nghiệm hoặc tạm dừng một thay đổi mà vẫn giữ nhánh chính ở trạng thái phù hợp với quy ước dự án.
3. **Lưu bối cảnh quyết định:** PR ghi lại lý do, phạm vi và bằng chứng kiểm tra để thuận tiện khi quay lại hoặc bàn giao.
4. **Hỗ trợ xử lý sự cố:** Các đơn vị thay đổi có phạm vi rõ ràng giúp tìm nguyên nhân và lựa chọn phần cần hoàn tác.
5. **Thực thi quy tắc chung:** Khi được cấu hình, bảo vệ nhánh và CI có thể yêu cầu kiểm tra đạt trước khi hợp nhất, đồng thời hạn chế những thao tác không được phép.

Những lợi ích này phụ thuộc vào cách thực hiện. PR không tự bảo đảm mã đúng, lịch sử dễ đọc hay khả năng hoàn tác toàn bộ thay đổi bằng một lệnh. Kết quả còn phụ thuộc vào chất lượng commit, cách hợp nhất và các phụ thuộc giữa những thay đổi.

Commit trực tiếp lên nhánh chính vẫn có thể phù hợp với dự án nhỏ hoặc quy trình cho phép tích hợp trực tiếp bằng các thay đổi nhỏ đã được kiểm tra. Số lượng người phát triển không phải tiêu chí duy nhất; cần cân nhắc yêu cầu ổn định, truy vết, phát hành và mức độ kiểm soát của dự án.

Kết luận:` Nhánh và PR giúp tạo điểm kiểm tra, cô lập công việc và lưu lại bối cảnh thay đổi, kể cả khi làm một mình. Có bắt buộc dùng hay không phụ thuộc vào quy trình và yêu cầu của dự án.
