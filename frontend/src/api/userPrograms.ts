import api from './client'
import type { UserProgram } from '../types'

export const getUserProgram = (programId: string) =>
  api.get<UserProgram | null>(`/user-programs/${programId}`).then(r => r.data)

export const enrollProgram = (programId: string, daysPerWeek: number) =>
  api.post<UserProgram>('/user-programs/', { program_id: programId, days_per_week: daysPerWeek }).then(r => r.data)
