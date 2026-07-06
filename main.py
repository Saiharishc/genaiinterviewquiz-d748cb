from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI(title="GenAIInterviewQuiz")

@app.get('/api/items')
async def list_items():
    return []

@app.get('/api/quizzes/topics')
async def get_quiz_topics():
    return {"topics": ["Python", "JavaScript", "React", "SQL"]}

@app.get('/api/quizzes/search')
async def search_quizzes(query: str):
    # This is a placeholder, in a real app you would search your quiz data
    return {"results": [{"id": 1, "title": "Python Basics", "topic": "Python"}, {"id": 2, "title": "JavaScript Fundamentals", "topic": "JavaScript"}]}

@app.get('/api/quizzes/topic/{topic_name}')
async def get_quizzes_by_topic(topic_name: str):
    # This is a placeholder, in a real app you would filter quizzes by topic
    return {"quizzes": [{"id": 1, "title": f"{topic_name} Quiz 1"}, {"id": 2, "title": f"{topic_name} Quiz 2"}]}

@app.get('/api/quizzes/quiz/{quiz_id}')
async def get_quiz_by_id(quiz_id: int):
    # This is a placeholder, in a real app you would fetch a specific quiz
    return {"quiz": {"id": quiz_id, "title": f"Quiz {quiz_id}", "questions": [{"question": "What is...?", "options": ["A", "B", "C"], "answer": "A"}]}}

BUILD_DIR = os.path.join(os.path.dirname(__file__), 'frontend', 'build')
if os.path.isdir(BUILD_DIR):
    app.mount('/static', StaticFiles(directory=os.path.join(BUILD_DIR, 'static')), name='static')

    @app.get('/{full_path:path}')
    async def serve_frontend(full_path: str):
        # Check if the requested path corresponds to a static file
        if os.path.exists(os.path.join(BUILD_DIR, full_path)) and not os.path.isdir(os.path.join(BUILD_DIR, full_path)):
            return FileResponse(os.path.join(BUILD_DIR, full_path))
        # Otherwise, serve the index.html for client-side routing
        return FileResponse(os.path.join(BUILD_DIR, 'index.html'))
