import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import ImageUpload from '@components/ImageUpload.jsx'

describe('ImageUpload Component', () => {
  const mockOnImageSelect = vi.fn()

  beforeEach(() => {
    mockOnImageSelect.mockClear()
  })

  it('renders upload area when no image is selected', () => {
    render(
      <ImageUpload
        onImageSelect={mockOnImageSelect}
        selectedImage={null}
        disabled={false}
      />
    )

    expect(screen.getByText('📸 Imagen del Cultivo')).toBeInTheDocument()
    expect(screen.getByText('Haz clic para subir')).toBeInTheDocument()
    expect(screen.getByText('o arrastra y suelta')).toBeInTheDocument()
    expect(screen.getByText('PNG, JPG, GIF hasta 10MB')).toBeInTheDocument()
  })

  it('renders selected image when provided', () => {
    const mockImageSrc = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg=='

    render(
      <ImageUpload
        onImageSelect={mockOnImageSelect}
        selectedImage={mockImageSrc}
        disabled={false}
      />
    )

    const image = screen.getByAltText('Imagen seleccionada')
    expect(image).toBeInTheDocument()
    expect(image).toHaveAttribute('src', mockImageSrc)
  })

  it('calls onImageSelect when file is selected', async () => {
    const user = userEvent.setup()

    render(
      <ImageUpload
        onImageSelect={mockOnImageSelect}
        selectedImage={null}
        disabled={false}
      />
    )

    const file = new File(['test'], 'test.png', { type: 'image/png' })
    const input = document.querySelector('input[type="file"]')

    await user.upload(input, file)

    await waitFor(() => {
      expect(mockOnImageSelect).toHaveBeenCalledTimes(1)
    })
  })

  it('handles drag and drop functionality', async () => {
    render(
      <ImageUpload
        onImageSelect={mockOnImageSelect}
        selectedImage={null}
        disabled={false}
      />
    )

    const dropZone = screen.getByText('Haz clic para subir').closest('button')
    const file = new File(['test'], 'test.png', { type: 'image/png' })

    // Test drag enter
    fireEvent.dragEnter(dropZone, {
      dataTransfer: {
        files: [file]
      }
    })

    // Test drag over
    fireEvent.dragOver(dropZone, {
      dataTransfer: {
        files: [file]
      }
    })

    // Test drop
    fireEvent.drop(dropZone, {
      dataTransfer: {
        files: [file]
      }
    })

    await waitFor(() => {
      expect(mockOnImageSelect).toHaveBeenCalledTimes(1)
    })
  })

  it('removes image when remove button is clicked', async () => {
    const user = userEvent.setup()
    const mockImageSrc = 'data:image/png;base64,test'

    render(
      <ImageUpload
        onImageSelect={mockOnImageSelect}
        selectedImage={mockImageSrc}
        disabled={false}
      />
    )

    const removeButton = document.querySelector('button')
    await user.click(removeButton)

    expect(mockOnImageSelect).toHaveBeenCalledWith(null, null)
  })

  it('disables interactions when disabled prop is true', () => {
    render(
      <ImageUpload
        onImageSelect={mockOnImageSelect}
        selectedImage={null}
        disabled={true}
      />
    )

    const input = document.querySelector('input[type="file"]')
    expect(input).toBeDisabled()
  })

  it('shows alert for invalid file types', async () => {
    userEvent.setup()
    const alertSpy = vi.spyOn(window, 'alert').mockImplementation(() => {})

    render(
      <ImageUpload
        onImageSelect={mockOnImageSelect}
        selectedImage={null}
        disabled={false}
      />
    )

    const file = new File(['test'], 'test.txt', { type: 'text/plain' })
    const input = document.querySelector('input[type="file"]')

    // Use fireEvent for file input change to trigger validation
    fireEvent.change(input, { target: { files: [file] } })

    // Wait for the alert to be called
    await waitFor(() => {
      expect(alertSpy).toHaveBeenCalledWith('Por favor selecciona un archivo de imagen válido')
    })

    expect(mockOnImageSelect).not.toHaveBeenCalled()

    alertSpy.mockRestore()
  })

  it('applies correct CSS classes for drag states', () => {
    render(
      <ImageUpload
        onImageSelect={mockOnImageSelect}
        selectedImage={null}
        disabled={false}
      />
    )

    const dropZone = screen.getByText('Haz clic para subir').closest('button')

    // Test initial state
    expect(dropZone).toHaveClass('border-gray-300')

    // Test drag active state
    fireEvent.dragEnter(dropZone)
    expect(dropZone).toHaveClass('border-green-400', 'bg-green-50')
  })

  it('handles disabled state correctly when image is selected', () => {
    const mockImageSrc = 'data:image/png;base64,test'

    render(
      <ImageUpload
        onImageSelect={mockOnImageSelect}
        selectedImage={mockImageSrc}
        disabled={true}
      />
    )

    const removeButton = document.querySelector('button')
    expect(removeButton).toHaveClass('disabled:opacity-50')
  })
})
