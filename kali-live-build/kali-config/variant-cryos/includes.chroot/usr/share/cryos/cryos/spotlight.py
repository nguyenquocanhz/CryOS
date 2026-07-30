from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QListWidget, QListWidgetItem, QLabel
from PyQt6.QtCore import Qt
from cryos.styles import SPOTLIGHT_STYLE

class CrySpotlight(QDialog):
    def __init__(self, parent=None, open_hub_cb=None):
        super().__init__(parent)
        self.open_hub_cb = open_hub_cb
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Popup)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(600, 360)
        self.setStyleSheet(SPOTLIGHT_STYLE)
        
        self.items_db = [
            ("🛡 Nmap Network Scanner", "Kali Security Tool - Quét cổng & dịch vụ mạng"),
            ("🦈 Wireshark Traffic Analyzer", "Kali Security Tool - Phân tích gói tin mạng"),
            ("🎯 Metasploit Framework", "Kali Security Tool - Exploitation & Security Auditing"),
            ("🕷 Burp Suite", "Kali Security Tool - Kiểm thử bảo mật Web App"),
            ("📝 Visual Studio Code", "Dev Tool - Trình soạn thảo mã nguồn"),
            ("🐳 Docker Desktop", "Dev Tool - Quản lý container ứng dụng"),
            ("🛍 CryHub Tool Center", "System - Trung tâm phần mềm & cài đặt công cụ Kali 1-Click"),
            ("⚙️ CryOS System Settings", "System - Cấu hình hệ thống & Giao diện macOS"),
            ("📂 Finder / File Manager", "System - Trình quản lý tệp tin"),
            ("💻 Terminal", "System - Trình điều khiển dòng lệnh Linux"),
        ]
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)
        
        header = QLabel("🔍 CrySearch")
        header.setStyleSheet("color: #38BDF8; font-weight: bold; font-size: 14px;")
        layout.addWidget(header)
        
        self.search_input = QLineEdit()
        self.search_input.setObjectName("SearchInput")
        self.search_input.setPlaceholderText("Gõ để tìm kiếm App, lệnh Kali Security, hoặc công cụ Dev...")
        self.search_input.textChanged.connect(self.filter_items)
        layout.addWidget(self.search_input)
        
        self.result_list = QListWidget()
        self.result_list.setObjectName("ResultList")
        self.result_list.itemDoubleClicked.connect(self.on_item_click)
        layout.addWidget(self.result_list)
        
        self.populate_list(self.items_db)
        
    def populate_list(self, items):
        self.result_list.clear()
        for title, desc in items:
            item = QListWidgetItem(f"{title}\n   ↳ {desc}")
            item.setData(Qt.ItemDataRole.UserRole, title)
            self.result_list.addItem(item)
            
    def filter_items(self, text):
        query = text.lower().strip()
        if not query:
            self.populate_list(self.items_db)
            return
            
        filtered = [
            (t, d) for t, d in self.items_db 
            if query in t.lower() or query in d.lower()
        ]
        self.populate_list(filtered)

    def on_item_click(self, item):
        title = item.data(Qt.ItemDataRole.UserRole)
        if "CryHub" in title and self.open_hub_cb:
            self.open_hub_cb()
        self.close()
