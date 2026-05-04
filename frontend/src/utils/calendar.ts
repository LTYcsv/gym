export interface CalendarCell {
  date: string
  inWindow: boolean
}

export function buildCalendarCells(today: Date): CalendarCell[] {
  const isoDay = (today.getDay() + 6) % 7
  const monday = new Date(today)
  monday.setDate(today.getDate() - isoDay)

  const start = new Date(monday)
  start.setDate(monday.getDate() - 28)

  const cutoff = new Date(today)
  cutoff.setDate(today.getDate() - 29)

  const cells: CalendarCell[] = []
  for (let i = 0; i < 35; i++) {
    const d = new Date(start)
    d.setDate(start.getDate() + i)
    const dateStr = d.toLocaleDateString('sv')
    cells.push({ date: dateStr, inWindow: d >= cutoff && d <= today })
  }
  return cells
}
