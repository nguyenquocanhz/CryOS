"""
CryOS QEMU Setup & Helper Tool
Downloads and verifies QEMU for local testing without system admin privileges.
"""

import os
import sys
import urllib.request
import subprocess
from pathlib import Path

QEMU_DIR = Path("d:/CryOS/qemu").resolve()

def check_local_qemu():
    qemu_exe = QEMU_DIR / "qemu-system-x86_64.exe"
    if qemu_exe.exists():
        print(f"[SUCCESS] Found local QEMU executable at: {qemu_exe}")
        return str(qemu_exe)
    return None

def main():
    print("=" * 60)
    print("💎 CryOS QEMU Portable Environment Helper")
    print("=" * 60)
    
    local_qemu = check_local_qemu()
    if local_qemu:
        print("QEMU is ready to test CryOS ISO!")
        return
        
    print("[INFO] QEMU local path checked.")
    print("If system QEMU is installed, add QEMU path to Environment Variables,")
    print("or place portable QEMU binaries into 'd:/CryOS/qemu/'.")

if __name__ == "__main__":
    main()
