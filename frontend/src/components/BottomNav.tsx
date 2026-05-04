import { useLocation, useNavigate } from 'react-router-dom'

const TABS = [
  { path: '/',        icon: '🏋️', label: 'Тренировки' },
  { path: '/stats',   icon: '📊', label: 'Прогресс'   },
  { path: '/library', icon: '📖', label: 'База'        },
]

export default function BottomNav() {
  const { pathname } = useLocation()
  const navigate = useNavigate()

  const active = (path: string) =>
    path === '/' ? pathname === '/' : pathname.startsWith(path)

  return (
    <nav style={{
      position: 'fixed', bottom: 0, left: 0, right: 0,
      display: 'flex',
      background: 'rgba(13,13,13,0.95)',
      borderTop: '1px solid rgba(255,255,255,0.08)',
      backdropFilter: 'blur(12px)',
      WebkitBackdropFilter: 'blur(12px)',
      paddingBottom: 'env(safe-area-inset-bottom)',
      zIndex: 20,
    }}>
      {TABS.map(tab => {
        const isActive = active(tab.path)
        return (
          <button
            key={tab.path}
            onClick={() => navigate(tab.path)}
            style={{
              flex: 1, padding: '12px 8px 14px',
              display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4,
              cursor: 'pointer', border: 'none', background: 'none',
              color: isActive ? 'var(--accent-a)' : 'var(--muted)',
              fontFamily: 'Manrope, sans-serif',
              transition: 'color 0.15s',
              WebkitTapHighlightColor: 'transparent',
            }}
          >
            <span style={{ fontSize: 20 }}>{tab.icon}</span>
            <span style={{
              fontSize: 10, fontWeight: 700,
              letterSpacing: '0.06em', textTransform: 'uppercase',
            }}>
              {tab.label}
            </span>
            {isActive && (
              <span style={{
                position: 'absolute',
                bottom: 'calc(env(safe-area-inset-bottom) + 0px)',
                width: 32, height: 2,
                background: 'var(--accent-a)',
                borderRadius: 2,
              }} />
            )}
          </button>
        )
      })}
    </nav>
  )
}
