import sys
import time
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QProgressBar, QApplication
from PyQt6.QtCore import Qt, QTimer
from cryos.styles import POLARIS_STYLES

class CryOSBootSplash(QWidget):
    def __init__(self, on_finish_callback=None):
        super().__init__()
        self.on_finish_callback = on_finish_callback
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.showMaximized()
        self.setStyleSheet("""
            QWidget#BootSplash {
                background-color: #060A12;
            }
        """)
        self.setObjectName("BootSplash")
        
        self.progress_value = 0
        self.status_messages = [
            "Booting CryOS Polaris Kernel 6.6...",
            "Initializing Hardware & Security Modules...",
            "Loading Kali Linux Repositories & Security Engine...",
            "Starting CryOS Quartz Window Manager...",
            "Applying Glassmorphism Compositor...",
            "Welcome to CryOS Polaris!"
        ]
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(16)
        
        # Glowing Crystal Logo
        logo = QLabel("💎")
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setStyleSheet("font-size: 90px; color: #38BDF8;")
        layout.addWidget(logo)
        
        # Brand Name
        title = QLabel("CryOS")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 36px; font-weight: 900; color: #FFFFFF; letter-spacing: 2px;")
        layout.addWidget(title)
        
        sub = QLabel("Polaris Edition")
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub.setStyleSheet("font-size: 13px; color: #94A3B8; margin-top: -8px;")
        layout.addWidget(sub)
        
        # Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedWidth(320)
        self.progress_bar.setFixedHeight(6)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 3px;
                border: none;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #38BDF8, stop:1 #A855F7);
                border-radius: 3px;
            }
        """)
        layout.addWidget(self.progress_bar, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Status Text
        self.status_label = QLabel(self.status_messages[0])
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 12px; color: #64748B; margin-top: 6px;")
        layout.addWidget(self.status_label)
        
        # Timer for boot simulation
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_boot)
        self.timer.start(35)
        
    def update_boot(self):
        self.progress_value += 1
        self.progress_bar.setValue(self.progress_value)
        
        # Update status messages
        idx = min(int(self.progress_value / 20), len(self.status_messages) - 1)
        self.status_label.setText(self.status_messages[idx])
        
        if self.progress_value >= 100:
            self.timer.stop()
            time.sleep(0.3)
            self.close()
            if self.on_finish_callback:
                self.on_finish_callback()
