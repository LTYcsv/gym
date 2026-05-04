import { describe, it, expect } from 'vitest'
import { buildCalendarCells } from '../utils/calendar'

// Fixed reference date: Sunday 2025-05-04
const SUNDAY = new Date('2025-05-04')
// Fixed reference date: Monday 2025-05-05
const MONDAY = new Date('2025-05-05')

describe('buildCalendarCells', () => {
  it('always returns exactly 35 cells', () => {
    expect(buildCalendarCells(SUNDAY)).toHaveLength(35)
    expect(buildCalendarCells(MONDAY)).toHaveLength(35)
  })

  it('first cell is always a Monday', () => {
    for (const date of [SUNDAY, MONDAY, new Date('2025-05-01')]) {
      const cells = buildCalendarCells(date)
      const first = new Date(cells[0].date)
      expect(first.getDay()).toBe(1) // 1 = Monday
    }
  })

  it('last 7 cells include today', () => {
    const cells = buildCalendarCells(SUNDAY)
    const todayStr = SUNDAY.toLocaleDateString('sv')
    const lastWeek = cells.slice(28)
    expect(lastWeek.some(c => c.date === todayStr)).toBe(true)
  })

  it('inWindow spans exactly 30 days', () => {
    const inWindow = buildCalendarCells(SUNDAY).filter(c => c.inWindow)
    expect(inWindow).toHaveLength(30)
  })

  it('today is inWindow', () => {
    const todayStr = SUNDAY.toLocaleDateString('sv')
    const cells = buildCalendarCells(SUNDAY)
    expect(cells.find(c => c.date === todayStr)?.inWindow).toBe(true)
  })

  it('30 days ago is inWindow', () => {
    const d = new Date(SUNDAY)
    d.setDate(d.getDate() - 29)
    const dateStr = d.toLocaleDateString('sv')
    const cells = buildCalendarCells(SUNDAY)
    expect(cells.find(c => c.date === dateStr)?.inWindow).toBe(true)
  })

  it('31 days ago is not inWindow', () => {
    const d = new Date(SUNDAY)
    d.setDate(d.getDate() - 30)
    const dateStr = d.toLocaleDateString('sv')
    const cells = buildCalendarCells(SUNDAY)
    const cell = cells.find(c => c.date === dateStr)
    // cell may be outside the 35-cell range entirely, or inWindow=false
    expect(cell?.inWindow ?? false).toBe(false)
  })

  it('cells before the window are not inWindow', () => {
    const cells = buildCalendarCells(SUNDAY)
    const outOfWindow = cells.filter(c => !c.inWindow)
    // 35 total - 30 in window = 5 cells outside
    expect(outOfWindow).toHaveLength(5)
  })
})
