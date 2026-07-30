<div align="center">

```text
       /\            /\       
      /  \          /  \      
     /    \  ____  /    \     
    /  /\  \/    \/  /\  \    
   /  /  \          /  \  \   
  (  (    \        /    )  )  
   \  \    \  /\  /    /  /   
    \__\    \/  \/    /__/    
```

# 💎 CryOS v1.0.0 Polaris

**Next-Generation Linux Distribution with macOS/Glassmorphic Desktop Shell & Kali Security Suite**

[![Linux](https://img.shields.io/badge/Linux-Kernel_6.6_LTS-blue.svg?logo=linux&logoColor=white)](https://kernel.org)
[![Kali Linux Base](https://img.shields.io/badge/Base-Kali_Rolling-557C93.svg?logo=kali-linux&logoColor=white)](https://kali.org)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB.svg?logo=python&logoColor=white)](https://python.org)
[![Qt Framework](https://img.shields.io/badge/UI-PyQt6_%7C_QML-41CD52.svg?logo=qt&logoColor=white)](https://qt.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ISO Build](https://img.shields.io/badge/ISO_Status-PASSED-success.svg)](#-iso-build-system)

[Trải nghiệm](#-tính-năng-nổi-bật) • [Cài đặt](#-hướng-dẫn-cài-đặt) • [Test ISO](#-thử-nhiệm-iso) • [Đóng góp (Contribute)](#-hướng-dẫn-đóng-góp-contribute)

---

</div>

## 🌟 Giới Thiệu (Overview)

**CryOS v1.0.0 Polaris** là bản phân phối Linux thế hệ mới kết hợp giữa **sức mạnh bảo mật của Kali Linux Rolling** và **giao diện Desktop Shell sang trọng (Polaris UI)** được xây dựng bằng Python & QML theo phong cách Glassmorphism (Kính mờ).

CryOS được thiết kế hướng tới sự cân bằng hoàn hảo:
1. **Lập trình viên & Designer:** Giao diện đẹp mắt, thanh Dock nổi, Spotlight Search (`Ctrl + Space`), hỗ trợ Docker, Python, VS Code.
2. **Chuyên gia Bảo mật & Pentester:** Trang bị sẵn bộ công cụ Security hàng đầu (Nmap, Wireshark, Metasploit, Burp Suite, Aircrack-ng).
3. **Người dùng phổ thông:** Cài đặt 1-Click đồ họa Quick Installer, lướt web Chromium 4K, hỗ trợ đầy đủ Wi-Fi, Bluetooth, GPU acceleration.

---

## ✨ Tính Năng Nổi Bật (Key Features)

- 🍎 **Polaris Desktop Shell (PyQt6/QML):**
  - **CryTopBar:** Thanh trạng thái phía trên hiển thị giờ, chỉ số hệ thống & Control Center.
  - **CryDock:** Thanh Dock ứng dụng nổi mượt mà phía dưới màn hình.
  - **CrySpotlight:** Trình tìm kiếm & khởi chạy nhanh toàn hệ thống (`Ctrl + Space`).
  - **CryFinder:** Trình quản lý tệp tin đồ họa phong cách Finder.
  - **CryTerminal:** Terminal tích hợp hiển thị Fastfetch hệ thống.
  - **CryControlCenter:** Trung tâm cài đặt nhanh Wi-Fi, Bluetooth, Âm lượng, Dark Mode.
- ⚡ **Kernel 6.6 LTS & EEVDF Scheduler:** Bộ lập lịch CPU mới giúp chơi game và đa nhiệm mượt 60 FPS không bị khựng đĩa.
- 📀 **Hybrid Boot ISO (UEFI & Legacy):** Boot mượt mà trên 100% các dòng laptop/PC từ 2008 đến 2026.
- 🐳 **Đã nạp sẵn Docker & Python 3.13:** Sẵn sàng cho mọi công việc ảo hóa và lập trình.

---

## 💻 Xem Trước Giao Diện (Preview UI)

Bạn có thể chạy thử trực tiếp giao diện Polaris Desktop Shell ngay trên Windows/Linux bằng Python mà không cần cài đặt:

```bash
# Clone repo
git clone https://github.com/your-username/CryOS.git
cd CryOS

# Cài phụ thuộc PyQt6
pip install -r requirements.txt

# Khởi chạy giao diện CryOS Polaris
python run_qml.py
```

---

## 🛠️ Biên Dịch File ISO (Build ISO)

Để tự đóng gói ra file bootable **`CryOS.iso`** trên môi trường WSL2/Linux:

```bash
# Cấp quyền và thực thi script build
dos2unix build_cryos_iso.sh
bash ./build_cryos_iso.sh
```

> File ISO kết quả sẽ nằm tại thư mục `output/kali-linux-rolling-live-cryos-amd64.iso`.

---

## 🚀 Thử Nghiệm ISO (Test ISO)

### 1. Test Bằng QEMU (Mở ngay trên máy)
```bash
python test_qemu.py
```

### 2. Ghi ra USB boot thử trên máy thật
Sử dụng **Rufus** hoặc **Ventoy** ghi file `output/kali-linux-rolling-live-cryos-amd64.iso` với chuẩn **GPT / UEFI**.

---

## 🤝 Hướng Dẫn Đóng Góp (Contribute)

Chúng mình rất hoan nghênh và trân trọng mọi đóng góp từ cộng đồng Open-Source & Ricers!

### Bạn có thể đóng góp gì cho CryOS?
- 🎨 **Thiết kế QML / UI Widgets:** Tạo thêm widget thời tiết, nhạc player, theme màu sắc mới cho Polaris Shell.
- 🐍 **Phát triển Python Backend Daemon:** Viết thêm tính năng quản lý mạng, cài đặt hệ thống trong `cryos/service.py`.
- 📦 **Tối ưu gói ISO (`cryos-polaris.list.chroot`):** Thêm/bớt ứng dụng để tạo bản *CryOS Lite* hoặc *CryOS Gaming Edition*.
- 🐛 **Báo lỗi & Đóng góp ý tưởng:** Mở [Issues](../../issues) hoặc [Pull Requests](../../pulls).

Vui lòng đọc chi tiết tại [CONTRIBUTING.md](CONTRIBUTING.md) trước khi gửi PR!

---

## 📜 Giấy Phép (License)

Dự án CryOS được phát hành theo giấy phép [MIT License](LICENSE). 

---

<div align="center">
  <b>Made with ❤️ by CryOS Community & Open-Source Contributors</b>
</div>
