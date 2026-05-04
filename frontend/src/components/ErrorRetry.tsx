export function ErrorRetry({ onRetry }: { onRetry: () => void }) {
  return (
    <div style={{ padding: '32px 20px', textAlign: 'center' }}>
      <p style={{ color: 'var(--muted)', fontSize: 14, marginBottom: 16 }}>
        Не удалось загрузить данные
      </p>
      <button
        onClick={onRetry}
        style={{
          padding: '10px 20px', borderRadius: 10, fontSize: 13, fontWeight: 700,
          background: 'rgba(77,159,255,0.1)', border: '1px solid rgba(77,159,255,0.25)',
          color: 'var(--accent-a)', cursor: 'pointer', fontFamily: 'inherit',
        }}
      >
        Повторить
      </button>
    </div>
  )
}
