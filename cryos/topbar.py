import datetime
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import QTimer, Qt
from cryos.styles import POLARIS_STYLES

class CryTopBar(QWidget):
    def __init__(self, parent=None, toggle_control_center_cb=None, open_spotlight_cb=None):
        super().__init__(parent)
        self.setObjectName("TopBar")
        self.setStyleSheet(POLARIS_STYLES)
        self.setFixedHeight(32)
        
        self.toggle_control_center_cb = toggle_control_center_cb
        self.open_spotlight_cb = open_spotlight_cb
        
        self.init_ui()
        
    def init_ui(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 0, 12, 0)
        layout.setSpacing(6)
        
        # Left Brand & Menus
        brand = QLabel("💎 CryOS")
        brand.setObjectName("TopBarBrand")
        layout.addWidget(brand)
        
        menus = ["File", "Edit", "View", "Go", "Window", "Help"]
        for m in menus:
            lbl = QLabel(m)
            lbl.setObjectName("TopBarMenu")
            layout.addWidget(lbl)
            
        layout.addStretch()
        
        # Right Icons & Controls
        # Display icon
        disp_icon = QLabel("🖥")
        disp_icon.setStyleSheet("padding: 0 4px; font-size: 13px;")
        layout.addWidget(disp_icon)
        
        # Sound icon
        sound_icon = QLabel("🔊")
        sound_icon.setStyleSheet("padding: 0 4px; font-size: 13px;")
        layout.addWidget(sound_icon)

        # Battery icon
        bat_icon = QLabel("🔋")
        bat_icon.setStyleSheet("padding: 0 4px; font-size: 13px;")
        layout.addWidget(bat_icon)

        # Control Center Icon Switch
        cc_btn = QPushButton("🎛")
        cc_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                font-size: 14px;
                padding: 0 4px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.15);
                border-radius: 4px;
            }
        """)
        if self.toggle_control_center_cb:
            cc_btn.clicked.connect(self.toggle_control_center_cb)
        layout.addWidget(cc_btn)

        # Search / Spotlight Icon
        search_btn = QPushButton("🔍")
        search_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                border: none;
                font-size: 13px;
                padding: 0 4px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.15);
                border-radius: 4px;
            }
        """)
        if self.open_spotlight_cb:
            search_btn.clicked.connect(self.open_spotlight_cb)
        layout.addWidget(search_btn)
        
        # Date & Time
        self.clock_label = QLabel()
        self.clock_label.setStyleSheet("color: #F1F5F9; font-weight: 500; font-size: 12px; padding-left: 8px;")
        layout.addWidget(self.clock_label)
        
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)
        self.update_clock()
        
    def update_clock(self):
        now = datetime.datetime.now()
        time_str = now.strftime("Tue May 27 10:30 AM") # Matched to user picture
        self.clock_label.setText(time_str)
