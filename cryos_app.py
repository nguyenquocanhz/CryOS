"""
CryOS v1.0.0 Polaris - Standalone System Interface App
Dedicated single-purpose executable for running the CryOS System Shell.
"""

import sys
import os
from pathlib import Path

# Fix Windows console UTF-8 output
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject, pyqtSlot

from cryos.service import CryOSService

class BootHandoffController(QObject):
    def __init__(self, engine, main_qml_path, cryos_service):
        super().__init__()
        self.engine = engine
        self.main_qml_path = main_qml_path
        self.cryos_service = cryos_service

    @pyqtSlot()
    def onBootFinished(self):
        print("[SUCCESS] CryOS Boot Animation Finished -> Entering Standalone System Shell...")
        for obj in self.engine.rootObjects():
            obj.deleteLater()
            
        self.engine.rootContext().setContextProperty("cryosService", self.cryos_service)
        self.engine.load(str(self.main_qml_path))

def main():
    print("=" * 65)
    print("💎 CryOS v1.0.0 Polaris - Standalone System Interface App")
    print("=" * 65)
    
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    # 1. Start CryOS Backend System Daemon Service
    cryos_service = CryOSService()
    print("[INFO] CryOS System Service Active.")
    
    # Locate QML assets
    base_dir = Path(__file__).parent
    splash_qml = base_dir / "qml" / "bootsplash.qml"
    main_qml = base_dir / "qml" / "main.qml"
    
    controller = BootHandoffController(engine, main_qml, cryos_service)
    
    print(f"[INFO] Playing System Boot Animation: {splash_qml.name}")
    engine.load(str(splash_qml))
    
    root_objects = engine.rootObjects()
    if not root_objects:
        print("[ERROR] Failed to load CryOS System UI QML.")
        sys.exit(-1)
        
    splash_root = root_objects[0]
    splash_root.bootFinished.connect(controller.onBootFinished)
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
