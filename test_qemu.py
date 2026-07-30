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
    os.path.expandvars(r"%LOCALAPPDATA%\Android\Sdk\emulator\qemu\windows-x86_64\qemu-system-x86_64.exe"),
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
    print("💎 CryOS v1.0.0 Polaris - QEMU Emulator Test Runner")
    print("=" * 65)
    
    qemu_bin = find_qemu()
    
    # Dynamically find any .iso file in output/ or kali-live-build/
    target_iso = None
    output_dir = ROOT_DIR / "output"
    if output_dir.exists():
        for iso_file in output_dir.glob("*.iso"):
            target_iso = iso_file
            break
            
    if not target_iso:
        iso_candidates = [
            ROOT_DIR / "output" / "kali-linux-rolling-live-cryos-amd64.iso",
            ROOT_DIR / "output" / "CryOS-v1.0.0-Polaris-UEFI-amd64.iso",
            ROOT_DIR / "kali-live-build" / "images" / "kali-rolling-cryos-amd64.iso"
        ]
        for iso in iso_candidates:
            if iso.exists():
                target_iso = iso
                break

    if not target_iso:
        print("[INFO] No compiled ISO found in output/ directory yet.")
        print("[ACTION] Run 'bash build_cryos_iso.sh' to generate the CryOS ISO")
        print("         or test the native QML GPU System UI directly using 'python run_qml.py'!")
        return

    print(f"[SUCCESS] Target ISO Found: {target_iso.name} ({target_iso.stat().st_size / (1024*1024):.1f} MB)")

    if not qemu_bin:
        print("[INFO] QEMU executable not found in Windows PATH.")
        print("[TIP] You can install QEMU via PowerShell:")
        print("      winget install SoftwareFreedomConservancy.QEMU")
        print("      Or double-click 'qemu-setup.exe' in D:\\CryOS\\")
        print(f"[WSL RUNNER] Attempting to run via WSL QEMU...")
        wsl_cmd = ["wsl", "qemu-system-x86_64", "-cdrom", f"/mnt/d/CryOS/output/{target_iso.name}", "-m", "4096", "-smp", "2", "-vga", "virtio"]
        try:
            subprocess.Popen(wsl_cmd)
            print("[SUCCESS] Launched QEMU via WSL.")
            return
        except Exception as e:
            print(f"[ERROR] Could not launch via WSL: {e}")
            return

    print(f"[SUCCESS] QEMU Executable Found: {qemu_bin}")
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
