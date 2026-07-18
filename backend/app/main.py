from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.search import router as search_router

app = FastAPI(title="AI Dataset & GitHub Recommender")

# Allow the frontend (running on a different port) to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js default dev port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_router, prefix="/api")


@app.get("/")
def health_check():
    return {"status": "ok", "message": "Backend is running"}