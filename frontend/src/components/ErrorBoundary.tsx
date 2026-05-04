import { Component, type ErrorInfo, type ReactNode } from 'react'

interface Props { children: ReactNode }
interface State { hasError: boolean }

export default class ErrorBoundary extends Component<Props, State> {
  state: State = { hasError: false }

  static getDerivedStateFromError(): State {
    return { hasError: true }
  }

  componentDidCatch(error: Error, info: ErrorInfo) {
    console.error('[ErrorBoundary]', error.message, info.componentStack)
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{ padding: '48px 20px', textAlign: 'center' }}>
          <p style={{ fontSize: 16, fontWeight: 700, color: 'var(--text)', marginBottom: 8 }}>
            Что-то пошло не так
          </p>
          <p style={{ fontSize: 13, color: 'var(--muted)', marginBottom: 24 }}>
            Перезапустите приложение
          </p>
          <button
            onClick={() => this.setState({ hasError: false })}
            style={{
              padding: '10px 20px', borderRadius: 10, fontSize: 13, fontWeight: 700,
              background: 'rgba(77,159,255,0.1)', border: '1px solid rgba(77,159,255,0.25)',
              color: 'var(--accent-a)', cursor: 'pointer', fontFamily: 'inherit',
            }}
          >
            Попробовать снова
          </button>
        </div>
      )
    }
    return this.props.children
  }
}
