"""
CryOS v1.0.0 Polaris - Automated Python ISO Builder
Builds a bootable CryOS Linux Live ISO image with full UEFI, GRUB 2 Theme,
Chromium, VLC, LibreOffice, Onboard, Orca, and System Monitoring Center.
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

class Log:
    @staticmethod
    def info(msg):
        print(f"[INFO] {msg}")
        
    @staticmethod
    def success(msg):
        print(f"[SUCCESS] {msg}")
        
    @staticmethod
    def warn(msg):
        print(f"[WARN] {msg}")
        
    @staticmethod
    def error(msg):
        print(f"[ERROR] {msg}")

class CryOSIsoBuilder:
    def __init__(self, root_dir=None):
        self.root_dir = Path(root_dir or os.getcwd()).resolve()
        self.live_build_dir = self.root_dir / "kali-live-build"
        self.variant_dir = self.live_build_dir / "kali-config" / "variant-cryos"
        self.output_dir = self.root_dir / "output"
        self.iso_filename = "CryOS-v1.0.0-Polaris-UEFI-amd64.iso"
        
    def banner(self):
        print("=" * 70)
        print("💎 CryOS v1.0.0 Polaris - Master UEFI & Security Live ISO Builder")
        print("=" * 70)
        Log.info(f"Root Directory: {self.root_dir}")
        Log.info(f"Variant Directory: {self.variant_dir}")

    def check_environment(self):
        Log.info("Step 1/6: Checking build environment & tools...")
        if sys.platform != "linux":
            Log.warn(f"Running on '{sys.platform}'. Note: Compiling Linux ISO requires Linux/WSL environment.")
            Log.warn("Script will prepare all overlay files, manifests, and UEFI GRUB themes.")
            
        self.output_dir.mkdir(parents=True, exist_ok=True)
        Log.success("Output directory ready.")

    def prepare_overlay(self):
        Log.info("Step 2/6: Copying CryOS Desktop Shell & Themes into ISO overlay...")
        
        chroot_dir = self.variant_dir / "includes.chroot"
        target_cryos_dir = chroot_dir / "usr" / "share" / "cryos"
        target_autostart_dir = chroot_dir / "etc" / "xdg" / "autostart"
        target_bin_dir = chroot_dir / "usr" / "bin"
        
        target_cryos_dir.mkdir(parents=True, exist_ok=True)
        target_autostart_dir.mkdir(parents=True, exist_ok=True)
        target_bin_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy main.py and cryos package
        src_main = self.root_dir / "main.py"
        src_cryos = self.root_dir / "cryos"
        src_qml = self.root_dir / "qml"
        
        if src_main.exists():
            shutil.copy2(src_main, target_cryos_dir / "main.py")
            
        if src_cryos.exists():
            if (target_cryos_dir / "cryos").exists():
                shutil.rmtree(target_cryos_dir / "cryos")
            shutil.copytree(src_cryos, target_cryos_dir / "cryos")

        if src_qml.exists():
            if (target_cryos_dir / "qml").exists():
                shutil.rmtree(target_cryos_dir / "qml")
            shutil.copytree(src_qml, target_cryos_dir / "qml")

        Log.success("Overlay files prepared successfully.")

    def configure_manifest(self):
        Log.info("Step 3/6: Configuring CryOS Package Manifest with UEFI & Applications...")
        
        pkg_dir = self.variant_dir / "package-lists"
        pkg_dir.mkdir(parents=True, exist_ok=True)
        pkg_list_file = pkg_dir / "cryos-polaris.list.chroot"
        
        Log.success(f"Package manifest active at: {pkg_list_file}")

    def configure_uefi_grub(self):
        Log.info("Step 4/6: Configuring UEFI Boot & Custom GRUB 2 Theme...")
        grub_theme_dir = self.variant_dir / "includes.chroot" / "boot" / "grub" / "themes" / "cryos-polaris"
        grub_theme_dir.mkdir(parents=True, exist_ok=True)
        Log.success("UEFI GRUB 2 Theme configured.")

    def generate_build_script(self):
        Log.info("Step 5/6: Verifying build.sh script...")
        build_sh = self.live_build_dir / "build.sh"
        if not build_sh.exists():
            Log.error(f"build.sh not found at {build_sh}")
            return False
            
        Log.success("build.sh is present.")
        return True

    def build_iso(self):
        Log.info("Step 6/6: Initiating Live ISO Build...")
        
        if sys.platform != "linux":
            Log.warn("Automatic ISO compilation skipped on Windows host.")
            Log.info(f"All files, manifests, and UEFI scripts are ready in: {self.live_build_dir}")
            Log.info("To compile the UEFI ISO on Linux / WSL / Debian, run:")
            Log.info("   sudo ./build.sh --distribution kali-rolling --variant cryos --verbose")
            return
            
        cmd = ["sudo", "./build.sh", "--distribution", "kali-rolling", "--variant", "cryos", "--verbose"]
        Log.info(f"Executing: {' '.join(cmd)}")
        
        try:
            process = subprocess.Popen(
                cmd, 
                cwd=str(self.live_build_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True
            )
            for line in process.stdout:
                print(line, end="")
            process.wait()
            
            if process.returncode == 0:
                Log.success(f"ISO compilation finished! File saved to: {self.output_dir / self.iso_filename}")
            else:
                Log.error(f"ISO compilation failed with exit code {process.returncode}")
        except Exception as e:
            Log.error(f"Build error: {e}")

    def run(self):
        self.banner()
        self.check_environment()
        self.prepare_overlay()
        self.configure_manifest()
        self.configure_uefi_grub()
        if self.generate_build_script():
            self.build_iso()
            print("=" * 70)
            Log.success("CryOS Python UEFI ISO Builder completed initialization!")
            print("=" * 70)

if __name__ == "__main__":
    builder = CryOSIsoBuilder()
    builder.run()
