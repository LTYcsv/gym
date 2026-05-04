import { Routes, Route, useLocation } from 'react-router-dom'
import Dashboard from './pages/Dashboard/Dashboard'
import ProgramPage from './pages/Program/ProgramPage'
import WorkoutDayPage from './pages/Program/WorkoutDayPage'
import LibraryPage from './pages/Library/LibraryPage'
import StatsPage from './pages/Stats/StatsPage'
import BottomNav from './components/BottomNav'

const TOP_LEVEL = ['/', '/library', '/stats']

export default function App() {
  const { pathname } = useLocation()
  const showNav = TOP_LEVEL.includes(pathname)

  return (
    <>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/programs/:slug" element={<ProgramPage />} />
        <Route path="/programs/:slug/days/:dayId" element={<WorkoutDayPage />} />
        <Route path="/library" element={<LibraryPage />} />
        <Route path="/stats" element={<StatsPage />} />
      </Routes>
      {showNav && <BottomNav />}
    </>
  )
}
