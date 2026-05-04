import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { getPrograms } from '../../api/programs'
import type { Program } from '../../types'

const TYPE_META: Record<string, { label: string; color: string }> = {
  hypertrophy:  { label: 'Гипертрофия', color: '#4d9fff' },
  strength:     { label: 'Сила',        color: '#ff6b35' },
  cardio:       { label: 'Кардио',      color: '#5ef29a' },
  hiit:         { label: 'HIIT',        color: '#ff6b35' },
  calisthenics: { label: 'Калистеника', color: '#d4a0ff' },
}

const DIFFICULTY_LABEL: Record<string, string> = {
  beginner: 'Новичок', intermediate: 'Средний', advanced: 'Продвинутый',
}

function ProgressRing({ done, total }: { done: number; total: number }) {
  const pct = total ? Math.min(done / total, 1) : 0
  const r = 18, stroke = 3
  const circ = 2 * Math.PI * r
  return (
    <div style={{ position: 'relative', width: 44, height: 44, flexShrink: 0 }}>
      <svg width={44} height={44} style={{ transform: 'rotate(-90deg)' }}>
        <circle cx={22} cy={22} r={r} fill="none" stroke="var(--surface2)" strokeWidth={stroke} />
        <circle cx={22} cy={22} r={r} fill="none" stroke="#4d9fff"
          strokeWidth={stroke} strokeDasharray={circ}
          strokeDashoffset={circ * (1 - pct)} strokeLinecap="round"
          style={{ transition: 'stroke-dashoffset 0.4s ease' }} />
      </svg>
      <span style={{
        position: 'absolute', inset: 0, display: 'flex', alignItems: 'center',
        justifyContent: 'center', fontSize: 11, fontWeight: 700, color: 'var(--text)',
      }}>
        {done}/{total}
      </span>
    </div>
  )
}

function ProgramCard({ p }: { p: Program }) {
  const meta = TYPE_META[p.type] ?? { label: p.type, color: 'var(--muted)' }
  return (
    <Link to={`/programs/${p.slug}`} style={{ textDecoration: 'none' }}>
      <div style={{
        background: 'var(--surface)', border: '1px solid var(--border)',
        borderRadius: 16, padding: '18px 20px', cursor: 'pointer',
        borderLeft: `3px solid ${meta.color}`,
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 12 }}>
          <div style={{ flex: 1, minWidth: 0 }}>
            <p style={{ fontSize: 11, fontWeight: 700, letterSpacing: '0.08em', textTransform: 'uppercase', color: meta.color, marginBottom: 4 }}>
              {meta.label}
            </p>
            <h2 style={{ fontSize: 20, fontWeight: 700, color: 'var(--text)', marginBottom: 4 }}>{p.name}</h2>
            {p.goal && <p style={{ fontSize: 13, color: 'var(--muted)' }}>{p.goal}</p>}
            <div style={{ display: 'flex', gap: 8, marginTop: 10, flexWrap: 'wrap' }}>
              {p.days_per_week && (
                <span style={{ fontSize: 11, background: 'var(--surface2)', border: '1px solid var(--border)', borderRadius: 20, padding: '3px 10px', display: 'flex', gap: 4, alignItems: 'center' }}>
                  <span style={{ color: 'var(--muted)', fontWeight: 500 }}>рек.</span>
                  <span style={{ color: 'var(--text)', fontWeight: 700 }}>{p.days_per_week}дн/нед</span>
                </span>
              )}
              {p.difficulty && (
                <span style={{ fontSize: 11, background: 'var(--surface2)', border: '1px solid var(--border)', borderRadius: 20, padding: '3px 10px', display: 'flex', gap: 4, alignItems: 'center' }}>
                  <span style={{ color: 'var(--muted)', fontWeight: 500 }}>ур.</span>
                  <span style={{ color: 'var(--text)', fontWeight: 700 }}>{DIFFICULTY_LABEL[p.difficulty] ?? p.difficulty}</span>
                </span>
              )}
            </div>
          </div>
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4 }}>
            {p.user_days_per_week != null ? (
              <>
                <ProgressRing done={p.weekly_sessions} total={p.user_days_per_week} />
                <span style={{ fontSize: 9, fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.08em', color: 'var(--muted)' }}>неделя</span>
              </>
            ) : (
              <div style={{
                width: 44, height: 44, borderRadius: '50%',
                border: '2px dashed var(--border)',
                display: 'flex', alignItems: 'center', justifyContent: 'center',
              }}>
                <span style={{ fontSize: 9, fontWeight: 800, letterSpacing: '0.05em', color: 'var(--accent)' }}>NEW</span>
              </div>
            )}
          </div>
        </div>
      </div>
    </Link>
  )
}

export default function Dashboard() {
  const { data: programs, isLoading } = useQuery({
    queryKey: ['programs'],
    queryFn: getPrograms,
  })

  return (
    <div style={{ minHeight: '100dvh', padding: '48px 20px var(--nav-height)' }}>
      <div style={{ marginBottom: 32 }}>
        <p style={{ fontSize: 11, fontWeight: 600, letterSpacing: '0.14em', textTransform: 'uppercase', color: 'var(--muted)', marginBottom: 8 }}>
          Программы тренировок
        </p>
        <h1 style={{ fontFamily: 'Bebas Neue, sans-serif', fontSize: 48, letterSpacing: '0.03em', lineHeight: 1 }}>
          GYM <span style={{ color: 'var(--accent-a)' }}>DASHBOARD</span>
        </h1>
      </div>

      {isLoading && <p style={{ color: 'var(--muted)', fontSize: 13 }}>Загрузка...</p>}

      <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
        {programs?.map(p => <ProgramCard key={p.id} p={p} />)}
      </div>
    </div>
  )
}
