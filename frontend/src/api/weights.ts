import api from './client'

export const saveWeight = (workout_exercise_id: string, weight_kg: number, exercise_id?: string) =>
  api.put(`/weights/${workout_exercise_id}`, { weight_kg, exercise_id }).then(r => r.data)

export const getDayWeights = (workout_day_id: string): Promise<Record<string, number>> =>
  api.get(`/weights/day/${workout_day_id}`).then(r => r.data)
