import { useState, useCallback, useEffect } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useParams, useNavigate } from 'react-router-dom'
import { getWorkoutDay } from '../../api/programs'
import { getAlternatives } from '../../api/exercises'
import { getDayWeights, saveWeight } from '../../api/weights'
import { completeWorkout } from '../../api/sessions'
import type { WorkoutExercise, Exercise } from '../../types'
import { useBackButton } from '../../hooks/useBackButton'
import { useTelegram } from '../../hooks/useTelegram'

export default function WorkoutDayPage() {
  const { slug, dayId } = useParams<{ slug: string; dayId: string }>()
  const navigate = useNavigate()
  const { haptic } = useTelegram()
  const qc = useQueryClient()

  const goBack = useCallback(() => navigate(`/programs/${slug}`), [navigate, slug])
  useBackButton(goBack)

  const storageKey = `workout-${dayId}`

  function loadSession<T>(field: string, fallback: T): T {
    try {
      const raw = sessionStorage.getItem(`${storageKey}:${field}`)
      return raw ? JSON.parse(raw) : fallback
    } catch { return fallback }
  }

  function saveSession(field: string, value: unknown) {
    sessionStorage.setItem(`${storageKey}:${field}`, JSON.stringify(value))
  }

  const [done, setDone] = useState<Record<string, boolean>>(() => loadSession('done', {}))
  const [expanded, setExpanded] = useState<Record<string, boolean>>({})
  const [swapTarget, setSwapTarget] = useState<WorkoutExercise | null>(null)
  const [overrides, setOverrides] = useState<Record<string, Exercise>>(() => loadSession('overrides', {}))
  const [weights, setWeights] = useState<Record<string, string>>({})
  const [savedWeights, setSavedWeights] = useState<Record<string, boolean>>({})

  const { data: day, isLoading } = useQuery({
    queryKey: ['workoutDay', dayId],
    queryFn: () => getWorkoutDay(slug!, dayId!),
    enabled: !!slug && !!dayId,
  })

  const { data: dayWeightsData } = useQuery({
    queryKey: ['dayWeights', dayId],
    queryFn: () => getDayWeights(dayId!),
    enabled: !!dayId,
  })

  useEffect(() => {
    if (!dayWeightsData) return
    setWeights(Object.fromEntries(Object.entries(dayWeightsData).map(([k, v]) => [k, String(v)])))
  }, [dayWeightsData])

  useEffect(() => { saveSession('done', done) }, [done])
  useEffect(() => { saveSession('overrides', overrides) }, [overrides])

  const { data: alternatives } = useQuery({
    queryKey: ['alternatives', swapTarget?.exercise.id, day?.program_type],
    queryFn: () => getAlternatives(swapTarget!.exercise.id, day!.program_type),
    enabled: !!swapTarget && !!day,
  })

  const completeMutation = useMutation({
    mutationFn: () => completeWorkout(dayId!, day!.program_id),
    onSuccess: () => {
      sessionStorage.removeItem(`${storageKey}:done`)
      sessionStorage.removeItem(`${storageKey}:overrides`)
      haptic('success')
      qc.invalidateQueries({ queryKey: ['programs'] })
      qc.invalidateQueries({ queryKey: ['session-count', day!.program_id] })
      qc.invalidateQueries({ queryKey: ['stats'] })
      navigate(`/programs/${slug}`)
    },
  })

  if (isLoading) return <p style={{ padding: 20, color: 'var(--muted)' }}>Загрузка...</p>
  if (!day) return <p style={{ padding: 20, color: 'var(--muted)' }}>День не найден</p>

  const exercises = day.workout_exercises
  const completedCount = exercises.filter(we => done[we.id]).length
  const allDone = completedCount === exercises.length

  function handleWeight(weId: string, val: string) {
    setWeights(s => ({ ...s, [weId]: val }))
    setSavedWeights(s => ({ ...s, [weId]: false }))
  }

  function handleSaveWeight(weId: string, exerciseId: string) {
    const val = parseFloat(weights[weId])
    if (isNaN(val)) return
    saveWeight(weId, val, exerciseId).then(() => {
      setSavedWeights(s => ({ ...s, [weId]: true }))
      setTimeout(() => setSavedWeights(s => ({ ...s, [weId]: false })), 2000)
    })
  }

  return (
    <div style={{ minHeight: '100dvh', paddingBottom: 120 }}>
      {/* Header */}
      <div className="page-header">
        <button onClick={goBack} className="back-btn" style={{ marginBottom: 12 }}>← {day.label}</button>
        <h1 className="heading" style={{ fontSize: 36, color: 'var(--accent-a)' }}>{day.title}</h1>
        {day.subtitle && <p style={{ fontSize: 13, color: 'var(--muted)', marginTop: 4 }}>{day.subtitle}</p>}
      </div>

      {/* Progress */}
      <div style={{ padding: '12px 20px' }}>
        <p className="label" style={{ letterSpacing: '0.08em', marginBottom: 6 }}>
          {completedCount} / {exercises.length} выполнено
        </p>
        <div style={{ height: 3, background: 'var(--surface2)', borderRadius: 3 }}>
          <div style={{ height: '100%', background: allDone ? 'var(--accent-c)' : 'var(--accent-a)', borderRadius: 3, width: `${(completedCount / exercises.length) * 100}%`, transition: 'width 0.4s ease' }} />
        </div>
      </div>

      {/* Exercises */}
      <div style={{ padding: '8px 20px', display: 'flex', flexDirection: 'column', gap: 10 }}>
        {exercises.map((we) => {
          const ex = overrides[we.id] ?? we.exercise
          const isDone = done[we.id]
          const isOpen = expanded[we.id]
          const isSaved = savedWeights[we.id]

          return (
            <div key={we.id} style={{
              background: 'var(--surface)', border: `1px solid ${isDone ? 'rgba(94,242,154,0.2)' : 'var(--border)'}`,
              borderRadius: 14, overflow: 'hidden', opacity: isDone ? 0.6 : 1, transition: 'all 0.2s',
            }}>
              {/* Top row */}
              <div style={{ padding: '14px 16px 12px', display: 'flex', alignItems: 'flex-start', gap: 14, cursor: 'pointer' }}
                onClick={() => setExpanded(s => ({ ...s, [we.id]: !s[we.id] }))}>
                <span className="heading" style={{ fontSize: 28, color: 'var(--accent-a)', minWidth: 28 }}>
                  {String(we.order + 1).padStart(2, '0')}
                </span>
                <div style={{ flex: 1 }}>
                  <p className="label" style={{ fontSize: 10, letterSpacing: '0.1em', marginBottom: 3 }}>
                    {ex.muscle_group}
                  </p>
                  <p style={{ fontSize: 15, fontWeight: 700, textDecoration: isDone ? 'line-through' : 'none' }}>{ex.name}</p>
                </div>
                <button onClick={e => { e.stopPropagation(); haptic(isDone ? 'light' : 'success'); setDone(s => ({ ...s, [we.id]: !s[we.id] })) }}
                  style={{
                    width: 28, height: 28, borderRadius: 8,
                    border: `2px solid ${isDone ? 'var(--accent-c)' : '#3a3a3a'}`,
                    background: isDone ? 'var(--accent-c)' : 'transparent',
                    color: isDone ? '#000' : 'transparent',
                    cursor: 'pointer', fontSize: 14, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0,
                  }}>✓</button>
              </div>

              {/* Tags */}
              <div style={{ padding: '0 16px 12px 58px', display: 'flex', gap: 6, flexWrap: 'wrap', alignItems: 'center' }}>
                {we.sets && <span className="tag" style={{ color: 'var(--accent-a)', border: '1px solid rgba(77,159,255,0.25)', background: 'rgba(77,159,255,0.08)' }}>{we.sets} сета</span>}
                {we.reps && <span className="tag" style={{ color: 'var(--accent-c)', border: '1px solid rgba(94,242,154,0.25)', background: 'rgba(94,242,154,0.08)' }}>{we.reps} повт.</span>}
                {we.rest_seconds && <span className="tag" style={{ color: 'var(--muted)', border: '1px solid var(--border)', background: 'rgba(255,255,255,0.04)' }}>⏱ {we.rest_seconds}с</span>}
                <button onClick={e => { e.stopPropagation(); setSwapTarget(we) }}
                  className="tag" style={{ color: 'var(--accent-b)', border: '1px solid rgba(255,107,53,0.3)', background: 'rgba(255,107,53,0.08)', cursor: 'pointer' }}>
                  ⇄ Заменить
                </button>
              </div>

              {/* Expanded: technique + weight */}
              {isOpen && (
                <div style={{ borderTop: '1px solid var(--border)', padding: '14px 16px 16px 58px' }}>
                  {ex.technique && (
                    <p style={{ fontSize: 13, lineHeight: 1.7, color: '#b0b0b0', marginBottom: 14 }}>{ex.technique}</p>
                  )}
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ fontSize: 12, color: 'var(--muted)', whiteSpace: 'nowrap' }}>Рабочий вес</span>
                    <input
                      type="number" inputMode="decimal" placeholder="—"
                      value={weights[we.id] ?? ''}
                      onChange={e => handleWeight(we.id, e.target.value)}
                      style={{
                        width: 80, background: 'var(--bg)', border: '1px solid var(--border)',
                        borderRadius: 8, padding: '6px 10px', fontSize: 14, fontWeight: 700,
                        color: 'var(--text)', outline: 'none', fontFamily: 'inherit',
                      }}
                    />
                    <span style={{ fontSize: 12, color: 'var(--muted)' }}>кг</span>
                    <button onClick={() => handleSaveWeight(we.id, ex.id)}
                      style={{
                        padding: '6px 12px', borderRadius: 8, fontSize: 12, fontWeight: 700,
                        background: isSaved ? 'rgba(94,242,154,0.15)' : 'rgba(77,159,255,0.1)',
                        border: `1px solid ${isSaved ? 'rgba(94,242,154,0.3)' : 'rgba(77,159,255,0.25)'}`,
                        color: isSaved ? 'var(--accent-c)' : 'var(--accent-a)', cursor: 'pointer',
                      }}>
                      {isSaved ? '✓ Сохранено' : 'Сохранить'}
                    </button>
                  </div>
                </div>
              )}
            </div>
          )
        })}
      </div>

      {/* Complete button */}
      <div className="bottom-bar">
        <button
          onClick={() => completeMutation.mutate()}
          disabled={!allDone || completeMutation.isPending}
          style={{
            width: '100%', padding: '16px', borderRadius: 14, fontSize: 15, fontWeight: 700,
            fontFamily: 'inherit', cursor: allDone ? 'pointer' : 'default',
            background: allDone ? 'var(--accent-c)' : 'var(--surface2)',
            color: allDone ? '#000' : 'var(--muted)',
            border: 'none', transition: 'all 0.2s',
          }}>
          {completeMutation.isPending ? 'Сохранение...' : allDone ? '✓ Тренировка завершена' : `Выполни все упражнения (${completedCount}/${exercises.length})`}
        </button>
      </div>

      {/* Swap modal */}
      {swapTarget && (
        <div className="modal-overlay" onClick={() => setSwapTarget(null)}>
          <div className="modal-sheet" style={{ maxHeight: '80dvh', display: 'flex', flexDirection: 'column' }}
            onClick={e => e.stopPropagation()}>
            <div style={{ padding: '18px 20px 12px', borderBottom: '1px solid var(--border)', display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
              <div>
                <p className="label" style={{ letterSpacing: '0.1em', marginBottom: 4 }}>Заменить · {day.program_type}</p>
                <p style={{ fontSize: 15, fontWeight: 700 }}>{swapTarget.exercise.name}</p>
              </div>
              <button onClick={() => setSwapTarget(null)} style={{ width: 32, height: 32, borderRadius: '50%', border: '1px solid var(--border)', background: 'var(--surface2)', color: 'var(--muted)', cursor: 'pointer' }}>✕</button>
            </div>
            <div style={{ overflowY: 'auto', padding: '12px 16px 32px', display: 'flex', flexDirection: 'column', gap: 8 }}>
              {!alternatives?.length && <p style={{ color: 'var(--muted)', fontSize: 13, padding: 20 }}>Альтернативы не найдены</p>}
              {alternatives?.map(alt => (
                <div key={alt.id}
                  style={{ background: 'var(--surface2)', border: '1px solid var(--border)', borderRadius: 12, padding: '14px 16px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 12 }}
                  onClick={() => { setOverrides(s => ({ ...s, [swapTarget.id]: alt })); setSwapTarget(null) }}>
                  <div style={{ flex: 1 }}>
                    <p style={{ fontSize: 14, fontWeight: 700 }}>{alt.name}</p>
                    <p style={{ fontSize: 11, color: 'var(--muted)', marginTop: 2 }}>{alt.muscle_group} · {alt.types.join(', ')}</p>
                  </div>
                  <span style={{ fontSize: 18, color: '#3a3a3a' }}>›</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
