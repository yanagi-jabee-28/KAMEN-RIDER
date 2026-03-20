@echo off
setlocal

set "PYTHON_EXE=python"
if exist "%~dp0..\..\.venv\Scripts\python.exe" set "PYTHON_EXE=%~dp0..\..\.venv\Scripts\python.exe"
if exist "%~dp0..\..\.venv\bin\python.exe" set "PYTHON_EXE=%~dp0..\..\.venv\bin\python.exe"

REM Run the workflow in a separate process group via START to avoid Ctrl+C in this batch file forcing "Terminate batch job" prompt.
start "" /wait "%PYTHON_EXE%" "%~dp0scripts\run_refresh_workflow_rpg6.py" %*
exit /b %errorlevel%
