import { render, screen, waitFor, act } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from '@components/app.jsx'
import * as websocketConfig from '@utils/websocket-config.js'

// Mock the ScenarioForm component
vi.mock('@components/ScenarioForm.jsx', () => ({
  default: ({ onSubmit, isConnected, isAnalyzing }) => (
    <div data-testid="mock-scenario-form">
      <span>Connected: {isConnected ? 'Yes' : 'No'}</span>
      <span>Analyzing: {isAnalyzing ? 'Yes' : 'No'}</span>
      <button
        onClick={() => onSubmit('mock-base64', 'mock-environment')}
        data-testid="mock-submit"
      >
        Submit Analysis
      </button>
    </div>
  )
}))

describe('App Component', () => {
  let mockWebSocket
  const defaultWsUrl = 'ws://localhost:8000/ws'

  beforeEach(() => {
    // Mock window.location for relative URL tests
    Object.defineProperty(window, 'location', {
      writable: true,
      value: {
        protocol: 'http:',
        host: 'localhost:3000'
      }
    })

    // Reset WebSocket mock
    mockWebSocket = {
      send: vi.fn(),
      close: vi.fn(),
      readyState: WebSocket.OPEN,
      onopen: null,
      onmessage: null,
      onerror: null,
      onclose: null
    }

    global.WebSocket = vi.fn(() => mockWebSocket)
  })

  afterEach(() => {
    vi.clearAllMocks()
  })

  it('renders main title and components', () => {
    render(<App />)

    expect(screen.getByText('🌱 AgroTech AI Agents Demo')).toBeInTheDocument()
    expect(screen.getByTestId('mock-scenario-form')).toBeInTheDocument()
  })

  it('renders agent cards with loading state initially', () => {
    render(<App />)

    expect(screen.getByText('📸 ImageVision')).toBeInTheDocument()
    expect(screen.getByText('🔍 AgriVision')).toBeInTheDocument()
    expect(screen.getByText('🌍 SoilSense')).toBeInTheDocument()
    expect(screen.getByText('🧠 CropMaster')).toBeInTheDocument()

    // Check for loading/skeleton states (divs with animate-pulse class)
    const loadingElements = document.querySelectorAll('.animate-pulse')
    expect(loadingElements.length).toBeGreaterThan(0)
  })

  it('establishes WebSocket connection on mount', async () => {
    // Mock the helper to return the expected URL
    vi.spyOn(websocketConfig, 'getWebSocketUrl').mockReturnValue(defaultWsUrl)

    render(<App />)

    await waitFor(() => {
      expect(global.WebSocket).toHaveBeenCalledWith(defaultWsUrl)
    })

    // Clean up mock
    websocketConfig.getWebSocketUrl.mockRestore()
  })

  it('uses environment variable for WebSocket URL when available', async () => {
    const customUrl = 'ws://custom-server:9000/ws'

    // Mock environment variable
    vi.spyOn(websocketConfig, 'getWebSocketUrl').mockReturnValue(customUrl)

    render(<App />)

    await waitFor(() => {
      expect(global.WebSocket).toHaveBeenCalledWith(customUrl)
    })

    // Restore mock
    websocketConfig.getWebSocketUrl.mockRestore()
  })

  it('uses relative URL when no environment variable is set', async () => {
    // Mock the helper to return relative URL
    vi.spyOn(websocketConfig, 'getWebSocketUrl').mockReturnValue('ws://localhost:3000/ws')

    render(<App />)

    await waitFor(() => {
      expect(global.WebSocket).toHaveBeenCalledWith('ws://localhost:3000/ws')
    })

    websocketConfig.getWebSocketUrl.mockRestore()
  })

  it('handles successful WebSocket connection', async () => {
    render(<App />)

    await waitFor(() => {
      expect(mockWebSocket.onopen).toBeDefined()
    })

    // Simulate successful connection
    act(() => {
      mockWebSocket.onopen()
    })

    await waitFor(() => {
      expect(screen.getByText('Connected: Yes')).toBeInTheDocument()
    })
  })

  it('handles agent result messages', async () => {
    render(<App />)

    // Wait for WebSocket setup
    await waitFor(() => {
      expect(mockWebSocket.onmessage).toBeDefined()
    })

    // Simulate agent result message
    const mockMessage = {
      data: JSON.stringify({
        type: 'agent_result',
        agent: 'ImageVision',
        data: {
          crop_type: 'corn',
          health_status: 'healthy',
          confidence: 0.95
        }
      })
    }

    act(() => {
      mockWebSocket.onmessage(mockMessage)
    })

    await waitFor(() => {
      expect(screen.getByText('corn')).toBeInTheDocument()
      expect(screen.getByText('healthy')).toBeInTheDocument()
    })
  })

  it('handles status messages', async () => {
    render(<App />)

    await waitFor(() => {
      expect(mockWebSocket.onmessage).toBeDefined()
    })

    // Simulate status message indicating completion
    const statusMessage = {
      data: JSON.stringify({
        type: 'status',
        message: 'Análisis completado exitosamente'
      })
    }

    act(() => {
      mockWebSocket.onmessage(statusMessage)
    })

    await waitFor(() => {
      expect(screen.getByText('Analyzing: No')).toBeInTheDocument()
    })
  })

  it('handles WebSocket error messages', async () => {
    render(<App />)

    await waitFor(() => {
      expect(mockWebSocket.onmessage).toBeDefined()
    })

    const errorMessage = {
      data: JSON.stringify({
        type: 'error',
        message: 'Server error occurred'
      })
    }

    act(() => {
      mockWebSocket.onmessage(errorMessage)
    })

    // Error handling should not crash the app
    expect(screen.getByText('🌱 AgroTech AI Agents Demo')).toBeInTheDocument()
  })

  it('sends image analysis request through WebSocket', async () => {
    const user = userEvent.setup()
    render(<App />)

    // Wait for connection to be established
    await waitFor(() => {
      expect(mockWebSocket.onopen).toBeDefined()
    })

    act(() => {
      mockWebSocket.onopen()
    })

    await waitFor(() => {
      expect(screen.getByText('Connected: Yes')).toBeInTheDocument()
    })

    // Trigger analysis submission
    const submitButton = screen.getByTestId('mock-submit')
    await user.click(submitButton)

    await waitFor(() => {
      expect(mockWebSocket.send).toHaveBeenCalledWith(
        JSON.stringify({
          type: 'image_analysis',
          image_data: 'mock-base64',
          environment_description: 'mock-environment'
        })
      )
    })

    // Should start analyzing
    await waitFor(() => {
      expect(screen.getByText('Analyzing: Yes')).toBeInTheDocument()
    })
  })

  it('handles WebSocket connection errors', async () => {
    render(<App />)

    await waitFor(() => {
      expect(mockWebSocket.onerror).toBeDefined()
    })

    act(() => {
      mockWebSocket.onerror(new Error('Connection failed'))
    })

    // Component should still render properly
    expect(screen.getByText('🌱 AgroTech AI Agents Demo')).toBeInTheDocument()
  })

  it('handles WebSocket connection close with reconnection', async () => {
    render(<App />)

    await waitFor(() => {
      expect(mockWebSocket.onclose).toBeDefined()
    })

    // Simulate connection close (not normal closure - should trigger reconnection)
    act(() => {
      mockWebSocket.onclose({ code: 1006, reason: 'Connection lost' })
    })

    // Should show disconnected state
    await waitFor(() => {
      expect(screen.getByText('Connected: No')).toBeInTheDocument()
    })
  })

  it('maintains stable connection without unnecessary closes', async () => {
    render(<App />)

    // Establish initial connection
    await waitFor(() => {
      expect(mockWebSocket.onopen).toBeDefined()
    })

    act(() => {
      mockWebSocket.onopen()
    })

    await waitFor(() => {
      expect(screen.getByText('Connected: Yes')).toBeInTheDocument()
    })

    // Verify connection was created
    expect(global.WebSocket).toHaveBeenCalledTimes(1)

    // Simulate some normal app activity (message handling)
    const testMessage = {
      data: JSON.stringify({
        type: 'status',
        message: 'Processing...'
      })
    }

    act(() => {
      mockWebSocket.onmessage(testMessage)
    })

    // Connection should remain stable - no close() calls during normal operation
    expect(mockWebSocket.close).not.toHaveBeenCalled()
    expect(screen.getByText('Connected: Yes')).toBeInTheDocument()
  })

  it('prevents submission when WebSocket is not connected', async () => {
    const user = userEvent.setup()
    render(<App />)

    // Don't establish connection
    const submitButton = screen.getByTestId('mock-submit')
    await user.click(submitButton)

    // Should not send any WebSocket message
    expect(mockWebSocket.send).not.toHaveBeenCalled()
  })

  it('cleans up WebSocket connection on unmount', () => {
    const { unmount } = render(<App />)

    unmount()

    expect(mockWebSocket.close).toHaveBeenCalledWith(1000, 'Component unmounting')
  })

  it('does not close WebSocket connection during normal operation', async () => {
    render(<App />)

    // Establish connection
    await waitFor(() => {
      expect(mockWebSocket.onopen).toBeDefined()
    })

    act(() => {
      mockWebSocket.onopen()
    })

    await waitFor(() => {
      expect(screen.getByText('Connected: Yes')).toBeInTheDocument()
    })

    // During normal operation, close should not be called
    expect(mockWebSocket.close).not.toHaveBeenCalled()
  })

  it('sets up heartbeat mechanism on connection', async () => {
    // Mock setInterval to verify heartbeat setup
    const setIntervalSpy = vi.spyOn(global, 'setInterval')
    render(<App />)

    await waitFor(() => {
      expect(mockWebSocket.onopen).toBeDefined()
    })

    // Simulate connection - this should set up heartbeat interval
    act(() => {
      mockWebSocket.onopen()
    })

    // Verify connection is established
    await waitFor(() => {
      expect(screen.getByText('Connected: Yes')).toBeInTheDocument()
    })

    // Verify setInterval was called for heartbeat (should be called for 4000ms)
    expect(setIntervalSpy).toHaveBeenCalledWith(expect.any(Function), 4000)

    setIntervalSpy.mockRestore()
  })

  it('renders DecisionPanel when CropMaster data is available', async () => {
    render(<App />)

    await waitFor(() => {
      expect(mockWebSocket.onmessage).toBeDefined()
    })

    // Simulate CropMaster result with decision data
    const cropMasterMessage = {
      data: JSON.stringify({
        type: 'agent_result',
        agent: 'CropMaster',
        data: {
          overall_status: 'good',
          priority_actions: ['Water the crops', 'Apply fertilizer'],
          recommendations: 'Continue current care routine'
        }
      })
    }

    act(() => {
      mockWebSocket.onmessage(cropMasterMessage)
    })

    await waitFor(() => {
      expect(screen.getByText('📊 Decisión Final del Sistema')).toBeInTheDocument()
      expect(screen.getByText('Water the crops')).toBeInTheDocument()
      expect(screen.getByText('Apply fertilizer')).toBeInTheDocument()
    })
  })
})
