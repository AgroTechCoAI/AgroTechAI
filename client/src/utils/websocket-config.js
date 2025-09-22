// WebSocket configuration utility
// Supports both local development (with env vars) and Docker deployment (relative URLs)

/**
 * Gets the appropriate WebSocket URL based on environment
 * @returns {string} WebSocket URL
 */
export const getWebSocketUrl = () => {
    // Priority 1: Environment variable (for local development)
    if (import.meta.env.VITE_WEBSOCKET_URL) {
        return import.meta.env.VITE_WEBSOCKET_URL;
    }

    // Priority 2: Relative URL for Docker/production (same-origin)
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    return `${protocol}//${window.location.host}/ws`;
};

/**
 * Gets the appropriate API base URL
 * @returns {string} API base URL
 */
export const getApiBaseUrl = () => {
    // Priority 1: Environment variable (for local development)
    if (import.meta.env.VITE_API_URL) {
        return import.meta.env.VITE_API_URL;
    }

    // Priority 2: Relative URL for Docker/production (same-origin)
    const protocol = window.location.protocol;
    return `${protocol}//${window.location.host}/api`;
};
