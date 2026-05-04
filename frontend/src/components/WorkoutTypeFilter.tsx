import { useState } from 'react'
import type { ProgramType } from '../types'

interface TypeMeta {
  key: ProgramType
  label: string
  color: string
  emoji: string
  description: string
  goal: string
  reps: string
  rest: string
}

const WORKOUT_TYPES: TypeMeta[] = [
  {
    key: 'strength', label: 'Сила', color: '#ff6b35', emoji: '💪',
    goal: 'Стать сильнее',
    description: 'Тренировки на максимальную силу. Работа с тяжёлыми весами в диапазоне 1–5 повторений. Развивает нейромышечную связь и плотность мышц. Длинный отдых между подходами (3–5 мин).',
    reps: '1–5 повт.', rest: '3–5 мин',
  },
  {
    key: 'hypertrophy', label: 'Масса', color: '#4d9fff', emoji: '🏋️',
    goal: 'Нарастить мышцы',
    description: 'Тренировки на рост мышечной массы (гипертрофию). Умеренный вес, 8–15 повторений. Важна прогрессия нагрузки и достаточное питание с профицитом белка.',
    reps: '8–15 повт.', rest: '60–90 сек',
  },
  {
    key: 'cardio', label: 'Кардио', color: '#5ef29a', emoji: '🏃',
    goal: 'Выносливость и жиросжигание',
    description: 'Упражнения для сердечно-сосудистой системы. Улучшают выносливость, сжигают калории, ускоряют восстановление. Поддерживают умеренный пульс длительное время.',
    reps: '15–30+ мин', rest: 'Минимальный',
  },
  {
    key: 'hiit', label: 'HIIT', color: '#ffd166', emoji: '⚡',
    goal: 'Жиросжигание и скорость',
    description: 'Высокоинтенсивные интервальные тренировки. Чередование коротких взрывных усилий и отдыха. Эффективно сжигают жир, улучшают метаболизм и занимают мало времени.',
    reps: '20–40 сек', rest: '10–20 сек',
  },
  {
    key: 'calisthenics', label: 'Калистеника', color: '#d4a0ff', emoji: '🤸',
    goal: 'Контроль тела и гибкость',
    description: 'Тренировки с весом собственного тела. Развивают функциональную силу, координацию и гибкость. Не требуют оборудования. Упражнения прогрессируют усложнением движений.',
    reps: '8–20 повт.', rest: '45–90 сек',
  },
]

interface Props {
  selected: ProgramType | null
  onSelect: (type: ProgramType | null) => void
}

export default function WorkoutTypeFilter({ selected, onSelect }: Props) {
  const [sheet, setSheet] = useState<TypeMeta | null>(null)

  return (
    <>
      <div style={{ display: 'flex', gap: 8, padding: '0 20px 12px', overflowX: 'auto', scrollbarWidth: 'none' }}>
        {/* Все типы */}
        <button
          onClick={() => onSelect(null)}
          style={{
            flexShrink: 0, padding: '5px 12px', borderRadius: 20, fontSize: 11, fontWeight: 700,
            cursor: 'pointer', fontFamily: 'inherit',
            background: selected === null ? 'var(--surface2)' : 'transparent',
            color: selected === null ? 'var(--text)' : 'var(--muted)',
            border: `1px solid ${selected === null ? 'rgba(255,255,255,0.2)' : 'var(--border)'}`,
          }}
        >
          Все типы
        </button>

        {WORKOUT_TYPES.map(t => {
          const isActive = selected === t.key
          return (
            <div key={t.key} style={{ display: 'flex', alignItems: 'center', flexShrink: 0 }}>
              <button
                onClick={() => onSelect(isActive ? null : t.key)}
                style={{
                  padding: '5px 8px 5px 12px', borderRadius: '20px 0 0 20px', fontSize: 11, fontWeight: 700,
                  cursor: 'pointer', fontFamily: 'inherit',
                  background: isActive ? `${t.color}22` : 'transparent',
                  color: isActive ? t.color : 'var(--muted)',
                  border: `1px solid ${isActive ? `${t.color}44` : 'var(--border)'}`,
                  borderRight: 'none',
                }}
              >
                {t.label}
              </button>
              <button
                onClick={e => { e.stopPropagation(); setSheet(t) }}
                title={`Подробнее: ${t.label}`}
                style={{
                  width: 22, height: 22, borderRadius: '0 20px 20px 0', fontSize: 10, fontWeight: 700,
                  cursor: 'pointer', fontFamily: 'inherit', fontStyle: 'italic',
                  display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0,
                  background: isActive ? `${t.color}22` : 'rgba(255,255,255,0.06)',
                  color: isActive ? t.color : 'var(--muted)',
                  border: `1px solid ${isActive ? `${t.color}44` : 'var(--border)'}`,
                  padding: '0 6px 0 4px',
                }}
              >
                i
              </button>
            </div>
          )
        })}
      </div>

      {sheet && (
        <div className="modal-overlay" onClick={() => setSheet(null)}>
          <div className="modal-sheet" onClick={e => e.stopPropagation()} style={{ paddingBottom: 32 }}>

            {/* Header */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '18px 20px 14px', borderBottom: '1px solid var(--border)' }}>
              <div style={{
                width: 48, height: 48, borderRadius: 14, flexShrink: 0,
                background: `${sheet.color}22`,
                display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: 24,
              }}>
                {sheet.emoji}
              </div>
              <div style={{ flex: 1 }}>
                <p style={{ fontSize: 20, fontWeight: 700, color: 'var(--text)', marginBottom: 2 }}>{sheet.label}</p>
                <p style={{ fontSize: 13, fontWeight: 500, color: sheet.color }}>{sheet.goal}</p>
              </div>
              <button
                onClick={() => setSheet(null)}
                style={{
                  width: 32, height: 32, borderRadius: '50%',
                  border: '1px solid var(--border)', background: 'var(--surface2)',
                  color: 'var(--muted)', cursor: 'pointer', fontSize: 13,
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                }}
              >✕</button>
            </div>

            {/* Description */}
            <p style={{ fontSize: 15, lineHeight: 1.7, color: 'rgba(255,255,255,0.72)', padding: '16px 20px 20px' }}>
              {sheet.description}
            </p>

            {/* Stats */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, padding: '0 20px 20px' }}>
              {[{ label: 'Повторения', value: sheet.reps }, { label: 'Отдых', value: sheet.rest }].map(s => (
                <div key={s.label} style={{
                  background: 'rgba(255,255,255,0.07)', borderRadius: 14,
                  padding: '12px 14px',
                }}>
                  <p style={{ fontSize: 11, color: 'var(--muted)', fontWeight: 600, letterSpacing: '0.06em', textTransform: 'uppercase', marginBottom: 4 }}>
                    {s.label}
                  </p>
                  <p style={{ fontSize: 17, fontWeight: 700, color: sheet.color }}>{s.value}</p>
                </div>
              ))}
            </div>

            {/* Accent bar */}
            <div style={{ height: 3, borderRadius: 2, background: sheet.color, opacity: 0.6, margin: '0 20px' }} />
          </div>
        </div>
      )}
    </>
  )
}
