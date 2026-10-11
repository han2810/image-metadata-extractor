# image-metadata-extractor

Trang web xem, sửa và xóa metadata của ảnh JPEG.

## Giới thiệu

Ảnh JPEG chứa nhiều dữ liệu ẩn: loại máy ảnh, thời gian chụp, phần mềm đã dùng, đôi khi cả vị trí GPS. Trang web này giúp xem những dữ liệu đó, chỉnh sửa hoặc xóa trước khi chia sẻ ảnh.

## Tính năng

- **Trích xuất:** đọc và hiển thị metadata của ảnh JPEG
- **Chỉnh sửa:** sửa các trường metadata
- **Xóa:** xóa một trường hoặc toàn bộ metadata

## Công nghệ

- Frontend: ReactJS
- Backend: Flask (Python)

## Chạy thử

Chạy trên máy (cần cài sẵn Python và Node.js):

```bash
git clone https://github.com/han2810/image-metadata-extractor.git
cd image-metadata-extractor
```

**Backend:**

```bash
cd backend
pip install -r requirements.txt
python app.py
```

**Frontend** (mở terminal khác):

```bash
cd frontend
npm install
npm run dev
```

Sau đó mở địa chỉ http://localhost:5173 trên trình duyệt.

## Cách dùng

1. Tải ảnh JPEG lên.
2. Xem metadata hiển thị.
3. Sửa hoặc xóa trường muốn đổi.
4. Tải ảnh đã xử lý về.

## Lưu ý

- Chỉ hỗ trợ JPEG (`.jpg`, `.jpeg`).
