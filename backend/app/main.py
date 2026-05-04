from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.programs.router import router as programs_router
from app.exercises.router import router as exercises_router
from app.auth.router import router as auth_router
from app.sessions.router import router as sessions_router
from app.weights.router import router as weights_router
from app.user_programs.router import router as user_programs_router
from app.stats.router import router as stats_router

app = FastAPI(title="Gym API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api")
app.include_router(programs_router, prefix="/api")
app.include_router(exercises_router, prefix="/api")
app.include_router(sessions_router, prefix="/api")
app.include_router(weights_router, prefix="/api")
app.include_router(user_programs_router, prefix="/api")
app.include_router(stats_router, prefix="/api")


@app.get("/api/health")
def health():
    return {"status": "ok"}
