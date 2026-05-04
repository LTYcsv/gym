import axios from 'axios'
import { authDev, authWithTelegram } from './auth'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL ?? '/api',
})

api.interceptors.request.use(config => {
  const token = localStorage.getItem('token')
  if (token) config.headers.Authorization = `Bearer ${token}`
  config.headers['X-Timezone'] = Intl.DateTimeFormat().resolvedOptions().timeZone
  return config
})

api.interceptors.response.use(
  res => res,
  async err => {
    if (err.response?.status === 401) {
      localStorage.removeItem('token')
      try {
        const tg = (window as any).Telegram?.WebApp
        const { token } = tg?.initData
          ? await authWithTelegram(tg.initData)
          : await authDev()
        localStorage.setItem('token', token)
        err.config.headers.Authorization = `Bearer ${token}`
        return api.request(err.config)
      } catch {
        // не смогли переавторизоваться — пробрасываем ошибку
      }
    }
    return Promise.reject(err)
  }
)

export default api
