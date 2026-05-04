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
    <nav className="bottom-nav">
      {TABS.map(tab => {
        const isActive = active(tab.path)
        return (
          <button
            key={tab.path}
            onClick={() => navigate(tab.path)}
            className="bottom-nav__tab"
            style={{ color: isActive ? 'var(--accent-a)' : 'var(--muted)' }}
          >
            <span style={{ fontSize: 20 }}>{tab.icon}</span>
            <span className="bottom-nav__tab-label">{tab.label}</span>
            {isActive && <span className="bottom-nav__indicator" />}
          </button>
        )
      })}
    </nav>
  )
}
