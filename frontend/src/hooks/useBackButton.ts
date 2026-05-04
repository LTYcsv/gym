import { useEffect } from 'react'

export function useBackButton(onBack: () => void) {
  useEffect(() => {
    const tg = (window as any).Telegram?.WebApp
    if (!tg) return
    tg.BackButton.show()
    tg.BackButton.onClick(onBack)
    return () => {
      tg.BackButton.offClick(onBack)
      tg.BackButton.hide()
    }
  }, [onBack])
}
