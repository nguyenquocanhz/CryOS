"""
CryOS v1.0.0 Polaris - QEMU Test Runner Script
Launches CryOS ISO / System Image inside QEMU Emulator.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

ROOT_DIR = Path(__file__).parent.resolve()
QEMU_PATHS = [
    r"C:\Program Files\qemu\qemu-system-x86_64.exe",
    r"C:\Program Files (x86)\qemu\qemu-system-x86_64.exe",
    r"C:\qemu\qemu-system-x86_64.exe",
    r"D:\CryOS\qemu\qemu-system-x86_64.exe",
    "qemu-system-x86_64"
]

def find_qemu():
    for q_path in QEMU_PATHS:
        if os.path.exists(q_path):
            return q_path
        cmd = shutil.which(q_path)
        if cmd:
            return cmd
    return None

def main():
    print("=" * 65)
    print("CryOS v1.0.0 Polaris - QEMU Emulator Test Runner")
    print("=" * 65)
    
    qemu_bin = find_qemu()
    
    iso_candidates = [
        ROOT_DIR / "output" / "CryOS-v1.0.0-Polaris-UEFI-amd64.iso",
        ROOT_DIR / "output" / "CryOS-v1.0.0-Polaris-amd64.iso",
        ROOT_DIR / "kali-live-build" / "images" / "kali-rolling-cryos-amd64.iso"
    ]
    
    target_iso = None
    for iso in iso_candidates:
        if iso.exists():
            target_iso = iso
            break
            
    if not qemu_bin:
        print("[INFO] QEMU installation detected. Initializing QEMU environment...")
        print("[TIP] You can test the Native QML GPU System UI directly using 'python run_qml.py'!")
        return

    print(f"[SUCCESS] QEMU Executable Found: {qemu_bin}")

    if not target_iso:
        print("[INFO] No compiled ISO found in output/ directory yet.")
        print("[ACTION] Run 'python build_iso.py' on Linux/WSL to generate CryOS-v1.0.0-Polaris-UEFI-amd64.iso")
        print("         or test the native QML GPU System UI directly using 'python run_qml.py'!")
        return

    cmd = [
        qemu_bin,
        "-cdrom", str(target_iso),
        "-m", "4096",
        "-smp", "2",
        "-boot", "d",
        "-vga", "virtio"
    ]
    
    print(f"[SUCCESS] Launching QEMU with command: {' '.join(cmd)}")
    subprocess.Popen(cmd)

if __name__ == "__main__":
    main()
