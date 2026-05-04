import logging
import time
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.config import settings
from app.programs.router import router as programs_router
from app.exercises.router import router as exercises_router
from app.auth.router import router as auth_router
from app.sessions.router import router as sessions_router
from app.weights.router import router as weights_router
from app.user_programs.router import router as user_programs_router
from app.stats.router import router as stats_router
from app.webhook import router as webhook_router

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s: %(message)s",
    datefmt="%Y-%m-%dT%H:%M:%S",
)

logger = logging.getLogger("app")

app = FastAPI(title="Gym API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "X-Timezone"],
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    ms = (time.perf_counter() - start) * 1000
    logger.info("%s %s %d %.0fms", request.method, request.url.path, response.status_code, ms)
    return response


@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("Unhandled error %s %s", request.method, request.url.path)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})

app.include_router(auth_router, prefix="/api")
app.include_router(programs_router, prefix="/api")
app.include_router(exercises_router, prefix="/api")
app.include_router(sessions_router, prefix="/api")
app.include_router(weights_router, prefix="/api")
app.include_router(user_programs_router, prefix="/api")
app.include_router(stats_router, prefix="/api")
app.include_router(webhook_router, prefix="/api")


@app.get("/api/health")
def health():
    return {"status": "ok"}
