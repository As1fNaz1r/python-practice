#!/bin/bash

# Python Practice Dashboard - Quick Start Script
# Runs the FastAPI backend (port 8000) and Vite frontend (port 3333) together.

set -e

# Resolve the directory this script lives in, so it works from anywhere.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

BACKEND_PORT=8000
FRONTEND_PORT=3333
VENV_DIR="vev"

echo "🐍 Starting Python Practice Dashboard..."
echo ""

# --- Backend setup ---
if [ ! -d "backend/$VENV_DIR" ]; then
    echo "📦 Setting up backend virtual environment..."
    cd backend
    python3 -m venv "$VENV_DIR"
    source "$VENV_DIR/bin/activate"
    pip install -r requirements.txt
    deactivate
    cd ..
    echo "✅ Backend setup complete"
    echo ""
fi

# --- Frontend setup ---
if [ ! -d "frontend/node_modules" ]; then
    echo "📦 Installing frontend dependencies..."
    cd frontend
    npm install
    cd ..
    echo "✅ Frontend setup complete"
    echo ""
fi

# --- Cleanup on exit ---
BACKEND_PID=""
FRONTEND_PID=""
cleanup() {
    echo ""
    echo "🛑 Stopping servers..."
    [ -n "$BACKEND_PID" ] && kill "$BACKEND_PID" 2>/dev/null || true
    [ -n "$FRONTEND_PID" ] && kill "$FRONTEND_PID" 2>/dev/null || true
    exit 0
}
trap cleanup INT TERM

# --- Start backend ---
echo "🚀 Starting backend server on http://localhost:$BACKEND_PORT..."
cd backend
source "$VENV_DIR/bin/activate"
uvicorn main:app --reload --port "$BACKEND_PORT" &
BACKEND_PID=$!
cd ..

# Give the backend a moment to come up.
sleep 2

# --- Start frontend ---
echo "🚀 Starting frontend server on http://localhost:$FRONTEND_PORT..."
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo ""
echo "✨ Dashboard is running!"
echo "   Frontend: http://localhost:$FRONTEND_PORT"
echo "   Backend:  http://localhost:$BACKEND_PORT"
echo ""
echo "Press Ctrl+C to stop both servers"

# Wait for either process to exit.
wait
