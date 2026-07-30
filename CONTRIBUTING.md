# 🤝 Hướng Dẫn Đóng Góp Cho CryOS (Contribution Guidelines)

Cảm ơn bạn đã quan tâm và muốn đóng góp phát triển cho **CryOS v1.0.0 Polaris**! 

CryOS là một dự án phân phối Linux nguồn mở độc đáo, được xây dựng dựa trên sự kết hợp giữa **Kali Linux Rolling** và **Polaris Desktop Shell (PyQt6/QML)**.

---

## 🛠️ Quy Trình Đóng Góp Mã Nguồn (Pull Request Workflow)

1. **Fork Repository:** Nhấn nút `Fork` ở góc phải trên cùng của GitHub Repo này.
2. **Clone Fork về máy:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/CryOS.git
   cd CryOS
   ```
3. **Tạo nhánh mới (Feature Branch):**
   ```bash
   git checkout -b feature/giao-dien-moi
   ```
4. **Thực hiện thay đổi & Kiểm thử (Test):**
   - Chạy `python run_qml.py` để test giao diện QML / PyQt.
   - Chạy `python test_qemu.py` để test file ISO nếu có thay đổi trong `kali-config`.
5. **Commit & Push:**
   ```bash
   git commit -m "feat: Thêm widget phát nhạc cho TopBar"
   git push origin feature/giao-dien-moi
   ```
6. **Tạo Pull Request (PR):** Mở PR trên GitHub giải thích chi tiết các thay đổi của bạn.

---

## 🎨 Các Khu Vực Bạn Có Thể Đóng Góp

### 1. Giao diện Polaris Desktop Shell (`qml/` & `cryos/`)
- Cải thiện CSS, bo góc, hiệu ứng kính mờ (Blur) trong `qml/main.qml` hoặc `cryos/styles.py`.
- Thiết kế thêm widget: Đồng hồ, Dự báo thời tiết, Trình điều khiển Spotify/MP3, System Monitor.

### 2. Dịch vụ Hệ thống Python Backend (`cryos/service.py`)
- Viết thêm hàm API kết nối Wi-Fi (`NetworkManager`), Bluetooth (`bluez`), chỉnh độ sáng màn hình.

### 3. Cấu hình Đóng gói ISO (`kali-config/`)
- Tùy chỉnh danh sách gói phần mềm trong [cryos-polaris.list.chroot](kali-live-build/kali-config/variant-cryos/package-lists/cryos-polaris.list.chroot).
- Thêm bộ dotfiles cá nhân đẹp mắt vào `kali-config/variant-cryos/includes.chroot/etc/skel/`.

---

## 💬 Quy Tắc Ứng Xử (Code of Conduct)
- Tôn trọng các thành viên và đóng góp ý kiến mang tính xây dựng.
- Giữ cho mã nguồn sạch sẽ, dễ đọc và có chú thích (Comment) rõ ràng.

Rất mong nhận được những Pull Requests chất lượng từ bạn! 🚀
