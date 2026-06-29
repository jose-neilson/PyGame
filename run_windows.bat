@echo off
setlocal

py -3.11 --version
if errorlevel 1 exit /b 1

py -3.11 -m pip install -r requirements.txt
if errorlevel 1 exit /b 1

py -3.11 main.py
pause
