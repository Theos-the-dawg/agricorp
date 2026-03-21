@echo off
REM AgriCorp Development Server Starter for Windows
REM Run both Django and React development servers simultaneously

echo 🌾 Starting AgriCorp Development Environment...
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install dependencies
echo Checking Django dependencies...
pip install -r requirements.txt -q

REM Start Django server
echo.
echo 🚀 Starting Django server on http://localhost:8000...
start "Django Server" python manage.py runserver

REM Start React development server
echo 🎨 Starting React frontend on http://localhost:5173...
cd frontend

REM Check if node_modules exists
if not exist "node_modules" (
    echo Installing React dependencies...
    call npm install -q
)

start "React Frontend" npm run dev

cd ..

echo.
echo ✅ Both servers are starting!
echo.
echo Frontend: http://localhost:5173
echo Backend:  http://localhost:8000
echo Admin:    http://localhost:8000/admin
echo.
echo Press Ctrl+C in the terminal windows to stop the servers.
echo.

call .venv\Scripts\activate.bat
