"""
CryOS v1.0.0 Polaris - System Service Daemon (cryosd)
Backend IPC & System Management Service for CryOS Shell
"""

import sys
import os
import subprocess
import shutil
import psutil
from PyQt6.QtCore import QObject, pyqtSlot, pyqtSignal, pyqtProperty, QTimer

class CryOSService(QObject):
    # Signals to update QML Frontend in real-time
    cpuUsageChanged = pyqtSignal(float)
    ramUsageChanged = pyqtSignal(float)
    batteryPercentChanged = pyqtSignal(int)
    wifiStatusChanged = pyqtSignal(bool, str)
    bluetoothStatusChanged = pyqtSignal(bool)
    notificationReceived = pyqtSignal(str, str, str) # app_name, title, message

    def __init__(self, parent=None):
        super().__init__(parent)
        self._cpu_usage = 0.0
        self._ram_usage = 0.0
        self._battery_percent = 100
        self._wifi_enabled = True
        self._wifi_ssid = "CryNet_5G"
        self._bluetooth_enabled = True
        self._dnd_enabled = False
        self._volume_level = 70
        self._brightness_level = 85
        
        # System Monitor Loop Timer (Every 1.5 seconds)
        self.monitor_timer = QTimer(self)
        self.monitor_timer.timeout.connect(self._update_system_stats)
        self.monitor_timer.start(1500)
        self._update_system_stats()

    # --- Properties Exposed to QML ---
    @pyqtProperty(float, notify=cpuUsageChanged)
    def cpuUsage(self):
        return self._cpu_usage

    @pyqtProperty(float, notify=ramUsageChanged)
    def ramUsage(self):
        return self._ram_usage

    @pyqtProperty(int, notify=batteryPercentChanged)
    def batteryPercent(self):
        return self._battery_percent

    @pyqtProperty(bool, notify=wifiStatusChanged)
    def wifiEnabled(self):
        return self._wifi_enabled

    @pyqtProperty(str)
    def wifiSsid(self):
        return self._wifi_ssid

    @pyqtProperty(bool)
    def bluetoothEnabled(self):
        return self._bluetooth_enabled

    @pyqtProperty(int)
    def volumeLevel(self):
        return self._volume_level

    @pyqtProperty(int)
    def brightnessLevel(self):
        return self._brightness_level

    # --- Real-Time Hardware Monitoring ---
    def _update_system_stats(self):
        try:
            self._cpu_usage = psutil.cpu_percent()
            self.cpuUsageChanged.emit(self._cpu_usage)
            
            ram = psutil.virtual_memory()
            self._ram_usage = ram.percent
            self.ramUsageChanged.emit(self._ram_usage)
            
            battery = psutil.sensors_battery()
            if battery:
                self._battery_percent = int(battery.percent)
                self.batteryPercentChanged.emit(self._battery_percent)
        except Exception as e:
            pass

    # --- System Control Slots Invokable from QML ---
    @pyqtSlot(str)
    def launchApp(self, app_name):
        """App Service Launcher - Opens native applications asynchronously"""
        print(f"[cryosd] App Service requested launch for: '{app_name}'")
        
        app_map = {
            "Terminal": ["powershell", "-NoExit"] if sys.platform == "win32" else ["x-terminal-emulator"],
            "VS Code": ["code"],
            "Browser": ["start", "https://google.com"] if sys.platform == "win32" else ["xdg-open", "https://google.com"],
            "Finder": ["explorer"] if sys.platform == "win32" else ["nautilus"],
            "Nmap": ["nmap", "--help"],
            "Wireshark": ["wireshark"],
        }
        
        cmd = app_map.get(app_name)
        if cmd:
            try:
                subprocess.Popen(cmd, shell=(sys.platform == "win32"))
                self.notificationReceived.emit("CryOS Service", "Application Started", f"Launched {app_name} successfully.")
            except Exception as e:
                print(f"[cryosd ERROR] Could not launch {app_name}: {e}")

    @pyqtSlot()
    def toggleWifi(self):
        self._wifi_enabled = not self._wifi_enabled
        status_str = "Enabled" if self._wifi_enabled else "Disabled"
        print(f"[cryosd] Wi-Fi Service: {status_str}")
        self.wifiStatusChanged.emit(self._wifi_enabled, self._wifi_ssid)
        self.notificationReceived.emit("Network Service", "Wi-Fi Status", f"Wi-Fi is now {status_str}")

    @pyqtSlot()
    def toggleBluetooth(self):
        self._bluetooth_enabled = not self._bluetooth_enabled
        status_str = "Enabled" if self._bluetooth_enabled else "Disabled"
        print(f"[cryosd] Bluetooth Service: {status_str}")
        self.bluetoothStatusChanged.emit(self._bluetooth_enabled)

    @pyqtSlot(int)
    def setVolume(self, level):
        self._volume_level = level
        print(f"[cryosd] Volume Service level set to: {level}%")

    @pyqtSlot(int)
    def setBrightness(self, level):
        self._brightness_level = level
        print(f"[cryosd] Display Brightness Service set to: {level}%")
