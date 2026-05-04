export interface Program {
  id: string
  name: string
  slug: string
  description: string | null
  type: ProgramType
  days_per_week: number | null
  difficulty: Difficulty | null
  goal: string | null
  weekly_sessions: number
  user_days_per_week: number | null
}

export interface UserProgram {
  id: string
  program_id: string
  days_per_week: number
  started_at: string
}

export interface ProgramDetail extends Program {
  workout_days: WorkoutDaySummary[]
}

export type ProgramType = 'strength' | 'hypertrophy' | 'cardio' | 'hiit' | 'calisthenics'
export type Difficulty = 'beginner' | 'intermediate' | 'advanced'
export type MuscleGroup =
  | 'back' | 'chest' | 'shoulders' | 'biceps' | 'triceps'
  | 'quadriceps' | 'hamstrings' | 'calves' | 'glutes'
  | 'core' | 'lower_back' | 'traps' | 'forearms'

export interface Exercise {
  id: string
  name: string
  muscle_group: MuscleGroup
  types: ProgramType[]
  equipment: string[]
  technique: string | null
  difficulty: string
}

export interface WorkoutDaySummary {
  id: string
  label: string | null
  title: string | null
  subtitle: string | null
  day_number: number
  exercise_count: number
}

export interface WorkoutExercise {
  id: string
  exercise: Exercise
  sets: number | null
  reps: string | null
  rest_seconds: number | null
  order: number
  notes: string | null
}

export interface WorkoutDay {
  id: string
  program_id: string
  program_type: ProgramType
  program_slug: string
  label: string | null
  title: string | null
  subtitle: string | null
  day_number: number
  workout_exercises: WorkoutExercise[]
}

export interface ExerciseProgram {
  program_name: string
  program_slug: string
  day_label: string | null
  day_title: string | null
}
