from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QTabWidget, 
    QLabel, QPushButton, QFrame, QGridLayout, QScrollArea
)
from PyQt6.QtCore import Qt
from cryos.styles import CRYHUB_STYLE

class CryHub(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("CryHub - Security & Developer Suite Center")
        self.resize(900, 600)
        
        main_widget = QWidget()
        main_widget.setObjectName("CryHubWindow")
        main_widget.setStyleSheet(CRYHUB_STYLE)
        self.setCentralWidget(main_widget)
        
        layout = QVBoxLayout(main_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Header
        title = QLabel("🛍 CryHub - Trung Tâm Phần Mềm & Công Cụ CryOS")
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: #38BDF8;")
        subtitle = QLabel("Quản lý & Cài đặt 1-Click các bộ công cụ Kali Security Linux và Môi trường Lập Trình")
        subtitle.setStyleSheet("font-size: 13px; color: #94A3B8; margin-bottom: 10px;")
        
        layout.addWidget(title)
        layout.addWidget(subtitle)
        
        # Tabs
        tabs = QTabWidget()
        tabs.addTab(self.create_kali_tab(), "🛡 Kali Security Suite")
        tabs.addTab(self.create_dev_tab(), "💻 Developer Ecosystem")
        tabs.addTab(self.create_system_tab(), "⚙️ System & Utilities")
        
        layout.addWidget(tabs)
        
    def create_kali_tab(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        grid = QGridLayout(content)
        grid.setSpacing(16)
        
        tools = [
            ("🛡 Nmap Network Scanner", "Information Gathering", "Quét lỗ hổng, phát hiện cổng mở và dịch vụ trên mạng", True),
            ("🦈 Wireshark", "Sniffing & Spoofing", "Bắt và phân tích chi tiết các gói tin mạng theo thời gian thực", True),
            ("🎯 Metasploit Framework", "Exploitation Tools", "Khung thử nghiệm khai thác lỗ hổng bảo mật tiêu chuẩn", True),
            ("🕷 Burp Suite Community", "Web Application Analysis", "Công cụ kiểm thử bảo mật ứng dụng Web phổ biến nhất", False),
            ("🔓 Aircrack-ng", "Wireless Attacks", "Bộ công cụ đánh giá an toàn mạng không dây Wi-Fi", True),
            ("🔍 John the Ripper", "Password Attacks", "Công cụ bẻ khóa mật khẩu và kiểm tra độ mạnh mật khẩu", True),
            ("🧬 Ghidra", "Reverse Engineering", "Bộ công cụ dịch ngược (Reverse Engineering) mã nguồn từ NSA", False),
            ("🕵️ Autopsy", "Digital Forensics", "Nền tảng điều tra số và phân tích chứng cứ kĩ thuật số", False),
        ]
        
        for idx, (name, cat, desc, installed) in enumerate(tools):
            card = self.create_tool_card(name, cat, desc, installed)
            grid.addWidget(card, idx // 2, idx % 2)
            
        scroll.setWidget(content)
        return scroll
        
    def create_dev_tab(self):
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        grid = QGridLayout(content)
        grid.setSpacing(16)
        
        tools = [
            ("📝 Visual Studio Code", "IDE & Editor", "Trình soạn thảo mã nguồn phổ biến hàng đầu cho Dev", True),
            ("🐳 Docker & Docker Compose", "Containers", "Nền tảng đóng gói và chạy ứng dụng trong Container", True),
            ("🐍 Python 3.11 Environment", "Programming Language", "Môi trường lập trình Python sẵn sàng cho Data/Dev/Hacking", True),
            ("⚡ Node.js & npm", "JavaScript Runtime", "Môi trường chạy JavaScript cho Web Dev & Tooling", True),
            ("🦀 Rust Toolchain (cargo)", "System Programming", "Ngôn ngữ lập trình hệ thống nhanh và an toàn bộ nhớ", False),
            ("📮 Postman API Platform", "API Development", "Nền tảng kiểm thử và xây dựng RESTful APIs", False),
        ]
        
        for idx, (name, cat, desc, installed) in enumerate(tools):
            card = self.create_tool_card(name, cat, desc, installed)
            grid.addWidget(card, idx // 2, idx % 2)
            
        scroll.setWidget(content)
        return scroll
        
    def create_system_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        info = QLabel("⚙️ Cấu hình CryOS Linux Core & Kali Repositories\n\n- Repositories Status: Connected to Kali Rolling & Debian Stable\n- Core Kernel: Linux 6.x\n- Shell Theme: macOS Glassmorphism Dark Mode")
        info.setStyleSheet("color: #CBD5E1; font-size: 14px; line-height: 1.6;")
        layout.addWidget(info)
        layout.addStretch()
        return widget
        
    def create_tool_card(self, name, category, desc, installed):
        card = QFrame()
        card.setObjectName("ToolCard")
        
        layout = QVBoxLayout(card)
        
        name_lbl = QLabel(name)
        name_lbl.setStyleSheet("font-size: 15px; font-weight: bold; color: #F8FAFC;")
        
        cat_lbl = QLabel(category)
        cat_lbl.setStyleSheet("font-size: 11px; color: #38BDF8; font-weight: 500;")
        
        desc_lbl = QLabel(desc)
        desc_lbl.setWordWrap(True)
        desc_lbl.setStyleSheet("font-size: 12px; color: #94A3B8; margin-top: 4px;")
        
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        
        if installed:
            status_btn = QPushButton("▶ Chạy Ngay")
            status_btn.setObjectName("LaunchButton")
        else:
            status_btn = QPushButton("📥 Cài Đặt 1-Click")
            status_btn.setObjectName("InstallButton")
            
        btn_layout.addWidget(status_btn)
        
        layout.addWidget(name_lbl)
        layout.addWidget(cat_lbl)
        layout.addWidget(desc_lbl)
        layout.addLayout(btn_layout)
        
        return card
