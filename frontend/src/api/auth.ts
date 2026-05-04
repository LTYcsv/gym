import api from './client'

interface AuthResponse {
  token: string
  user: { id: string; telegram_id: number; username: string | null; first_name: string | null }
}

export async function authWithTelegram(initData: string): Promise<AuthResponse> {
  const res = await api.post<AuthResponse>('/auth/telegram', { init_data: initData })
  return res.data
}

export async function authDev(): Promise<AuthResponse> {
  const res = await api.post<AuthResponse>('/auth/dev')
  return res.data
}
