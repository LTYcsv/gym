import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { getProgram } from '../../api/programs'
import { getUserProgram, enrollProgram } from '../../api/userPrograms'
import { getProgramSessionCounts } from '../../api/sessions'
import { useBackButton } from '../../hooks/useBackButton'
import OnboardingSheet from '../../components/OnboardingSheet'

export default function ProgramPage() {
  const { slug } = useParams<{ slug: string }>()
  const navigate = useNavigate()
  const qc = useQueryClient()
  useBackButton(() => navigate('/'))

  const { data: program, isLoading: programLoading } = useQuery({
    queryKey: ['program', slug],
    queryFn: () => getProgram(slug!),
    enabled: !!slug,
  })

  const { data: enrollment, isLoading: enrollLoading } = useQuery({
    queryKey: ['user-program', program?.id],
    queryFn: () => getUserProgram(program!.id),
    enabled: !!program?.id,
  })

  const { data: sessionCounts } = useQuery({
    queryKey: ['session-count', program?.id],
    queryFn: () => getProgramSessionCounts(program!.id),
    enabled: !!program?.id && !!enrollment,
  })
  const totalSessions = sessionCounts?.total ?? 0
  const weeklySessions = sessionCounts?.weekly ?? 0

  const enroll = useMutation({
    mutationFn: (days: number) => enrollProgram(program!.id, days),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['user-program', program?.id] })
      qc.invalidateQueries({ queryKey: ['programs'] })
    },
  })

  if (programLoading || enrollLoading) return <p style={{ padding: 20, color: 'var(--muted)' }}>Загрузка...</p>
  if (!program) return <p style={{ padding: 20, color: 'var(--muted)' }}>Программа не найдена</p>

  const totalDays = program.workout_days.length
  const slotsCount = enrollment?.days_per_week ?? totalDays
  // Фиксируем начало недели: с какого дня цикла началась эта неделя
  const weekStartIndex = (totalSessions - weeklySessions) % totalDays
  const schedule = Array.from({ length: slotsCount }, (_, i) => ({
    slot: i + 1,
    day: program.workout_days[(weekStartIndex + i) % totalDays],
    isDone: i < weeklySessions,
    isNext: i === weeklySessions && weeklySessions < slotsCount,
  }))

  return (
    <div style={{ minHeight: '100dvh', paddingBottom: 100 }}>
      <div className="page-header">
        <Link to="/" className="back-btn">← Назад</Link>
        <h1 className="heading" style={{ fontSize: 40, marginTop: 12 }}>{program.name}</h1>
        {program.description && <p style={{ color: 'var(--muted)', fontSize: 13, marginTop: 8 }}>{program.description}</p>}
        {enrollment && (
          <p style={{ fontSize: 12, color: 'var(--accent)', marginTop: 10, fontWeight: 600 }}>
            {enrollment.days_per_week} {enrollment.days_per_week === 1 ? 'день' : enrollment.days_per_week < 5 ? 'дня' : 'дней'} в неделю
          </p>
        )}
      </div>

      <div style={{ padding: '16px 20px', display: 'flex', flexDirection: 'column', gap: 10 }}>
        {schedule.map(({ slot, day, isDone, isNext }) => (
          <Link key={slot} to={`/programs/${slug}/days/${day.id}`} style={{ textDecoration: 'none' }}>
            <div style={{
              background: 'var(--surface)',
              border: `1px solid ${isNext ? 'var(--accent)' : isDone ? 'rgba(94,242,154,0.2)' : 'var(--border)'}`,
              borderRadius: 14, padding: '16px 20px',
              position: 'relative',
              opacity: isDone ? 0.5 : 1,
            }}>
              <div style={{ position: 'absolute', top: 14, right: 16 }}>
                {isDone && <span style={{ fontSize: 16 }}>✓</span>}
                {isNext && (
                  <span style={{
                    fontSize: 10, fontWeight: 800, letterSpacing: '0.06em',
                    color: '#000', background: 'var(--accent)',
                    borderRadius: 20, padding: '2px 8px',
                    textTransform: 'uppercase',
                  }}>Следующая</span>
                )}
              </div>
              <p className="label" style={{ letterSpacing: '0.1em', marginBottom: 4 }}>
                День {slot}
              </p>
              <h3 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text)' }}>{day.title}</h3>
              {day.subtitle && <p style={{ fontSize: 12, color: 'var(--muted)', marginTop: 4 }}>{day.subtitle}</p>}
              <p style={{ fontSize: 12, color: 'var(--muted)', marginTop: 8 }}>{day.exercise_count} упражнений</p>
            </div>
          </Link>
        ))}
      </div>

      {!enrollment && !enroll.isPending && (
        <OnboardingSheet
          programName={program.name}
          onConfirm={days => enroll.mutate(days)}
        />
      )}
    </div>
  )
}
