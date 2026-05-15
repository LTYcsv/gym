# Frontend — Gym App

React 19 + TypeScript Single Page Application, deployed to Vercel as a Telegram Mini App.

## Stack

| | |
|---|---|
| Framework | React 19 + TypeScript |
| Build tool | Vite 8 |
| Routing | React Router DOM v7 |
| Server state | TanStack Query v5 |
| HTTP | Axios |
| Telegram SDK | @twa-dev/sdk |
| Tests | vitest |

## Pages

| Route | Page | Description |
|---|---|---|
| `/` | Dashboard | Active program overview, weekly schedule, progress ring |
| `/programs/:slug` | Program | Workout days list |
| `/programs/:slug/days/:id` | WorkoutDay | Exercise list with sets/reps, weight input, swap |
| `/library` | Library | Browse 150+ exercises by muscle group |
| `/stats` | Stats | Streak, workout calendar, personal records |

## Setup

```bash
npm install
npm run dev   # http://localhost:5174
```

Vite proxies `/api → http://localhost:8000` automatically in development, so no env file is needed locally.

## Environment Variables

In production (Vercel), set:

```
VITE_API_URL=https://your-backend.up.railway.app
```

## Scripts

```bash
npm run dev      # dev server
npm run build    # production build
npm run test     # vitest
npm run lint     # eslint
```

## Structure

```
src/
├── api/          # Axios instance, typed API functions
├── components/   # Shared UI: BottomNav, sheets, cards
├── hooks/        # TanStack Query hooks (useProgram, useStats, …)
├── pages/        # Route-level components
├── types/        # TypeScript interfaces mirroring backend schemas
└── utils/        # Date helpers, formatting
```
