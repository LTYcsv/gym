import { useEffect } from 'react'

const tg = (window as any).Telegram?.WebApp

export function useBackButton(onBack: () => void) {
  useEffect(() => {
    if (!tg) return
    tg.BackButton.show()
    tg.BackButton.onClick(onBack)
    return () => {
      tg.BackButton.offClick(onBack)
      tg.BackButton.hide()
    }
  }, [onBack])
}
