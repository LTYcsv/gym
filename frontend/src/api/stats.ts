import api from './client'

export interface MuscleGroupCount {
  muscle_group: string
  count: number
}

export interface RecordItem {
  exercise_name: string
  weight_kg: number
  achieved_at: string
}

export interface StatsOut {
  weekly_done: number
  weekly_planned: number
  weekly_muscle_groups: MuscleGroupCount[]
  workout_dates: string[]
  week_streak: number
  workout_streak: number
  records: RecordItem[]
}

export const getStats = () =>
  api.get<StatsOut>('/stats/').then(r => r.data)
