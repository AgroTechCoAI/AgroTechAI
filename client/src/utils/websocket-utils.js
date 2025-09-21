// WebSocket utility functions for AgroTech AI client

export const createWebSocketConnection = (url, callbacks = {}) => {
  const ws = new WebSocket(url)

  // Set binary type for consistent cross-browser behavior
  ws.binaryType = 'arraybuffer'

  ws.onopen = callbacks.onOpen || (() => {})
  ws.onmessage = callbacks.onMessage || (() => {})
  ws.onerror = callbacks.onError || (() => {})
  ws.onclose = callbacks.onClose || (() => {})

  return ws
}

export const sendAnalysisRequest = (websocket, imageData, environmentDescription) => {
  if (websocket && websocket.readyState === WebSocket.OPEN) {
    websocket.send(JSON.stringify({
      type: 'image_analysis',
      image_data: imageData,
      environment_description: environmentDescription
    }))
    return true
  }
  return false
}

export const sendHeartbeat = (websocket) => {
  if (websocket && websocket.readyState === WebSocket.OPEN) {
    websocket.send(JSON.stringify({ type: 'ping' }))
    return true
  }
  return false
}

export const calculateReconnectDelay = (attempt, maxDelay = 30000) => {
  return Math.min(1000 * Math.pow(2, attempt), maxDelay)
}

export const parseWebSocketMessage = (messageData) => {
  try {
    return JSON.parse(messageData)
  } catch (error) {
    console.error('Failed to parse WebSocket message:', error)
    return null
  }
}

export const isWebSocketReady = (websocket) => {
  return !!(websocket && websocket.readyState === WebSocket.OPEN)
}
