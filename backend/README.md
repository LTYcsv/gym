# Backend — Gym App

FastAPI REST API with PostgreSQL, deployed to Railway.

## Stack

| | |
|---|---|
| Framework | FastAPI 0.115 |
| ORM | SQLAlchemy 2.0 (sync) |
| Migrations | Alembic |
| Database | PostgreSQL 16 |
| Driver | psycopg3 |
| Validation | Pydantic v2 |
| Auth | Telegram initData HMAC + JWT (python-jose) |
| Tests | pytest |

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env

alembic upgrade head
python -m app.seed     # seed 150+ exercises and 2 programs

uvicorn app.main:app --reload
# → http://localhost:8000
# → http://localhost:8000/docs  (Swagger UI)
```

## Environment Variables

```
DATABASE_URL=postgresql://localhost:5432/gym
SECRET_KEY=your-secret-key
TELEGRAM_BOT_TOKEN=your-bot-token
CORS_ORIGINS=http://localhost:5174
```

## Structure

```
app/
├── auth/           # Telegram initData HMAC verification, JWT issue
├── exercises/      # Exercise CRUD, alternatives endpoint
├── programs/       # Programs, workout days, workout exercises
├── sessions/       # Workout session logging
├── stats/          # Streak calculation, calendar, personal records
├── user_programs/  # Enrollment, days-per-week goal
├── weights/        # Per-exercise weight history
├── models.py       # SQLAlchemy declarative models
├── database.py     # Engine, session factory
├── config.py       # Pydantic Settings
├── seed.py         # Idempotent DB seeder (checks by slug)
└── main.py         # App factory, CORS, logging middleware
```

## Key Endpoints

| Method | Path | Description |
|---|---|---|
| `POST` | `/api/auth/telegram` | Verify Telegram initData, issue JWT |
| `GET` | `/api/programs` | List programs |
| `GET` | `/api/programs/{slug}/days/{id}` | Workout day with exercises |
| `POST` | `/api/sessions` | Log completed workout |
| `GET` | `/api/stats` | Streak, calendar, personal records |
| `GET` | `/api/exercises/alternatives` | Swap by muscle group + program type |
| `PUT` | `/api/weights/{exercise_id}` | Save weight (appends to history) |
| `GET` | `/api/health` | Health check |

## Tests

```bash
python -m pytest tests/ -v
```

20 tests covering streak logic and utility functions.

## Migrations

```bash
alembic upgrade head          # apply migrations
alembic revision --autogenerate -m "description"  # new migration
```
