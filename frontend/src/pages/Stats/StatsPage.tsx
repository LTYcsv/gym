import { useQuery } from '@tanstack/react-query'
import { getStats } from '../../api/stats'
import { ErrorRetry } from '../../components/ErrorRetry'

const MUSCLE_LABELS: Record<string, string> = {
  back: 'Спина', chest: 'Грудь', shoulders: 'Плечи',
  biceps: 'Бицепс', triceps: 'Трицепс', quadriceps: 'Квадрицепс',
  hamstrings: 'Бицепс бедра', calves: 'Икры', glutes: 'Ягодицы',
  core: 'Пресс', lower_back: 'Поясница', traps: 'Трапеции', forearms: 'Предплечья',
}

const MUSCLE_COLORS: Record<string, string> = {
  back: '#4d9fff', chest: '#ff6b35', shoulders: '#d4a0ff',
  biceps: '#5ef29a', triceps: '#ffd166', quadriceps: '#ff6b35',
  hamstrings: '#ff9a3c', calves: '#5ef29a', glutes: '#d4a0ff',
  core: '#4d9fff', lower_back: '#ff6b35', traps: '#5ef29a', forearms: '#ffd166',
}

function Section({ title, children }: { title: string; children: React.ReactNode }) {
  return (
    <div className="section">
      <p className="section-title">{title}</p>
      {children}
    </div>
  )
}

function Card({ children }: { children: React.ReactNode }) {
  return (
    <div className="card">
      {children}
    </div>
  )
}

function WeeklyProgress({ done, planned }: { done: number; planned: number }) {
  const pct = planned ? Math.min(done / planned, 1) : 0
  return (
    <Card>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-end', marginBottom: 14 }}>
        <div>
          <p style={{ fontSize: 11, color: 'var(--muted)', fontWeight: 600, marginBottom: 4 }}>Выполнено</p>
          <p className="heading" style={{ fontSize: 48, lineHeight: 1, color: 'var(--accent)' }}>
            {done}<span style={{ fontSize: 24, color: 'var(--muted)' }}>/{planned || '—'}</span>
          </p>
        </div>
        <p style={{ fontSize: 13, color: 'var(--muted)', fontWeight: 600 }}>
          {planned ? `${Math.round(pct * 100)}%` : ''}
        </p>
      </div>
      <div style={{ height: 6, background: 'var(--surface2)', borderRadius: 3, overflow: 'hidden' }}>
        <div style={{ height: '100%', width: `${pct * 100}%`, background: 'var(--accent)', borderRadius: 3, transition: 'width 0.6s ease' }} />
      </div>
    </Card>
  )
}

const WEEK_DAYS = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']

function MonthCalendar({ dates }: { dates: string[] }) {
  const dateSet = new Set(dates)
  const today = new Date()
  const todayStr = today.toLocaleDateString('sv')

  // Monday of current week (ISO: Mon=0 … Sun=6)
  const isoDay = (today.getDay() + 6) % 7
  const monday = new Date(today)
  monday.setDate(today.getDate() - isoDay)

  // Go back 4 more weeks → 5 full weeks = 35 cells
  const start = new Date(monday)
  start.setDate(monday.getDate() - 28)

  const cutoff = new Date(today)
  cutoff.setDate(today.getDate() - 29)

  const cells: { date: string; inWindow: boolean }[] = []
  for (let i = 0; i < 35; i++) {
    const d = new Date(start)
    d.setDate(start.getDate() + i)
    const dateStr = d.toLocaleDateString('sv')
    cells.push({ date: dateStr, inWindow: d >= cutoff && d <= today })
  }

  return (
    <Card>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)', gap: 4, marginBottom: 6 }}>
        {WEEK_DAYS.map(d => (
          <p key={d} style={{ fontSize: 10, color: 'var(--muted)', fontWeight: 600, textAlign: 'center', margin: 0 }}>
            {d}
          </p>
        ))}
      </div>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(7, 1fr)', gap: 4 }}>
        {cells.map(({ date, inWindow }) => {
          const worked = dateSet.has(date)
          const isToday = date === todayStr
          return (
            <div key={date} style={{
              aspectRatio: '1',
              borderRadius: 4,
              background: !inWindow ? 'transparent' : worked ? 'var(--accent)' : 'var(--surface2)',
              border: isToday ? '1px solid var(--accent)' : '1px solid transparent',
              opacity: !inWindow ? 0 : worked ? 1 : 0.35,
            }} />
          )
        })}
      </div>
      <p style={{ fontSize: 11, color: 'var(--muted)', marginTop: 10, textAlign: 'right' }}>
        {dates.length} тренировок за 30 дней
      </p>
    </Card>
  )
}

function StreakCards({ weekStreak, workoutStreak }: { weekStreak: number; workoutStreak: number }) {
  return (
    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
      <Card>
        <p style={{ fontSize: 11, color: 'var(--muted)', fontWeight: 600, marginBottom: 6 }}>Недель подряд</p>
        <p className="heading" style={{ fontSize: 40, lineHeight: 1, color: '#ffd166' }}>
          {weekStreak}
        </p>
        <p style={{ fontSize: 11, color: 'var(--muted)', marginTop: 4 }}>🔥 серия</p>
      </Card>
      <Card>
        <p style={{ fontSize: 11, color: 'var(--muted)', fontWeight: 600, marginBottom: 6 }}>Тренировок подряд</p>
        <p className="heading" style={{ fontSize: 40, lineHeight: 1, color: '#5ef29a' }}>
          {workoutStreak}
        </p>
        <p style={{ fontSize: 11, color: 'var(--muted)', marginTop: 4 }}>⚡ интервал ≤7 дней</p>
      </Card>
    </div>
  )
}

function MuscleGroups({ groups }: { groups: { muscle_group: string; count: number }[] }) {
  if (!groups.length) return <Card><p style={{ color: 'var(--muted)', fontSize: 13 }}>Пока нет тренировок на этой неделе</p></Card>
  return (
    <Card>
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
        {groups.map(g => (
          <span key={g.muscle_group} style={{
            fontSize: 12, fontWeight: 700, borderRadius: 20, padding: '4px 12px',
            background: `${MUSCLE_COLORS[g.muscle_group] ?? 'var(--muted)'}22`,
            color: MUSCLE_COLORS[g.muscle_group] ?? 'var(--muted)',
            border: `1px solid ${MUSCLE_COLORS[g.muscle_group] ?? 'var(--muted)'}44`,
          }}>
            {MUSCLE_LABELS[g.muscle_group] ?? g.muscle_group}
          </span>
        ))}
      </div>
    </Card>
  )
}

function Records({ records }: { records: { exercise_name: string; weight_kg: number; achieved_at: string }[] }) {
  if (!records.length) return <Card><p style={{ color: 'var(--muted)', fontSize: 13 }}>Рекорды появятся после первой тренировки с весами</p></Card>
  return (
    <Card>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
        {records.map((r, i) => (
          <div key={i} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div style={{ flex: 1, minWidth: 0 }}>
              <p style={{ fontSize: 14, fontWeight: 700, color: 'var(--text)', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                {r.exercise_name}
              </p>
              <p style={{ fontSize: 11, color: 'var(--muted)', marginTop: 2 }}>
                {new Date(r.achieved_at).toLocaleDateString('ru', { day: 'numeric', month: 'short' })}
              </p>
            </div>
            <div style={{ textAlign: 'right', flexShrink: 0, marginLeft: 12 }}>
              <span className="heading" style={{ fontSize: 22, color: '#ffd166' }}>
                {r.weight_kg}
              </span>
              <span style={{ fontSize: 12, color: 'var(--muted)', marginLeft: 3 }}>кг</span>
            </div>
          </div>
        ))}
      </div>
    </Card>
  )
}

export default function StatsPage() {
  const { data, isLoading, isError, refetch } = useQuery({
    queryKey: ['stats'],
    queryFn: getStats,
  })

  return (
    <div className="page-padded">
      <div style={{ marginBottom: 32 }}>
        <p className="label" style={{ letterSpacing: '0.14em', marginBottom: 8 }}>
          Твой прогресс
        </p>
        <h1 className="heading" style={{ fontSize: 48, letterSpacing: '0.03em', lineHeight: 1 }}>
          STATS
        </h1>
      </div>

      {isLoading && <p style={{ color: 'var(--muted)', fontSize: 13 }}>Загрузка...</p>}
      {isError && <ErrorRetry onRetry={() => refetch()} />}

      {data && (
        <>
          <Section title="Эта неделя">
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
              <WeeklyProgress done={data.weekly_done} planned={data.weekly_planned} />
              <MuscleGroups groups={data.weekly_muscle_groups} />
            </div>
          </Section>

          <Section title="Серия">
            <StreakCards weekStreak={data.week_streak} workoutStreak={data.workout_streak} />
          </Section>

          <Section title="Последние 30 дней">
            <MonthCalendar dates={data.workout_dates} />
          </Section>

          <Section title="Личные рекорды">
            <Records records={data.records} />
          </Section>
        </>
      )}
    </div>
  )
}
