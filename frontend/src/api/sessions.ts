import api from './client'

export interface SessionOut {
  id: string
  workout_day_id: string
  program_id: string
  completed_at: string
}

export const completeWorkout = (workout_day_id: string, program_id: string) =>
  api.post<SessionOut>('/sessions/', { workout_day_id, program_id }).then(r => r.data)

export const getWeeklySessions = () =>
  api.get<SessionOut[]>('/sessions/weekly').then(r => r.data)

export const getSessionHistory = () =>
  api.get<SessionOut[]>('/sessions/history').then(r => r.data)

export const getProgramSessionCounts = (programId: string) =>
  api.get<{ total: number; weekly: number }>(`/sessions/count/${programId}`).then(r => r.data)
