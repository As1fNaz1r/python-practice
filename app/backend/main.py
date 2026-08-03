from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
from typing import List, Dict, Any
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Python Practice Learning Dashboard",
    version="2.0.0",
    description="Interactive dashboard for Python learning materials"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "http://localhost:3333"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).parent.parent.parent

@app.get("/")
def root():
    return {"message": "Python Practice API"}

def build_folder_tree(dir_path, base_path):
    """Recursively build folder structure"""
    items = []
    for item_path in sorted(dir_path.iterdir()):
        if item_path.name.startswith('.'):
            continue
        if item_path.is_file() and item_path.suffix in ['.py', '.md']:
            rel_path = item_path.relative_to(base_path)
            items.append({
                "name": item_path.name,
                "path": str(rel_path),
                "type": "file",
                "language": item_path.suffix[1:]
            })
        elif item_path.is_dir():
            children = build_folder_tree(item_path, base_path)
            if children:
                items.append({
                    "name": item_path.name,
                    "type": "folder",
                    "children": children
                })
    return items

@app.get("/api/topics")
def get_topics():
    """Get all practice topics with folder structure"""
    topics = []
    
    topic_dirs = {
        "built-in-functions": "Built-in Functions (range, map, filter, enumerate, zip)",
        "clean-architecture": "Clean Architecture",
        "concurrency": "Concurrency (asyncio, threading, multiprocessing)",
        "data-structures": "Data Structures (lists, dicts, sets, comprehensions)",
        "debugging": "Debugging & Logging",
        "dunder-methods": "Dunder Methods (magic methods)",
        "error-handling": "Error Handling",
        "file-operation": "File Operations (reading, writing)",
        "functions": "Functions (decorators, closures, passing)",
        "loops-conditionals": "Loops & Conditionals (if/else, for/while, break/continue)",
        "main-import-main": "if __name__ == '__main__'",
        "modules-imports": "Modules & Imports (packages, relative/absolute imports)",
        "oop-basics": "OOP Basics (classes, inheritance, methods)",
        "string-manipulation": "String Manipulation",
        "testing": "Testing (unittest, pytest)"
    }
    
    for dir_name, display_name in topic_dirs.items():
        topic_path = BASE_DIR / dir_name
        if topic_path.exists():
            children = build_folder_tree(topic_path, BASE_DIR)
            
            doc_file = topic_path / "docs.txt"
            doc_content = ""
            if doc_file.exists():
                doc_content = doc_file.read_text()
            
            topics.append({
                "id": dir_name,
                "name": display_name,
                "structure": children,
                "docs": doc_content
            })
    
    return topics

@app.get("/api/file/{file_path:path}")
def get_file_content(file_path: str):
    """Get content of a specific file"""
    full_path = BASE_DIR / file_path
    
    if not full_path.exists() or not full_path.is_file():
        raise HTTPException(status_code=404, detail="File not found")
    
    try:
        content = full_path.read_text(encoding='utf-8')
        return {
            "path": file_path,
            "name": full_path.name,
            "content": content,
            "language": full_path.suffix[1:] if full_path.suffix else "text",
            "size": len(content),
            "lines": content.count('\n') + 1
        }
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")

@app.get("/api/stats")
def get_stats():
    """Get practice statistics"""
    stats = {
        "total_files": 0,
        "by_type": {},
        "topics": [],
        "total_lines": 0
    }
    
    topic_list = [
        "built-in-functions", "clean-architecture", "concurrency", "data-structures",
        "debugging", "dunder-methods", "error-handling", "file-operation",
        "functions", "loops-conditionals", "main-import-main", "modules-imports",
        "oop-basics", "string-manipulation", "testing"
    ]
    
    for topic_dir in topic_list:
        topic_path = BASE_DIR / topic_dir
        if topic_path.exists():
            py_files = list(topic_path.rglob("*.py"))
            md_files = list(topic_path.rglob("*.md"))
            
            topic_lines = 0
            for f in py_files + md_files:
                try:
                    topic_lines += len(f.read_text(encoding='utf-8').splitlines())
                except:
                    pass
            
            stats["topics"].append({
                "name": topic_dir,
                "python_files": len(py_files),
                "markdown_files": len(md_files),
                "lines": topic_lines
            })
            
            stats["total_files"] += len(py_files) + len(md_files)
            stats["total_lines"] += topic_lines
            stats["by_type"]["python"] = stats["by_type"].get("python", 0) + len(py_files)
            stats["by_type"]["markdown"] = stats["by_type"].get("markdown", 0) + len(md_files)
    
    return stats

@app.get("/api/search")
def search_files(q: str):
    """Search for files by name or content"""
    if not q or len(q) < 2:
        return {"results": []}
    
    results = []
    query_lower = q.lower()
    
    for py_file in BASE_DIR.rglob("*.py"):
        if py_file.name.startswith('.'):
            continue
        
        rel_path = py_file.relative_to(BASE_DIR)
        
        # Search in filename
        if query_lower in py_file.name.lower():
            results.append({
                "path": str(rel_path),
                "name": py_file.name,
                "type": "filename",
                "language": "py"
            })
            continue
        
        # Search in content
        try:
            content = py_file.read_text(encoding='utf-8')
            if query_lower in content.lower():
                # Find matching line
                for i, line in enumerate(content.splitlines(), 1):
                    if query_lower in line.lower():
                        results.append({
                            "path": str(rel_path),
                            "name": py_file.name,
                            "type": "content",
                            "language": "py",
                            "line": i,
                            "preview": line.strip()[:100]
                        })
                        break
        except:
            pass
        
        if len(results) >= 50:
            break
    
    return {"results": results, "count": len(results)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)