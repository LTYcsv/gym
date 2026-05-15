<div align="center">

<img src="frontend/src/assets/hero.png" alt="Gym App" width="300"/>

# Gym App

**Telegram Mini App for structured workout tracking**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://python.org)
[![React](https://img.shields.io/badge/React-19-61DAFB?logo=react&logoColor=black)](https://react.dev)
[![TypeScript](https://img.shields.io/badge/TypeScript-6.0-3178C6?logo=typescript&logoColor=white)](https://typescriptlang.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)](https://postgresql.org)
[![Railway](https://img.shields.io/badge/Backend-Railway-0B0D0E?logo=railway)](https://railway.app)
[![Vercel](https://img.shields.io/badge/Frontend-Vercel-000000?logo=vercel)](https://vercel.com)

[**Live App**](https://gym-ruby-tau.vercel.app) · [**API Docs**](https://gym-production-4052.up.railway.app/docs)

</div>

---

## Overview

Gym App is a full-stack Telegram Mini App that helps users follow structured training programs, log workouts, and track progress over time.

Users open the app directly inside Telegram — no separate login required. Authentication is handled via **Telegram initData HMAC verification** with JWT tokens issued by the backend.

## Features

- **Training programs** — curated multi-day programs (V-Shape hypertrophy, Bodyweight Fundamentals) with 150+ exercises across 13 muscle groups
- **Weekly schedule** — cyclic day scheduling that adapts to the user's chosen training frequency (1–7 days/week)
- **Exercise swapping** — replace any exercise with an alternative from the same muscle group and program type
- **Weight tracking** — log weight per exercise; history is persisted across sessions
- **Stats & streaks** — workout calendar, current streak, personal records
- **Onboarding** — program selection flow with days-per-week goal setting

## Tech Stack

| Layer | Technologies |
|---|---|
| **Backend** | FastAPI 0.115, SQLAlchemy 2.0, Alembic, Pydantic v2 |
| **Database** | PostgreSQL 16, psycopg3 |
| **Auth** | Telegram initData HMAC + JWT (python-jose) |
| **Frontend** | React 19, TypeScript, Vite, React Router v7 |
| **Server state** | TanStack Query v5 |
| **Telegram SDK** | @twa-dev/sdk |
| **Deploy** | Railway (backend + DB), Vercel (frontend) |
| **Tests** | pytest (backend), vitest (frontend) |

## Architecture

```
Telegram Client
      │
      ▼
 Mini App (React + TypeScript)   ← hosted on Vercel
      │  Axios + TanStack Query
      ▼
 FastAPI REST API                ← hosted on Railway
      │  SQLAlchemy ORM
      ▼
 PostgreSQL 16                   ← Railway managed DB
```

Authentication flow:
1. Telegram passes `initData` to the Mini App
2. Frontend sends `initData` to `POST /api/auth/telegram`
3. Backend verifies HMAC signature using the bot token
4. Backend issues a JWT; all subsequent requests use `Authorization: Bearer <token>`

## API Overview

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/api/auth/telegram` | Exchange Telegram initData for JWT |
| `GET` | `/api/programs` | List all training programs |
| `GET` | `/api/programs/{slug}` | Program detail with workout days |
| `GET` | `/api/programs/{slug}/days/{id}` | Workout day with exercises |
| `POST` | `/api/sessions` | Log a completed workout |
| `GET` | `/api/stats` | Streak, calendar, records |
| `GET` | `/api/exercises/alternatives` | Swap suggestions by muscle group |
| `PUT` | `/api/weights/{exercise_id}` | Save exercise weight |
| `POST` | `/api/user-programs` | Enroll in a program |

Full interactive docs: [https://gym-production-4052.up.railway.app/docs](https://gym-production-4052.up.railway.app/docs)

## Project Structure

```
gym/
├── backend/
│   ├── app/
│   │   ├── auth/          # Telegram HMAC verification, JWT
│   │   ├── exercises/     # 150+ exercises, muscle groups
│   │   ├── programs/      # Training programs, workout days
│   │   ├── sessions/      # Workout session logging
│   │   ├── stats/         # Streak, calendar, records
│   │   ├── user_programs/ # Enrollment, days-per-week goal
│   │   ├── weights/       # Per-exercise weight history
│   │   ├── models.py      # SQLAlchemy models
│   │   └── main.py        # FastAPI app, CORS, middleware
│   ├── alembic/           # DB migrations
│   └── tests/             # pytest (20 tests)
└── frontend/
    └── src/
        ├── pages/         # Dashboard, Program, Library, Stats
        ├── components/    # BottomNav, sheets, exercise cards
        ├── api/           # Axios client, typed API functions
        ├── hooks/         # TanStack Query hooks
        └── types/         # TypeScript interfaces
```

## Local Setup

**Prerequisites:** Python 3.12+, Node.js 20+, PostgreSQL

```bash
git clone https://github.com/LTYcsv/gym.git
cd gym
```

**Backend**

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# Create a .env file (see backend/.env.example)
alembic upgrade head
python -m app.seed      # seed 150+ exercises and programs

uvicorn app.main:app --reload
# → http://localhost:8000
```

**Frontend**

```bash
cd frontend
npm install
npm run dev
# → http://localhost:5174
# Vite proxies /api → localhost:8000 automatically
```

## Running Tests

```bash
# Backend (20 tests: streak logic, utilities)
cd backend && python -m pytest tests/ -v

# Frontend (8 tests: calendar component)
cd frontend && npm test
```

## Deployment

| Service | Platform | Config |
|---|---|---|
| Backend API + DB | Railway | `backend/railway.toml` |
| Frontend | Vercel | `frontend/vercel.json` |

Both services use HTTPS out of the box. Environment variables are set in each platform's dashboard.
