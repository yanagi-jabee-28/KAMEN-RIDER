@echo off
REM Simple wrapper to invoke the Python refresh script from Windows.
REM Place this file at the project root (same directory as refresh_allfiles.py),
REM then run it from anywhere or double-click it.

REM if the user has a venv activated, use its python; otherwise rely on PATH
if exist "%~dp0..\.venv\Scripts\python.exe" (
    "%~dp0..\.venv\Scripts\python.exe" "%~dp0refresh_allfiles.py"
) else (
    python "%~dp0refresh_allfiles.py"
)
