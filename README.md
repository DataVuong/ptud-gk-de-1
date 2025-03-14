# ptud-gk-de-1
# PTUD-GK-DE-1: Blog Cá Nhân với Flask

## 1️⃣ Thông tin cá nhân
- **Họ tên**: Nguyễn Trường Vương
- **MSSV**: 22642961
- **Lớp**: DHKHDL18A
- **Trường**: Đại học Công Nghiệp TP.HCM

---

## 2️⃣ Mô tả project
Đây là một ứng dụng **Blog cá nhân** được xây dựng bằng **Flask**, hỗ trợ hai loại người dùng:
- **Admin**: Quản lý user, xóa bình luận, theo dõi bài viết, bình luận.
- **User**: Đăng ký, đăng nhập, bình luận bài viết, theo dõi bài viết.

**Chức năng chính của Blog:**
✅ Đăng ký, đăng nhập, đăng xuất  
✅ Phân quyền **Admin & User**  
✅ Quản lý bài viết, hiển thị ảnh từ `picsum.photos`  
✅ Bình luận bài viết, admin có quyền xóa bình luận  
✅ Theo dõi bài viết (lượt follow tăng khi người dùng click)  
✅ Giao diện đẹp với **Bootstrap 5**  
✅ Có thể xem chi tiết của bài viết
✅ có 1 tài khoản mặc định: 
       admin	admin123	Admin

---

## 3️⃣ Hướng dẫn cài đặt và chạy project

### **📌 Yêu cầu hệ thống**
- Python >= 3.8
- Pip (Python package manager)
- Flask, Flask-Login, Flask-WTF, Werkzeug

### **💻 Cài đặt và chạy ứng dụng**
1. **Clone project từ GitHub**
   mở cmd: di chuyển tới thư mục bạn muốn lưu project sau đó ghi dòng code dưới đây: 
    git clone https://github.com/DataVuong/ptud-gk-de-1.git

   sau đó sẽ xuất hiện thư mục bạn clone, vào thư mục đó,
   sau đó vào phần app.py để chạy project
   Xem thông báo trong terminal: Sẽ thấy một dòng tương tự như:
   Running on http://127.0.0.1:5000/ => Copy dòng địa chỉ và truy cập địa chỉ này
