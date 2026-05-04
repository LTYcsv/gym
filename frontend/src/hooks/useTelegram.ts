export function useTelegram() {
  const tg = (window as any).Telegram?.WebApp
  const user = tg?.initDataUnsafe?.user ?? null
  const isInsideTelegram = !!tg?.initData

  function haptic(type: 'light' | 'medium' | 'heavy' | 'success' | 'error' = 'light') {
    if (!tg) return
    if (type === 'success' || type === 'error') {
      tg.HapticFeedback.notificationOccurred(type)
    } else {
      tg.HapticFeedback.impactOccurred(type)
    }
  }

  return { webApp: tg, user, isInsideTelegram, haptic }
}
