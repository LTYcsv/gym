import { useState } from 'react'

interface Props {
  programName: string
  onConfirm: (days: number) => void
}

export default function OnboardingSheet({ programName, onConfirm }: Props) {
  const options = [1, 2, 3, 4, 5, 6, 7]
  const [selected, setSelected] = useState(3)

  return (
    <div style={{
      position: 'fixed', inset: 0, zIndex: 100,
      background: 'rgba(0,0,0,0.7)',
      display: 'flex', alignItems: 'flex-end',
    }}>
      <div style={{
        width: '100%', background: 'var(--surface)',
        borderRadius: '20px 20px 0 0',
        padding: '28px 24px 40px',
      }}>
        <div style={{
          width: 40, height: 4, borderRadius: 2,
          background: 'var(--border)', margin: '0 auto 24px',
        }} />
        <h2 style={{ fontFamily: 'Bebas Neue, sans-serif', fontSize: 28, marginBottom: 6 }}>
          {programName}
        </h2>
        <p style={{ color: 'var(--muted)', fontSize: 14, marginBottom: 28 }}>
          Сколько дней в неделю ты готов тренироваться?
        </p>

        <div style={{ display: 'flex', gap: 10, marginBottom: 32 }}>
          {options.map(n => (
            <button
              key={n}
              onClick={() => setSelected(n)}
              style={{
                flex: 1, paddingTop: 14, paddingBottom: 14,
                borderRadius: 12, border: '2px solid',
                borderColor: selected === n ? 'var(--accent)' : 'var(--border)',
                background: selected === n ? 'var(--accent)' : 'transparent',
                color: selected === n ? '#000' : 'var(--text)',
                fontSize: 18, fontWeight: 700, cursor: 'pointer',
                transition: 'all 0.15s',
              }}
            >
              {n}
            </button>
          ))}
        </div>

        <button
          onClick={() => onConfirm(selected)}
          style={{
            width: '100%', padding: '16px',
            background: 'var(--accent)', color: '#000',
            border: 'none', borderRadius: 14,
            fontSize: 16, fontWeight: 700, cursor: 'pointer',
          }}
        >
          Начать программу
        </button>
      </div>
    </div>
  )
}
