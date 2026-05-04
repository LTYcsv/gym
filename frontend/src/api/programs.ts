import api from './client'
import type { Program, ProgramDetail, WorkoutDay } from '../types'

export const getPrograms = () =>
  api.get<Program[]>('/programs/with-progress').then(r => r.data)

export const getProgram = (slug: string) =>
  api.get<ProgramDetail>(`/programs/${slug}`).then(r => r.data)

export const getWorkoutDay = (slug: string, dayId: string) =>
  api.get<WorkoutDay>(`/programs/${slug}/days/${dayId}`).then(r => r.data)
