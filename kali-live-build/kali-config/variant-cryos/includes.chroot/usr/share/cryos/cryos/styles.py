"""
CryOS v1.0.0 Polaris - Master QSS Glassmorphism Design System
"""

POLARIS_STYLES = """
/* Global Font & Reset */
* {
    font-family: 'Segoe UI', 'Inter', -apple-system, sans-serif;
    color: #F8FAFC;
}

/* TopBar */
QWidget#TopBar {
    background-color: rgba(12, 18, 32, 0.75);
    border-bottom: 1px solid rgba(255, 255, 255, 0.12);
}

QLabel#TopBarBrand {
    font-weight: 800;
    font-size: 14px;
    color: #38BDF8;
    padding-right: 12px;
}

QLabel#TopBarMenu {
    font-size: 13px;
    font-weight: 500;
    color: #E2E8F0;
    padding: 2px 8px;
    border-radius: 4px;
}

QLabel#TopBarMenu:hover {
    background-color: rgba(255, 255, 255, 0.15);
}

/* Traffic Lights */
QPushButton#BtnClose {
    background-color: #FF5F56;
    border: none;
    border-radius: 6px;
}
QPushButton#BtnMin {
    background-color: #FFBD2E;
    border: none;
    border-radius: 6px;
}
QPushButton#BtnMax {
    background-color: #27C93F;
    border: none;
    border-radius: 6px;
}

/* Finder Glass Window */
QFrame#FinderWindow {
    background-color: rgba(20, 30, 52, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
}

QFrame#Sidebar {
    background-color: rgba(15, 23, 42, 0.45);
    border-right: 1px solid rgba(255, 255, 255, 0.1);
    border-top-left-radius: 16px;
    border-bottom-left-radius: 16px;
}

QLabel#SidebarHeader {
    font-size: 11px;
    font-weight: 700;
    color: #64748B;
    text-transform: uppercase;
    padding: 10px 14px 4px 14px;
}

QLabel#SidebarItem {
    font-size: 13px;
    color: #CBD5E1;
    padding: 6px 14px;
    border-radius: 6px;
}

QLabel#SidebarItem:hover {
    background-color: rgba(56, 189, 248, 0.15);
    color: #FFFFFF;
}

QLabel#SidebarItemActive {
    background-color: rgba(56, 189, 248, 0.25);
    color: #38BDF8;
    font-weight: 600;
    padding: 6px 14px;
    border-radius: 6px;
}

/* Folder Card */
QFrame#FolderCard {
    background-color: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 12px;
    padding: 12px;
}

QFrame#FolderCard:hover {
    background-color: rgba(56, 189, 248, 0.15);
    border: 1px solid rgba(56, 189, 248, 0.5);
}

/* Terminal Glass Window */
QFrame#TerminalWindow {
    background-color: rgba(10, 14, 26, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 14px;
}

QTextEdit#TerminalBody {
    background-color: transparent;
    border: none;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 12px;
    color: #E2E8F0;
}

/* Control Center Panel */
QFrame#ControlCenterPanel {
    background-color: rgba(15, 23, 42, 0.82);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 20px;
}

QFrame#ToggleCard {
    background-color: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 14px;
}

QFrame#ToggleCardActive {
    background-color: rgba(37, 99, 235, 0.5);
    border: 1px solid rgba(59, 130, 246, 0.8);
    border-radius: 14px;
}

QSlider::groove:horizontal {
    height: 6px;
    background: rgba(255, 255, 255, 0.15);
    border-radius: 3px;
}

QSlider::sub-page:horizontal {
    background: #38BDF8;
    border-radius: 3px;
}

QSlider::handle:horizontal {
    background: #FFFFFF;
    width: 14px;
    height: 14px;
    margin-top: -4px;
    margin-bottom: -4px;
    border-radius: 7px;
}

/* Notification Item */
QFrame#NotifCard {
    background-color: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 10px;
}

/* Dock */
QFrame#DockPill {
    background-color: rgba(15, 23, 42, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 24px;
}

QPushButton#DockItem {
    background-color: transparent;
    border: none;
    border-radius: 12px;
}

QPushButton#DockItem:hover {
    background-color: rgba(255, 255, 255, 0.15);
}

/* Spotlight Modal */
QWidget#SpotlightContainer {
    background-color: rgba(15, 23, 42, 0.95);
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 16px;
}

QLineEdit#SearchInput {
    background-color: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 10px;
    color: #FFFFFF;
    font-size: 14px;
    padding: 8px 12px;
}

QListWidget#ResultList {
    background-color: transparent;
    border: none;
    color: #E2E8F0;
    font-size: 13px;
}

QListWidget#ResultList::item {
    padding: 8px 10px;
    border-radius: 8px;
}

QListWidget#ResultList::item:hover, QListWidget#ResultList::item:selected {
    background-color: rgba(56, 189, 248, 0.3);
    color: #FFFFFF;
}

/* CryHub Store */
QWidget#CryHubWindow {
    background-color: #0F172A;
    color: #F8FAFC;
}

QTabWidget::pane {
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    background-color: #1E293B;
}

QTabBar::tab {
    background: #0F172A;
    color: #94A3B8;
    padding: 10px 20px;
    font-weight: bold;
}

QTabBar::tab:selected {
    background: #1E293B;
    color: #38BDF8;
}

QFrame.ToolCard {
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 12px;
}

QPushButton.InstallButton {
    background-color: #2563EB;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    padding: 6px 14px;
}

QPushButton.LaunchButton {
    background-color: #16A34A;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 6px;
    padding: 6px 14px;
}
"""

GLASS_TOPBAR_STYLE = POLARIS_STYLES
GLASS_DOCK_STYLE = POLARIS_STYLES
SPOTLIGHT_STYLE = POLARIS_STYLES
CRYHUB_STYLE = POLARIS_STYLES
