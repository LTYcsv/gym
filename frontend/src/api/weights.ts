import api from './client'

export const saveWeight = (workout_exercise_id: string, weight_kg: number) =>
  api.put(`/weights/${workout_exercise_id}`, { weight_kg }).then(r => r.data)

export const getDayWeights = (workout_day_id: string): Promise<Record<string, number>> =>
  api.get(`/weights/day/${workout_day_id}`).then(r => r.data)
