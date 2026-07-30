#!/bin/bash
# CryOS v1.0.0 Polaris - Master ISO Build Script

set -e

echo "💎 Starting CryOS v1.0.0 Polaris ISO Build Process..."

# 1. Ensure build dependencies are installed
apt update
apt install -y curl git live-build cdebootstrap python3 dos2unix rsync dctrl-tools

# 2. Copy project to native WSL ext4 filesystem (prevents NTFS/DrvFS tar permission errors)
BUILD_DIR="/var/tmp/cryos-build"
echo "📂 Syncing CryOS project to native Linux filesystem ($BUILD_DIR)..."
mkdir -p "$BUILD_DIR"
rsync -a --exclude='.git' --exclude='qemu-setup.exe' --exclude='build' --exclude='dist' --exclude='output' --exclude='__pycache__' --exclude='*.exe' /mnt/d/CryOS/ "$BUILD_DIR/" || true

cd "$BUILD_DIR"

# 3. Copy CryOS Desktop Shell into Live ISO root overlay
mkdir -p kali-live-build/kali-config/variant-cryos/includes.chroot/usr/share/cryos
cp -r main.py cryos/ kali-live-build/kali-config/variant-cryos/includes.chroot/usr/share/cryos/
chmod +x kali-live-build/kali-config/variant-cryos/includes.chroot/usr/bin/cryos-session 2>/dev/null || true

# 4. Build the ISO image using official Kali Live Build Framework
cd kali-live-build
echo "🚀 Building CryOS ISO (distribution: kali-rolling, variant: cryos)..."
./build.sh --distribution kali-rolling --variant cryos --verbose

# 5. Copy output ISO image back to Windows Drive D:
mkdir -p /mnt/d/CryOS/output
mkdir -p /mnt/d/CryOS/kali-live-build/images
cp -r images/* /mnt/d/CryOS/output/ 2>/dev/null || true
cp -r images/* /mnt/d/CryOS/kali-live-build/images/ 2>/dev/null || true

echo "✅ CryOS v1.0.0 Polaris ISO compiled successfully!"
echo "📦 Output ISO image is located in: d:/CryOS/output/"

