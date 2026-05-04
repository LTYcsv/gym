import api from './client'
import type { Exercise, ExerciseProgram } from '../types'

export const getExercises = (params?: {
  muscle_group?: string
  type?: string
  equipment?: string
}) => api.get<Exercise[]>('/exercises/', { params }).then(r => r.data)

export const getAlternatives = (exerciseId: string, programType: string) =>
  api.get<Exercise[]>('/exercises/alternatives', {
    params: { exercise_id: exerciseId, program_type: programType },
  }).then(r => r.data)

export const getExercisePrograms = (exerciseId: string) =>
  api.get<ExerciseProgram[]>(`/exercises/${exerciseId}/programs`).then(r => r.data)
