# Introduction 🤖
- Đây Là Một Dự Án Nhỏ Đầu Tay Của Mình Nhằm Mục Đích Quản Lý Máy Tính Từ Xa, Khi Người Dùng Máy Không Muốn Sử Dụng Phần Mềm Thứ 3 Để Can Thiệp Hoặc Vân Vân Và Mây Mây ~.~
- Đồng Thời Đây Cũng Là 1 Dự Án Mình Làm Mang Tính Chất Cá Nhân. Cho Nên Mọi Đóng Góp, Ý Kiến Về Sửa Lỗi Cũng Như Thêm Tính Năng Các Bạn Có Thể Liên Hệ Qua:<br>
    > Telegram : @DucThinhEXE<br>
    > Facebook : Facebook.com/61556351104541<br>
    > Youtube : @JiraySoftware<br>

## Installation
1. **Tải Và Cài Đặt Môi Trường**
   - Tải Và Cài Đặt [Python 3.11](https://www.python.org/downloads/release/python-3110/)
   - Thực Hiện Setup Python Trên Máy ( Nhớ Tích Vào Ô Add To Path Nhé )
2. **Tải Xuống Source Code Phần Mềm**
   - Thực Hiện Tải Source Code Về Hoặc Mở Command Prompt Nhập Dòng Lệnh
        ```
        git clone https://github.com/DucThinhEXE/Control-Device-In-Telegram.git
        ```

3. **Install Các Thư Viện Cần Thiết**
   - Vào Folder Chứa Code, Mở CMD Tại Thanh Địa Chỉ. Tại Bảng Console, Nhập Lệnh
        ```
        pip install -r requirements.txt
        ```
4. **Lấy Dữ Liệu Cần Thiết**
- Vào Telegram , Search Từ Khóa @BotFather 
- Nhập lệnh __/newbot__ Và Tự Khởi Tạo Con Bot Cho Mình Theo Các Bước Có Sẵn
- Sau Khi Tạo Xong Sẽ Có Một Tin Nhắn Trả Về Như Ảnh

    ![Login](https://i.imgur.com/MGMCk9D.jpg)
- Api Token Chính Là Phần Bôi Đỏ, Còn Chat ID Thì Anh Em Lên [Web Telegram](web.telegram.com) Đăng Nhập, Tạo Nhóm ( Nhớ Thêm Bot Vào Nhé )
- Sau Khi Tạo Nhóm Xong, chatID Sẽ Hiện Ở Trên URL, Các Bạn Nhớ Lưu Vào Nhé ( Nhớ Là Có Cả Dấu '-'' )
    
# How To Use
- Vào Folder Chứa Tool -> Config -> ApiKey.py
- Tại Đây Các Bạn Mở File Lên, Cấu Hình Api Key Bot Telegram Và Chat ID Của Các Bạn Vào Nhé
- Sau Khi Cấu Hình Xong, Các Bạn Quay Lại Folder Chứa Tool, Mở CMD. Tại Đây Các Bạn Thực Hiện Nhập Lệnh Sau :

    ```
    pyinstaller --onefile --noconsole main.py
    ```
- Đợi Sau Khi Chạy Xong Chương Trình, Các Bạn Mở Folder __dist__ -> Nhận File .EXE ( Là Phần Mềm Các Bạn Khởi Tạo Vừa Xong ). Sau Đó Mở Thư Mục __Startup__ bằng Cách Gõ Window + R Rồi Nhập __shell:startup__
- Các Bạn Kéo Thả File .EXE ban nãy vào là xong nhé. Muốn Test Thử Thì Chạy File Đó Lên, Vào Trong Nhóm Telegram Ban Nãy Nhập __/help__. Nếu Nó Phản Hồi Là Thành Công Rồi Nha
# Important Note !!!
- Đây Là Phần Mềm Được Tạo Ra Nhằm Để Học Hỏi, Không Nhằm Mục Đích Xấu. Tuyệt Đối Không Sử Dụng Sản Phẩm Vào Các Mục Đích Vi Phạm Pháp Luật. Nếu Có Tôi Hoàn Toàn Không Chịu Trách Nhiệm !
# Donate
- Cảm Ơn Các Bạn Đã Sử Dụng Sản Phẩm Của Mình. Các Bạn Có Thể Donate Cho Mình Qua Các Ví Sau Tạo Động Lực Giúp Mình Chia Sẻ Các Phần Mềm Hữu Ích Hơn. Xin Cảm Ơn Các Bạn Rất Nhiều :3
```MBBANK : 8386282006 - NGUYEN DUC THINH```
- Mọi Thắc Mắc Hoặc Câu Hỏi Đáp Có Thể Liên Hệ Qua Telegram : @DucThinhEXE. Chúc Các Bạn Sử Dụng Phần Mềm An Toàn Và Có Một Ngày Mới Tốt Lành <333



