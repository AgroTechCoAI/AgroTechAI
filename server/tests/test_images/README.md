# Test Images for Acceptance Tests

This directory contains test images for the AgroTech AI acceptance tests.

## Required Test Images

To run the acceptance tests, you need to add the following test images to this directory:

### Agricultural Images
- `sample_crop.jpg` - Image of a crop/agricultural field
- `sample_plant.jpg` - Close-up image of a plant
- `tomato_plant.jpg` - Image of tomato plants (optional)
- `corn_field.jpg` - Image of corn field (optional)

### Non-Agricultural Images (for negative testing)
- `invalid_image.txt` - Text file to test invalid file handling
- `random_object.jpg` - Image of non-agricultural subject

## Image Requirements

- **Format**: JPEG, PNG, or other common image formats
- **Size**: Preferably under 5MB for faster testing
- **Content**: Real agricultural images work best for testing the AI agents
- **Resolution**: 800x600 or higher recommended

## Sources for Test Images

You can obtain test images from:

1. **Your own agricultural photos**
2. **Free stock photo sites**:
   - Unsplash (unsplash.com)
   - Pexels (pexels.com)
   - Pixabay (pixabay.com)
3. **Agricultural research datasets** (with proper licensing)

## Example Commands to Download Test Images

```bash
# Navigate to test images directory
cd server/tests/acceptance/test_images/

# Download sample images (replace URLs with actual free stock photos)
wget -O sample_crop.jpg "https://example.com/crop-image.jpg"
wget -O sample_plant.jpg "https://example.com/plant-image.jpg"

# Create invalid test file
echo "This is not an image" > invalid_image.txt
```

## Usage in Tests

The acceptance tests automatically look for images in this directory. If images are missing, those specific tests will be skipped.
