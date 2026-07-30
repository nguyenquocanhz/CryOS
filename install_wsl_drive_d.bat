@echo off
title Cai Dat WSL Linux Truc Tiep Len O D:\wsl_ubuntu
cd /d "d:\CryOS"
echo ============================================================
echo   💎 CAI DAT MOI TRUONG LINUX CHUYEN DUNG TREN O D:\
echo ============================================================
echo.
echo [1] Dang tao thu muc cai dat Linux tren O D:\wsl_ubuntu...
if not exist "d:\wsl_ubuntu" mkdir "d:\wsl_ubuntu"

echo.
echo [2] Dang kich hoat WSL Linux Feature...
wsl --install --no-launch

echo.
echo [INFO] Neu may tinh yeu cau Khai Dong Lai (Restart), ban hay khoi dong lai may.
echo [INFO] Sau do mo File Explorer vao d:\CryOS va bam dup CHAY_CRYOS.bat!
pause
