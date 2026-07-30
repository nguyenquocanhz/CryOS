@echo off
title CryOS v1.0.0 Polaris Launcher
cd /d "d:\CryOS"
echo ======================================================
echo  💎 Khoi chay CryOS v1.0.0 Polaris System Interface
echo ======================================================
if exist "dist\CryOS\CryOS.exe" (
    start "" "dist\CryOS\CryOS.exe"
) else (
    python run_qml.py
)
