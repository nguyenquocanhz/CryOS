from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt
from cryos.styles import POLARIS_STYLES

class CryDock(QWidget):
    def __init__(self, parent=None, open_spotlight_cb=None, open_hub_cb=None, open_finder_cb=None, open_term_cb=None):
        super().__init__(parent)
        self.open_spotlight_cb = open_spotlight_cb
        self.open_hub_cb = open_hub_cb
        self.open_finder_cb = open_finder_cb
        self.open_term_cb = open_term_cb
        
        self.setStyleSheet(POLARIS_STYLES)
        self.setFixedHeight(75)
        
        self.init_ui()
        
    def init_ui(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        container = QFrame()
        container.setObjectName("DockPill")
        
        dock_layout = QHBoxLayout(container)
        dock_layout.setContentsMargins(14, 6, 14, 6)
        dock_layout.setSpacing(10)
        
        # Exact icons from user picture
        dock_items = [
            ("🔷", "Finder", self.open_finder_cb, False),
            ("🎛", "Launchpad", self.open_spotlight_cb, False),
            ("💎", "CryOS", self.open_hub_cb, True), # Active dot under CryOS!
            ("✉️", "Mail", None, False),
            ("📅", "Calendar", None, False),
            ("📝", "Notes", None, False),
            ("🖼", "Photos", None, False),
            ("💻", "Terminal", self.open_term_cb, True),
            ("⚙️", "Settings", None, False),
            ("🗑", "Trash", None, False),
        ]
        
        for icon, name, cb, is_active in dock_items:
            item_box = QVBoxLayout()
            item_box.setSpacing(2)
            item_box.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            btn = QPushButton(icon)
            btn.setObjectName("DockItem")
            btn.setFixedSize(48, 48)
            btn.setStyleSheet("font-size: 26px;")
            btn.setToolTip(name)
            if cb:
                btn.clicked.connect(cb)
            item_box.addWidget(btn)
            
            # Active Indicator Dot
            dot = QLabel("•" if is_active else " ")
            dot.setAlignment(Qt.AlignmentFlag.AlignCenter)
            dot.setStyleSheet("color: #FFFFFF; font-size: 14px; font-weight: bold; margin-top: -6px;")
            item_box.addWidget(dot)
            
            dock_layout.addLayout(item_box)
            
        main_layout.addWidget(container)
