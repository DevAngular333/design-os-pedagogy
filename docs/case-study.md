# Case study: kiểm chứng một vòng Agent Teacher

## Người dùng và vấn đề

Giáo viên hoặc người thiết kế tutor cần luyện cách hỏi, diễn giải và kiểm tra
chuyển giao trước khi đưa một bài dạy vào thực tế. Một bản tóm tắt lý thuyết
không cho thấy các quyết định có được lưu, xem lại và xuất ra hay không.

## Đóng góp của fork DevAngular333

Fork này giữ runtime local-first và dữ liệu mô phỏng có ghi nhãn từ upstream,
đồng thời thêm một đường kiểm chứng không phụ thuộc framework: `scripts/smoke_flow.py`.
Script khởi động server thật trên loopback, tạo phiên, đi qua đủ bảy chuyển tiếp,
kiểm tra replay khớp snapshot và đọc bản xuất Markdown. Dữ liệu phiên được tạo
trong thư mục tạm, không đi vào Git.

## Cách chạy

```bash
python3 scripts/smoke_flow.py
```

Kết quả thành công có dạng:

```json
{"status":"PASS","mode":"authored_rehearsal","case":"fraction-magnitude","revision":7,"replay_matches":true,"export":"markdown"}
```

Để xem giao diện bằng tay:

```bash
python3 run_rehearsal.py --port 0 --data-dir /tmp/agent-teacher-data
```

Mở URL `http://127.0.0.1:<port>` mà lệnh in ra. Dừng server bằng `Ctrl-C`.

## Quyết định kỹ thuật

- **Không gọi model ngoài:** các nhánh học sinh, coaching và transfer được ghi
  rõ là authored simulation; việc này làm demo tái hiện được và giữ dữ liệu local.
- **Kiểm tra qua HTTP thật:** smoke runner không gọi hàm nội bộ, nên bắt được
  lỗi khởi động, route, trạng thái revision và export.
- **CSDL tạm:** đầu ra chứng minh persistence/replay mà không đưa database cá
  nhân hoặc trạng thái runtime vào repo công khai.

## Giới hạn đã kiểm chứng

Runner chứng minh luồng kỹ thuật của một tình huống và cơ chế lưu/replay/export.
Nó không chứng minh chất lượng sư phạm, semantic grading, hiệu quả học tập,
expert review, pilot người dùng hoặc chứng nhận năng lực giảng dạy. Xem
[`docs/rehearsal-contract.md`](rehearsal-contract.md) để biết boundary đầy đủ.

## Nguồn

- Upstream: [`jangtrinh/design-os-pedagogy`](https://github.com/jangtrinh/design-os-pedagogy)
- Fork: [`DevAngular333/design-os-pedagogy`](https://github.com/DevAngular333/design-os-pedagogy)
- License: PolyForm Shield 1.0.0; xem [`NOTICE.md`](../NOTICE.md) và [`LICENSE`](../LICENSE)
