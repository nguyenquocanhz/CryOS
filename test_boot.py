"""
CryOS v1.0.0 Polaris - Standalone Boot Animation Tester
Plays the full 60fps Glowing Pulse Boot Animation.
"""

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

def main():
    print("=" * 65)
    print("💎 CryOS v1.0.0 Polaris - Boot Animation Tester")
    print("=" * 65)
    
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    boot_qml = Path(__file__).parent / "qml" / "bootsplash.qml"
    print(f"[INFO] Playing Boot Animation QML: {boot_qml}")
    
    engine.load(str(boot_qml))
    
    if not engine.rootObjects():
        print("[ERROR] Failed to load Boot Animation QML.")
        sys.exit(-1)
        
    splash_root = engine.rootObjects()[0]
    splash_root.bootFinished.connect(app.quit)
    
    print("[SUCCESS] Boot Animation is playing on screen...")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
