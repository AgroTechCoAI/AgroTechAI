import { getWebSocketUrl, getApiBaseUrl } from '../../src/utils/websocket-config.js'

describe('WebSocket Configuration', () => {
  beforeEach(() => {
    // Reset environment variables
    delete import.meta.env.VITE_WEBSOCKET_URL
    delete import.meta.env.VITE_API_URL

    // Mock window.location
    Object.defineProperty(window, 'location', {
      writable: true,
      value: {
        protocol: 'http:',
        host: 'localhost:3000'
      }
    })
  })

  describe('getWebSocketUrl', () => {
    it('returns environment variable when available', () => {
      import.meta.env.VITE_WEBSOCKET_URL = 'ws://dev-server:8000/ws'

      const result = getWebSocketUrl()

      expect(result).toBe('ws://dev-server:8000/ws')
    })

    it('returns relative URL when no environment variable is set', () => {
      const result = getWebSocketUrl()

      expect(result).toBe('ws://localhost:3000/ws')
    })

    it('uses wss protocol for HTTPS sites', () => {
      window.location.protocol = 'https:'
      window.location.host = 'myapp.com'

      const result = getWebSocketUrl()

      expect(result).toBe('wss://myapp.com/ws')
    })

    it('uses ws protocol for HTTP sites', () => {
      window.location.protocol = 'http:'
      window.location.host = 'localhost:3000'

      const result = getWebSocketUrl()

      expect(result).toBe('ws://localhost:3000/ws')
    })
  })

  describe('getApiBaseUrl', () => {
    it('returns environment variable when available', () => {
      import.meta.env.VITE_API_URL = 'http://dev-server:8000/api'

      const result = getApiBaseUrl()

      expect(result).toBe('http://dev-server:8000/api')
    })

    it('returns relative URL when no environment variable is set', () => {
      const result = getApiBaseUrl()

      expect(result).toBe('http://localhost:3000/api')
    })

    it('uses HTTPS for secure sites', () => {
      window.location.protocol = 'https:'
      window.location.host = 'myapp.com'

      const result = getApiBaseUrl()

      expect(result).toBe('https://myapp.com/api')
    })
  })
})
