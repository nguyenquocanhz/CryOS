from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QGridLayout, QWidget, QPushButton
)
from PyQt6.QtCore import Qt
from cryos.styles import POLARIS_STYLES

class CryFinder(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("FinderWindow")
        self.setStyleSheet(POLARIS_STYLES)
        self.resize(650, 420)
        
        self.init_ui()
        
    def init_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # 1. Left Sidebar
        sidebar = QFrame()
        sidebar.setObjectName("Sidebar")
        sidebar.setFixedWidth(180)
        sb_layout = QVBoxLayout(sidebar)
        sb_layout.setContentsMargins(10, 14, 10, 14)
        sb_layout.setSpacing(2)
        
        # Traffic Lights
        tf_layout = QHBoxLayout()
        tf_layout.setContentsMargins(4, 0, 0, 10)
        tf_layout.setSpacing(6)
        
        btn_close = QPushButton()
        btn_close.setObjectName("BtnClose")
        btn_close.setFixedSize(12, 12)
        
        btn_min = QPushButton()
        btn_min.setObjectName("BtnMin")
        btn_min.setFixedSize(12, 12)
        
        btn_max = QPushButton()
        btn_max.setObjectName("BtnMax")
        btn_max.setFixedSize(12, 12)
        
        tf_layout.addWidget(btn_close)
        tf_layout.addWidget(btn_min)
        tf_layout.addWidget(btn_max)
        tf_layout.addStretch()
        sb_layout.addLayout(tf_layout)
        
        # Favorites
        fav_header = QLabel("Favorites")
        fav_header.setObjectName("SidebarHeader")
        sb_layout.addWidget(fav_header)
        
        favorites = [
            ("🏠", "Home", True),
            ("🖥", "Desktop", False),
            ("📄", "Documents", False),
            ("📥", "Downloads", False),
            ("🖼", "Pictures", False),
            ("🎵", "Music", False),
            ("🎬", "Movies", False),
        ]
        for icon, name, active in favorites:
            item = QLabel(f"{icon}  {name}")
            item.setObjectName("SidebarItemActive" if active else "SidebarItem")
            sb_layout.addWidget(item)
            
        # Locations
        loc_header = QLabel("Locations")
        loc_header.setObjectName("SidebarHeader")
        sb_layout.addWidget(loc_header)
        
        locations = [
            ("💻", "CryOS Drive"),
            ("💾", "Storage"),
            ("🌐", "Network"),
        ]
        for icon, name in locations:
            item = QLabel(f"{icon}  {name}")
            item.setObjectName("SidebarItem")
            sb_layout.addWidget(item)
            
        # Tags
        tags_header = QLabel("Tags")
        tags_header.setObjectName("SidebarHeader")
        sb_layout.addWidget(tags_header)
        
        tags = [
            ("🔴", "Work"),
            ("🟠", "Personal"),
            ("🟡", "Important"),
            ("🟣", "Design"),
            ("🔵", "Study"),
        ]
        for icon, name in tags:
            item = QLabel(f"{icon} {name}")
            item.setObjectName("SidebarItem")
            sb_layout.addWidget(item)
            
        sb_layout.addStretch()
        main_layout.addWidget(sidebar)
        
        # 2. Right Main View
        right_panel = QWidget()
        rp_layout = QVBoxLayout(right_panel)
        rp_layout.setContentsMargins(16, 14, 16, 16)
        
        # Header bar
        header_bar = QHBoxLayout()
        back_btn = QLabel("<  Home")
        back_btn.setStyleSheet("font-weight: 700; font-size: 14px; color: #F8FAFC;")
        header_bar.addWidget(back_btn)
        header_bar.addStretch()
        
        view_mode = QLabel("🎛  ☰  🔍")
        view_mode.setStyleSheet("color: #94A3B8; font-size: 13px; padding-right: 6px;")
        header_bar.addWidget(view_mode)
        rp_layout.addLayout(header_bar)
        
        # Grid of Folders
        grid_widget = QWidget()
        grid = QGridLayout(grid_widget)
        grid.setSpacing(14)
        
        folders = [
            ("Desktop", "12 items"),
            ("Documents", "84 items"),
            ("Downloads", "36 items"),
            ("Pictures", "215 items"),
            ("Music", "47 items"),
            ("Movies", "18 items"),
            ("Projects", "9 items"),
            ("Public", "3 items"),
        ]
        
        for idx, (name, count) in enumerate(folders):
            card = QFrame()
            card.setObjectName("FolderCard")
            c_layout = QVBoxLayout(card)
            c_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            c_layout.setSpacing(4)
            
            f_icon = QLabel("📁")
            f_icon.setStyleSheet("font-size: 38px; color: #38BDF8;")
            c_layout.addWidget(f_icon, alignment=Qt.AlignmentFlag.AlignCenter)
            
            f_name = QLabel(name)
            f_name.setStyleSheet("font-weight: 600; font-size: 12px; color: #F8FAFC;")
            c_layout.addWidget(f_name, alignment=Qt.AlignmentFlag.AlignCenter)
            
            f_count = QLabel(count)
            f_count.setStyleSheet("font-size: 10px; color: #64748B;")
            c_layout.addWidget(f_count, alignment=Qt.AlignmentFlag.AlignCenter)
            
            grid.addWidget(card, idx // 4, idx % 4)
            
        rp_layout.addWidget(grid_widget)
        rp_layout.addStretch()
        
        main_layout.addWidget(right_panel)
