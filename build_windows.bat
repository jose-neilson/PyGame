@echo off
setlocal

py -3.11 --version
if errorlevel 1 exit /b 1

py -3.11 -m pip install --upgrade pip
if errorlevel 1 exit /b 1

py -3.11 -m pip install -r requirements.txt
if errorlevel 1 exit /b 1

py -3.11 -m pip install -r requirements-dev.txt
if errorlevel 1 exit /b 1

py -3.11 -m PyInstaller --noconfirm --clean --onefile --windowed --name SkyboundPeaks main.py
if errorlevel 1 exit /b 1

if exist release rmdir /s /q release
mkdir release
copy dist\SkyboundPeaks.exe release\SkyboundPeaks.exe
xcopy "Mountain Shooter Assets" "release\Mountain Shooter Assets" /E /I /Y

powershell -NoProfile -ExecutionPolicy Bypass -Command "Compress-Archive -Path 'release\*' -DestinationPath 'SkyboundPeaks-Windows.zip' -Force"
if errorlevel 1 exit /b 1

echo.
echo Build finalizado: SkyboundPeaks-Windows.zip
echo Envie esse ZIP na atividade.
pause
