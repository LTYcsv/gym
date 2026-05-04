import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { authWithTelegram, authDev } from './api/auth'
import App from './App'
import './index.css'

const tg = (window as any).Telegram?.WebApp

async function initAuth() {
  if (localStorage.getItem('token')) return
  if (tg?.initData) {
    tg.ready()
    tg.expand()
    const { token } = await authWithTelegram(tg.initData)
    localStorage.setItem('token', token)
  } else {
    // локальная разработка
    const { token } = await authDev()
    localStorage.setItem('token', token)
  }
}

initAuth().catch(() => {})

const queryClient = new QueryClient()

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <App />
      </BrowserRouter>
    </QueryClientProvider>
  </StrictMode>,
)
