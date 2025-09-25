import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components'),
      '@utils': path.resolve(__dirname, './src/utils'),
      '@tests': path.resolve(__dirname, './tests'),
      '~': path.resolve(__dirname, './')
    }
  },
  server: {
    port: 3000,
    host: '0.0.0.0',
    open: false
  },
  test: {
    globals: true,
    environment: 'jsdom',
    setupFiles: ['./tests/test-setup.js'],
    css: true,
    testTimeout: 10000,
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html', 'lcov'],
      exclude: [
        'node_modules/',
        'dist/',
        'coverage/',
        '**/*.config.js',
        '**/*.config.ts',
        'tests/test-setup.js'
      ],
      thresholds: {
        global: {
          branches: 70,
          functions: 70,
          lines: 70,
          statements: 70
        }
      }
    },
    include: ['tests/**/*.{test,spec}.{js,jsx,ts,tsx}'],
    exclude: [
      'node_modules',
      'dist',
      '.idea',
      '.git',
      '.cache'
    ],
    server: {
      deps: {
        inline: ['@testing-library/user-event']
      }
    }
  }
})
