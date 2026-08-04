@echo off

echo Running Ruff lint...
ruff check .

if errorlevel 1 (
    echo Ruff linting failed. Please fix the issues above.
    pause
    exit /b 1
)

echo.
echo Checking formatting...
ruff format --check .
if errorlevel 1 (
    echo Ruff formatting check failed. Please fix the issues above.
    pause
    exit /b 1
)

pause