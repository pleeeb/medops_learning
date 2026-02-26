@echo off
title Dosage Master Pro - Setup and Run
color 0A

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║           💊 DOSAGE MASTER PRO - Auto Launcher 💊              ║
echo ╠════════════════════════════════════════════════════════════════╣
echo ║  This script will automatically set up and run the app.       ║
echo ║  It will download a portable Python if not installed.         ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

:: Check if Python is available
python --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo ✓ Python found on system!
    goto :install_deps
)

:: Check for py launcher
py --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo ✓ Python found via py launcher!
    set PYTHON_CMD=py
    goto :install_deps_py
)

echo ✗ Python not found. Installing portable Python...
echo.
goto :portable_python

:install_deps
echo.
echo Installing required packages...
python -m pip install --upgrade pip >nul 2>&1
python -m pip install streamlit numpy matplotlib graphviz
echo.
echo ✓ Dependencies installed!
echo.
echo ════════════════════════════════════════════════════════════════
echo    Starting Dosage Master Pro...
echo    The app will open in your browser at http://localhost:8501
echo    Press Ctrl+C to stop the server when done.
echo ════════════════════════════════════════════════════════════════
echo.
python -m streamlit run app.py
goto :end

:install_deps_py
echo.
echo Installing required packages...
%PYTHON_CMD% -m pip install --upgrade pip >nul 2>&1
%PYTHON_CMD% -m pip install streamlit numpy matplotlib graphviz
echo.
echo ✓ Dependencies installed!
echo.
echo ════════════════════════════════════════════════════════════════
echo    Starting Dosage Master Pro...
echo    The app will open in your browser at http://localhost:8501
echo    Press Ctrl+C to stop the server when done.
echo ════════════════════════════════════════════════════════════════
echo.
%PYTHON_CMD% -m streamlit run app.py
goto :end

:portable_python
echo.
echo ══════════════════════════════════════════════════════════════════
echo  Python is not installed. Please choose an option:
echo ══════════════════════════════════════════════════════════════════
echo.
echo  [1] Download Python from python.org (recommended, 5 min setup)
echo  [2] Use Streamlit Cloud (no installation, just upload files)
echo  [3] Use Docker (if Docker Desktop is installed)
echo.
echo ══════════════════════════════════════════════════════════════════
echo.
echo OPTION 1: Install Python
echo   1. Go to https://www.python.org/downloads/
echo   2. Download and install Python 3.11+
echo   3. ✓ CHECK "Add Python to PATH" during installation!
echo   4. Run this script again
echo.
echo OPTION 2: Streamlit Cloud (FREE, no installation!)
echo   1. Go to https://share.streamlit.io/
echo   2. Sign in with GitHub
echo   3. Upload your app files (app.py, utils.py, requirements.txt)
echo   4. Click Deploy - done! Share the link with anyone.
echo.
echo OPTION 3: Docker
echo   1. Install Docker Desktop from https://docker.com
echo   2. Run: docker-compose up --build
echo.
pause

:end
echo.
echo Thank you for using Dosage Master Pro!
pause
