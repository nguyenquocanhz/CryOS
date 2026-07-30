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

from cryos.service import CryOSService

class BootHandoffController(QObject):
    def __init__(self, engine, main_qml_path, cryos_service):
        super().__init__()
        self.engine = engine
        self.main_qml_path = main_qml_path
        self.cryos_service = cryos_service

    @pyqtSlot()
    def onBootFinished(self):
        print("[SUCCESS] Boot Splash Animation Completed -> Transitioning to CryOS Polaris Desktop...")
        for obj in self.engine.rootObjects():
            obj.deleteLater()
            
        # Bind cryosService to QML Context
        self.engine.rootContext().setContextProperty("cryosService", self.cryos_service)
        self.engine.load(str(self.main_qml_path))

def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    # 1. Start CryOS System App Service Daemon
    cryos_service = CryOSService()
    print("[INFO] CryOS System App Service Daemon (cryosd) Started Successfully.")
    
    qml_dir = Path(__file__).parent / "qml"
    splash_qml = qml_dir / "bootsplash.qml"
    main_qml = qml_dir / "main.qml"
    
    controller = BootHandoffController(engine, main_qml, cryos_service)
    
    print(f"[INFO] Playing CryOS Flicker-Free Boot Animation: {splash_qml}")
    
    engine.objectCreated.connect(
        lambda obj, url: print(f"[INFO] QML Component loaded from {url}") if obj else print(f"[ERROR] Failed loading {url}")
    )
    
    engine.load(str(splash_qml))
    
    root_objects = engine.rootObjects()
    if not root_objects:
        print("[ERROR] Failed to load boot splash QML.")
        sys.exit(-1)
        
    splash_root = root_objects[0]
    splash_root.bootFinished.connect(controller.onBootFinished)
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
