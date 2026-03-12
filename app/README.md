# Python Practice Dashboard

An interactive web dashboard to browse and review your Python learning materials.

## Features

- 📁 Browse Python files organized by topics
- 🔍 Search files by name or content
- 📊 View statistics about your learning progress
- 🎨 Modern dark-themed UI with syntax highlighting
- 📱 Responsive design for all devices

## Tech Stack

### Backend
- FastAPI - Modern Python web framework
- Uvicorn - ASGI server

### Frontend
- React 18 - UI library
- Vite - Build tool
- Prism.js - Syntax highlighting

## Getting Started

### Backend Setup

1. Navigate to the backend directory:
```bash
cd app/backend
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the server:
```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd app/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## API Endpoints

- `GET /` - Root endpoint
- `GET /api/topics` - Get all topics with folder structure
- `GET /api/file/{file_path}` - Get content of a specific file
- `GET /api/stats` - Get practice statistics
- `GET /api/search?q={query}` - Search files by name or content

## Project Structure

```
app/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── venv/               # Virtual environment
└── frontend/
    ├── src/
    │   ├── App.jsx         # Main React component
    │   ├── App.css         # Styles
    │   ├── main.jsx        # Entry point
    │   └── index.css       # Global styles
    ├── index.html          # HTML template
    ├── package.json        # Node dependencies
    └── vite.config.js      # Vite configuration
```

## Updates in v2.0

- ✨ Added search functionality to find files by name or content
- 📈 Enhanced statistics with line count tracking
- 🔧 Updated to latest dependencies (FastAPI 0.115, React 18.3, Vite 6)
- 🛡️ Improved error handling with proper HTTP exceptions
- 📝 Better logging for debugging
- 🎯 More detailed file metadata (size, line count)

## Development

To build the frontend for production:
```bash
cd app/frontend
npm run build
```

To preview the production build:
```bash
npm run preview
```
