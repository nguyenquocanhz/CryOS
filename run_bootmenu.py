import sys
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject, pyqtSlot

class BootMenuController(QObject):
    def __init__(self, app):
        super().__init__()
        self.app = app

    @pyqtSlot(str)
    def onBootOptionSelected(self, option_name):
        print(f"[SUCCESS] Boot Menu Selected: '{option_name}' -> Booting System...")
        self.app.quit()

def main():
    print("=" * 65)
    print("💎 CryOS v1.0.0 Polaris - Boot Menu UI Runner")
    print("=" * 65)
    
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    controller = BootMenuController(app)
    
    boot_qml = Path(__file__).parent / "qml" / "bootmenu.qml"
    print(f"[INFO] Loading Boot Menu QML: {boot_qml}")
    
    engine.load(str(boot_qml))
    
    root_objects = engine.rootObjects()
    if not root_objects:
        print("[ERROR] Failed to load Boot Menu QML.")
        sys.exit(-1)
        
    menu_root = root_objects[0]
    menu_root.bootOptionSelected.connect(controller.onBootOptionSelected)
    
    print("[SUCCESS] Boot Menu UI is active! Use UP/DOWN arrows or ENTER key.")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
