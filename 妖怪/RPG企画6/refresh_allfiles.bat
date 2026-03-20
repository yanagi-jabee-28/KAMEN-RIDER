@echo off
setlocal

set "PYTHON_EXE=python"
if exist "%~dp0..\..\.venv\Scripts\python.exe" set "PYTHON_EXE=%~dp0..\..\.venv\Scripts\python.exe"
if exist "%~dp0..\..\.venv\bin\python.exe" set "PYTHON_EXE=%~dp0..\..\.venv\bin\python.exe"

"%PYTHON_EXE%" "%~dp0scripts\run_refresh_workflow_rpg6.py" %*
exit /b %errorlevel%
