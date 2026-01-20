@echo off
chcp 65001 >nul
echo ============================================
echo   ROI Calculator - Build Executable
echo ============================================
echo.

set "PROJECT_DIR=D:\code\git\roi_calculator"
set "VENV_DIR=%PROJECT_DIR%\venv312\Scripts"

rem Remove old build
if exist "%PROJECT_DIR%\dist\ROI_Calculator" rmdir /s /q "%PROJECT_DIR%\dist\ROI_Calculator"
if exist "%PROJECT_DIR%\build" rmdir /s /q "%PROJECT_DIR%\build"
del /q "%PROJECT_DIR%\ROI_Calculator.spec" 2>nul

rem Build exe
echo [INFO] Building executable...
"%VENV_DIR%\python.exe" -m PyInstaller --onedir --name ROI_Calculator --paths "%PROJECT_DIR%\venv312\Lib\site-packages" --add-data "%PROJECT_DIR%\venv312\Lib\site-packages\akshare\file_fold;akshare\file_fold" --add-data "%PROJECT_DIR%\config.py;." --add-data "%PROJECT_DIR%\roi.py;." --workpath "%PROJECT_DIR%\build" --distpath "%PROJECT_DIR%\dist" "%PROJECT_DIR%\main_fast.py"

rem Copy stocks.json template to dist folder
if exist "%PROJECT_DIR%\stocks.json" (
    copy "%PROJECT_DIR%\stocks.json" "%PROJECT_DIR%\dist\ROI_Calculator\stocks.json" >nul
    echo.
    echo [INFO] stocks.json template copied to dist folder
)

echo.
if exist "%PROJECT_DIR%\dist\ROI_Calculator\ROI_Calculator.exe" (
    echo Build SUCCESS!
    echo Output: %PROJECT_DIR%\dist\ROI_Calculator\ROI_Calculator.exe
    echo.
    echo ============================================
    echo   Custom Stock List Instructions
    echo ============================================
    echo.
    echo 1. Copy stocks.json to exe directory
    echo 2. Edit stocks.json to customize stock list
    echo 3. Program will prioritize external config
    echo.
) else (
    echo Build FAILED!
)
pause
