from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QPushButton, QGridLayout, QWidget
)
from PyQt6.QtCore import Qt
from cryos.styles import POLARIS_STYLES

class CryControlCenter(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ControlCenterPanel")
        self.setStyleSheet(POLARIS_STYLES)
        self.setFixedWidth(330)
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(12)
        
        # 1. Quick Toggles Grid (2x3)
        grid_widget = QWidget()
        grid = QGridLayout(grid_widget)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setSpacing(8)
        
        toggles = [
            ("📶", "Wi-Fi", "CryNet_5G", True),
            ("🎧", "Bluetooth", "On", True),
            ("📡", "AirDrop", "Everyone", True),
            ("🌙", "Do Not Disturb", "On", False),
            ("🔆", "Keyboard", "Brightness", False),
            ("🖥", "Screen", "Mirroring", False),
        ]
        
        for idx, (icon, title, sub, active) in enumerate(toggles):
            card = QFrame()
            card.setObjectName("ToggleCardActive" if active else "ToggleCard")
            c_layout = QHBoxLayout(card)
            c_layout.setContentsMargins(10, 8, 10, 8)
            c_layout.setSpacing(8)
            
            ic_lbl = QLabel(icon)
            ic_lbl.setStyleSheet("font-size: 18px;")
            c_layout.addWidget(ic_lbl)
            
            txt_box = QVBoxLayout()
            t_lbl = QLabel(title)
            t_lbl.setStyleSheet("font-weight: 700; font-size: 11px;")
            s_lbl = QLabel(sub)
            s_lbl.setStyleSheet("font-size: 10px; color: rgba(255, 255, 255, 0.7);")
            txt_box.addWidget(t_lbl)
            txt_box.addWidget(s_lbl)
            c_layout.addLayout(txt_box)
            
            grid.addWidget(card, idx // 2, idx % 2)
            
        layout.addWidget(grid_widget)
        
        # 2. Display Brightness Slider Card
        disp_card = QFrame()
        disp_card.setObjectName("ToggleCard")
        dc_layout = QVBoxLayout(disp_card)
        dc_layout.setContentsMargins(12, 10, 12, 10)
        
        d_hdr = QLabel("Display")
        d_hdr.setStyleSheet("font-size: 11px; font-weight: 600; color: #94A3B8;")
        dc_layout.addWidget(d_hdr)
        
        d_slider = QSlider(Qt.Orientation.Horizontal)
        d_slider.setValue(85)
        dc_layout.addWidget(d_slider)
        layout.addWidget(disp_card)
        
        # 3. Sound Volume Slider Card
        snd_card = QFrame()
        snd_card.setObjectName("ToggleCard")
        sc_layout = QVBoxLayout(snd_card)
        sc_layout.setContentsMargins(12, 10, 12, 10)
        
        s_hdr = QLabel("Sound")
        s_hdr.setStyleSheet("font-size: 11px; font-weight: 600; color: #94A3B8;")
        sc_layout.addWidget(s_hdr)
        
        s_slider = QSlider(Qt.Orientation.Horizontal)
        s_slider.setValue(70)
        sc_layout.addWidget(s_slider)
        layout.addWidget(snd_card)
        
        # 4. Media Player Card
        media_card = QFrame()
        media_card.setObjectName("ToggleCard")
        mc_layout = QHBoxLayout(media_card)
        mc_layout.setContentsMargins(10, 8, 10, 8)
        
        cover = QLabel("🎵")
        cover.setStyleSheet("background: rgba(56, 189, 248, 0.2); border-radius: 8px; font-size: 24px; padding: 6px;")
        mc_layout.addWidget(cover)
        
        m_txt = QVBoxLayout()
        m_title = QLabel("Arctic Winds")
        m_title.setStyleSheet("font-weight: 700; font-size: 12px;")
        m_sub = QLabel("Nordic Lights")
        m_sub.setStyleSheet("font-size: 10px; color: #94A3B8;")
        m_txt.addWidget(m_title)
        m_txt.addWidget(m_sub)
        mc_layout.addLayout(m_txt)
        mc_layout.addStretch()
        
        m_ctrl = QLabel("⏮  ⏯  ⏭")
        m_ctrl.setStyleSheet("font-size: 14px; color: #E2E8F0; padding-right: 6px;")
        mc_layout.addWidget(m_ctrl)
        layout.addWidget(media_card)
        
        # 5. Notifications
        notifs = [
            ("💎", "CryOS System", "now", "Update available: CryOS 1.0.1 is ready to install."),
            ("🖼", "Photos", "2m ago", "New memory created 'Winter Trip 2024'"),
            ("💬", "Messages", "5m ago", "Liam: Let's meet at 3PM later!"),
        ]
        
        for icon, app_n, time_n, msg_n in notifs:
            n_card = QFrame()
            n_card.setObjectName("NotifCard")
            n_layout = QVBoxLayout(n_card)
            n_layout.setContentsMargins(8, 6, 8, 6)
            
            nh_box = QHBoxLayout()
            nh_lbl = QLabel(f"{icon}  <b>{app_n}</b>")
            nh_lbl.setStyleSheet("font-size: 11px;")
            nt_lbl = QLabel(time_n)
            nt_lbl.setStyleSheet("font-size: 9px; color: #64748B;")
            nh_box.addWidget(nh_lbl)
            nh_box.addStretch()
            nh_box.addWidget(nt_lbl)
            n_layout.addLayout(nh_box)
            
            nm_lbl = QLabel(msg_n)
            nm_lbl.setStyleSheet("font-size: 11px; color: #CBD5E1; margin-top: 2px;")
            n_layout.addWidget(nm_lbl)
            
            layout.addWidget(n_card)
            
        # Clear All Button
        clear_btn = QPushButton("Clear All")
        clear_btn.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: #64748B;
                font-size: 11px;
                border: none;
            }
            QPushButton:hover {
                color: #94A3B8;
            }
        """)
        layout.addWidget(clear_btn, alignment=Qt.AlignmentFlag.AlignRight)
