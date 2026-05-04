import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import { Link } from 'react-router-dom'
import { getExercises, getExercisePrograms } from '../../api/exercises'
import type { MuscleGroup, ProgramType } from '../../types'
import WorkoutTypeFilter from '../../components/WorkoutTypeFilter'

const MUSCLE_GROUPS: { key: MuscleGroup; label: string; icon: string }[] = [
  { key: 'back',        label: 'Спина',        icon: '🔙' },
  { key: 'chest',       label: 'Грудь',        icon: '💪' },
  { key: 'shoulders',   label: 'Плечи',        icon: '🔺' },
  { key: 'biceps',      label: 'Бицепс',       icon: '✊' },
  { key: 'triceps',     label: 'Трицепс',      icon: '✊' },
  { key: 'quadriceps',  label: 'Квадрицепс',   icon: '🦵' },
  { key: 'hamstrings',  label: 'Бицепс бедра', icon: '🦵' },
  { key: 'glutes',      label: 'Ягодицы',      icon: '🍑' },
  { key: 'core',        label: 'Пресс',        icon: '⚡' },
  { key: 'lower_back',  label: 'Поясница',     icon: '⬇️' },
  { key: 'calves',      label: 'Икры',         icon: '🦵' },
  { key: 'traps',       label: 'Трапеции',     icon: '🏔️' },
  { key: 'forearms',    label: 'Предплечья',   icon: '💪' },
]

const TYPE_META: Record<string, { label: string; color: string }> = {
  strength:     { label: 'Сила',        color: '#ff6b35' },
  hypertrophy:  { label: 'Масса',       color: '#4d9fff' },
  cardio:       { label: 'Кардио',      color: '#5ef29a' },
  hiit:         { label: 'HIIT',        color: '#ffd166' },
  calisthenics: { label: 'Калистеника', color: '#d4a0ff' },
}

const EQUIPMENT_LABEL: Record<string, string> = {
  barbell:    'Штанга',
  dumbbells:  'Гантели',
  cable:      'Блок',
  machine:    'Тренажёр',
  bodyweight: 'Своё тело',
}


function ExercisePrograms({ exerciseId }: { exerciseId: string }) {
  const { data } = useQuery({
    queryKey: ['exercisePrograms', exerciseId],
    queryFn: () => getExercisePrograms(exerciseId),
  })
  if (!data?.length) return null
  return (
    <div style={{ marginTop: 10, display: 'flex', flexWrap: 'wrap', gap: 6 }}>
      {data.map((p, i) => (
        <Link key={i} to={`/programs/${p.program_slug}`}
          className="tag" style={{ textDecoration: 'none', color: '#d4a0ff', border: '1px solid rgba(212,160,255,0.25)', background: 'rgba(212,160,255,0.08)' }}>
          {p.program_name} · {p.day_label}
        </Link>
      ))}
    </div>
  )
}

export default function LibraryPage() {
  const [activeGroup, setActiveGroup] = useState<MuscleGroup>('back')
  const [activeType, setActiveType] = useState<ProgramType | null>(null)
  const [expandedId, setExpandedId] = useState<string | null>(null)

  const { data: exercises } = useQuery({
    queryKey: ['exercises', activeGroup, activeType],
    queryFn: () => getExercises({ muscle_group: activeGroup, type: activeType ?? undefined }),
  })

  const icon = MUSCLE_GROUPS.find(g => g.key === activeGroup)?.icon ?? '💪'

  return (
    <div className="page">
      <div style={{ padding: '48px 20px 8px' }}>
        <h1 className="heading" style={{ fontSize: 40, color: 'var(--accent-d)' }}>База упражнений</h1>
        <p style={{ fontSize: 13, color: 'var(--muted)', marginTop: 4 }}>Фильтр по мышцам и типу программы</p>
      </div>

      {/* Muscle group tabs */}
      <div style={{ display: 'flex', gap: 8, padding: '12px 20px', overflowX: 'auto', scrollbarWidth: 'none' }}>
        {MUSCLE_GROUPS.map(g => (
          <button key={g.key} onClick={() => setActiveGroup(g.key)} style={{
            flexShrink: 0, padding: '7px 14px', borderRadius: 20, fontSize: 12, fontWeight: 700,
            letterSpacing: '0.05em', cursor: 'pointer',
            background: activeGroup === g.key ? 'var(--accent-d)' : 'var(--surface)',
            color: activeGroup === g.key ? '#000' : 'var(--muted)',
            border: `1px solid ${activeGroup === g.key ? 'var(--accent-d)' : 'var(--border)'}`,
          }}>
            {g.icon} {g.label}
          </button>
        ))}
      </div>

      {/* Program type filter */}
      <WorkoutTypeFilter selected={activeType} onSelect={setActiveType} />

      {/* Count */}
      <div style={{ padding: '0 20px 8px' }}>
        <p style={{ fontSize: 11, color: 'var(--muted)', fontWeight: 600 }}>
          {exercises?.length ?? 0} упражнений
        </p>
      </div>

      {/* Exercise list */}
      <div style={{ padding: '0 20px', display: 'flex', flexDirection: 'column', gap: 8 }}>
        {exercises?.map(ex => (
          <div key={ex.id} style={{ background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: 14, overflow: 'hidden' }}>
            <div style={{ padding: '14px 16px', display: 'flex', alignItems: 'center', gap: 12, cursor: 'pointer' }}
              onClick={() => setExpandedId(expandedId === ex.id ? null : ex.id)}>
              <div style={{ width: 36, height: 36, borderRadius: 10, background: 'rgba(212,160,255,0.1)', border: '1px solid rgba(212,160,255,0.2)', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 16, flexShrink: 0 }}>
                {icon}
              </div>
              <div style={{ flex: 1 }}>
                <p style={{ fontSize: 14, fontWeight: 700 }}>{ex.name}</p>
                <div style={{ display: 'flex', gap: 4, marginTop: 4, flexWrap: 'wrap' }}>
                  {ex.types.map(t => {
                    const meta = TYPE_META[t]
                    return (
                      <span key={t} style={{ fontSize: 10, fontWeight: 700, padding: '2px 6px', borderRadius: 5, color: meta?.color ?? 'var(--muted)', background: `${meta?.color ?? '#fff'}18`, border: `1px solid ${meta?.color ?? '#fff'}33` }}>
                        {meta?.label ?? t}
                      </span>
                    )
                  })}
                  {ex.equipment.map(eq => (
                    <span key={eq} style={{ fontSize: 10, fontWeight: 600, padding: '2px 6px', borderRadius: 5, color: 'var(--muted)', border: '1px solid var(--border)' }}>
                      {EQUIPMENT_LABEL[eq] ?? eq}
                    </span>
                  ))}
                </div>
              </div>
              <span style={{ fontSize: 16, color: 'var(--muted)', transform: expandedId === ex.id ? 'rotate(90deg)' : 'none', transition: 'transform 0.2s', flexShrink: 0 }}>›</span>
            </div>

            {expandedId === ex.id && (
              <div style={{ borderTop: '1px solid var(--border)', padding: '14px 16px' }}>
                {ex.technique && (
                  <p style={{ fontSize: 13, lineHeight: 1.7, color: '#b0b0b0', marginBottom: 12 }}>{ex.technique}</p>
                )}
                <ExercisePrograms exerciseId={ex.id} />
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  )
}
