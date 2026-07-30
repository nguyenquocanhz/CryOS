import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QShortcut, QKeySequence

from cryos.topbar import CryTopBar
from cryos.dock import CryDock
from cryos.spotlight import CrySpotlight
from cryos.hub import CryHub
from cryos.finder import CryFinder
from cryos.terminal import CryTerminal
from cryos.control_center import CryControlCenter
from cryos.bootsplash import CryOSBootSplash

class CryOSPolarisDesktopWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CryOS 1.0.0 Polaris")
        self.resize(1366, 768)
        
        self.hub_window = None
        self.spotlight_dialog = None
        
        self.init_ui()
        
        # Shortcut Ctrl+Space for Spotlight
        self.shortcut_spotlight = QShortcut(QKeySequence("Ctrl+Space"), self)
        self.shortcut_spotlight.activated.connect(self.open_spotlight)
        
    def init_ui(self):
        central = QWidget()
        central.setStyleSheet("""
            QWidget#DesktopCentral {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1, 
                    stop:0 #090E1A, stop:0.4 #101B35, stop:0.7 #1E1B4B, stop:1 #0A1128
                );
            }
        """)
        central.setObjectName("DesktopCentral")
        self.setCentralWidget(central)
        
        root_layout = QVBoxLayout(central)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)
        
        # 1. Top Bar
        self.topbar = CryTopBar(
            parent=self, 
            toggle_control_center_cb=self.toggle_control_center,
            open_spotlight_cb=self.open_spotlight
        )
        root_layout.addWidget(self.topbar)
        
        # 2. Desktop Work Area
        desktop_workarea = QWidget()
        dw_layout = QHBoxLayout(desktop_workarea)
        dw_layout.setContentsMargins(20, 16, 20, 10)
        dw_layout.setSpacing(16)
        
        # Left Workspace Column
        left_col = QWidget()
        lc_layout = QVBoxLayout(left_col)
        lc_layout.setContentsMargins(0, 0, 0, 0)
        lc_layout.setSpacing(12)
        
        # Top-Left Brand Logo Text on Wallpaper
        brand_box = QHBoxLayout()
        b_icon = QLabel("💎")
        b_icon.setStyleSheet("font-size: 32px;")
        b_txt_box = QVBoxLayout()
        b_title = QLabel("CryOS")
        b_title.setStyleSheet("font-size: 20px; font-weight: 800; color: #FFFFFF;")
        b_ver = QLabel("v1.0.0 Polaris")
        b_ver.setStyleSheet("font-size: 11px; color: #94A3B8;")
        b_txt_box.addWidget(b_title)
        b_txt_box.addWidget(b_ver)
        brand_box.addWidget(b_icon)
        brand_box.addLayout(b_txt_box)
        brand_box.addStretch()
        lc_layout.addLayout(brand_box)
        
        # CryFinder Window
        self.finder_window = CryFinder()
        lc_layout.addWidget(self.finder_window, stretch=2)
        
        # CryTerminal Window
        self.terminal_window = CryTerminal()
        lc_layout.addWidget(self.terminal_window, stretch=2)
        
        dw_layout.addWidget(left_col, stretch=3)
        
        # Right Workspace Column (Control Center Panel)
        self.control_center = CryControlCenter()
        dw_layout.addWidget(self.control_center, alignment=Qt.AlignmentFlag.AlignTop)
        
        root_layout.addWidget(desktop_workarea, stretch=1)
        
        # 3. Bottom Floating Dock
        self.dock = CryDock(
            parent=self,
            open_spotlight_cb=self.open_spotlight,
            open_hub_cb=self.open_hub,
            open_finder_cb=self.focus_finder,
            open_term_cb=self.focus_terminal
        )
        root_layout.addWidget(self.dock, alignment=Qt.AlignmentFlag.AlignCenter)
        
    def toggle_control_center(self):
        self.control_center.setVisible(not self.control_center.isVisible())

    def open_spotlight(self):
        if not self.spotlight_dialog or not self.spotlight_dialog.isVisible():
            self.spotlight_dialog = CrySpotlight(self, open_hub_cb=self.open_hub)
            geo = self.geometry()
            self.spotlight_dialog.move(
                geo.x() + (geo.width() - self.spotlight_dialog.width()) // 2,
                geo.y() + (geo.height() - self.spotlight_dialog.height()) // 2 - 60
            )
            self.spotlight_dialog.show()

    def open_hub(self):
        if not self.hub_window or not self.hub_window.isVisible():
            self.hub_window = CryHub(self)
            self.hub_window.show()

    def focus_finder(self):
        self.finder_window.show()
        self.finder_window.raise_()

    def focus_terminal(self):
        self.terminal_window.show()
        self.terminal_window.raise_()

desktop_window_instance = None

def start_desktop():
    global desktop_window_instance
    desktop_window_instance = CryOSPolarisDesktopWindow()
    desktop_window_instance.showMaximized()

def main():
    app = QApplication(sys.argv)
    
    # 1. First show Boot Logo Splash Screen
    splash = CryOSBootSplash(on_finish_callback=start_desktop)
    splash.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
