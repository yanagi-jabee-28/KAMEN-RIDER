@echo off
setlocal

set "PYTHON_EXE=python"
if exist "%~dp0..\..\.venv\Scripts\python.exe" set "PYTHON_EXE=%~dp0..\..\.venv\Scripts\python.exe"
if exist "%~dp0..\..\.venv\bin\python.exe" set "PYTHON_EXE=%~dp0..\..\.venv\bin\python.exe"

REM Run in the current terminal so VS Code integrated terminal can handle everything in-place.
"%PYTHON_EXE%" "%~dp0scripts\run_refresh_workflow_rpg6.py" %*
set "EXIT_CODE=%ERRORLEVEL%"
exit /b %EXIT_CODE%
