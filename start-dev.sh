#!/bin/bash
# AgriCorp Development Server Starter
# Run both Django and React development servers simultaneously

echo "🌾 Starting AgriCorp Development Environment..."
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python -m venv .venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/Scripts/activate 2>/dev/null || source .venv/bin/activate

# Install dependencies if needed
echo "Checking Django dependencies..."
pip install -r requirements.txt -q

# Start Django server in background
echo ""
echo "🚀 Starting Django server on http://localhost:8000..."
python manage.py runserver &
DJANGO_PID=$!

# Start React development server in background
echo "🎨 Starting React frontend on http://localhost:5173..."
cd frontend

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo "Installing React dependencies..."
    npm install -q
fi

npm run dev &
REACT_PID=$!

cd ..

echo ""
echo "✅ Both servers are running!"
echo ""
echo "Frontend: http://localhost:5173"
echo "Backend:  http://localhost:8000"
echo "Admin:    http://localhost:8000/admin"
echo ""
echo "Press Ctrl+C to stop all servers..."
echo ""

# Wait for both processes
wait $DJANGO_PID $REACT_PID
