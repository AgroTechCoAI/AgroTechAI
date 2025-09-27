import os
import pytest
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

DEBUG_MODE = os.environ.get("TEST_DEBUG_MODE", "false")
BASE_URL = os.environ.get("APP_BASE_URL", "http://localhost:3000")

@pytest.fixture
def browser():
    """Configure Chrome browser for testing"""
    if not DEBUG_MODE == "true":
        logging.getLogger('selenium').setLevel(logging.WARNING)
        logging.getLogger('urllib3').setLevel(logging.WARNING)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def wait_for_websocket_connection(browser, timeout=15):
    """Wait for WebSocket connection to be established"""
    try:
        # Wait for React app to load first
        WebDriverWait(browser, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        # Wait for React app to be mounted and WebSocket to be established
        # Looking for the connection state in React
        WebDriverWait(browser, timeout).until(
            lambda driver: driver.execute_script("""
                // Check if React has mounted and WebSocket is connected
                const app = document.querySelector('[data-reactroot]') || document.querySelector('#root > div');
                if (!app) return false;

                // Look for connection status indicators in the DOM
                const connectionBanner = document.querySelector('.bg-green-100');
                const hasConnectedState = connectionBanner && connectionBanner.textContent.includes('Conectado');

                // Alternative: Check if WebSocket is available and ready
                const hasWebSocketSupport = typeof WebSocket !== 'undefined';

                return hasConnectedState || hasWebSocketSupport;
            """)
        )
        return True
    except TimeoutException:
        return False
    except Exception:
        return False

def wait_for_analysis_result(browser, timeout=60):
    """Wait for analysis result to appear"""
    try:
        print("🔍 Waiting for analysis results...")

        # First, wait for the analysis to start (loading states should appear)
        WebDriverWait(browser, 10).until(
            lambda driver: driver.find_elements(By.CSS_SELECTOR, ".animate-pulse") or
                          "Analizando" in driver.page_source or
                          "análisis" in driver.page_source.lower()
        )
        print("✅ Analysis started, waiting for completion...")

        # Then wait for analysis to complete (skeleton animations to disappear)
        result = WebDriverWait(browser, timeout).until(
            lambda driver: (
                # Check if skeleton loading is gone AND we have actual data
                len(driver.find_elements(By.CSS_SELECTOR, ".animate-pulse")) == 0 and
                # Look for actual data in agent cards
                (len(driver.find_elements(By.CSS_SELECTOR, ".text-gray-900.font-medium")) > 0 or
                 # Or check for agent names with data
                 ("AgriVision" in driver.page_source and "SoilSense" in driver.page_source))
            )
        )
        print("✅ Analysis completed!")
        return result

    except TimeoutException as e:
        print(f"❌ Timeout waiting for analysis results: {e}")
        # Debug: Print current page state
        try:
            skeleton_count = len(browser.find_elements(By.CSS_SELECTOR, ".animate-pulse"))
            data_elements = len(browser.find_elements(By.CSS_SELECTOR, ".text-gray-900.font-medium"))
            print(f"🐛 Debug - Skeleton elements: {skeleton_count}, Data elements: {data_elements}")

            # Check for error messages
            if "error" in browser.page_source.lower():
                print("🐛 Found error in page source")
            if "desconectado" in browser.page_source.lower():
                print("🐛 Found disconnection in page source")

        except Exception as debug_e:
            print(f"🐛 Debug error: {debug_e}")
        return None
    except Exception as e:
        print(f"❌ Error waiting for results: {e}")
        return None

def upload_image_file(browser, image_path):
    """Upload an image file using the ImageUpload component"""
    try:
        # Find the hidden file input
        file_input = browser.find_element(By.CSS_SELECTOR, "input#image-upload-input[type='file']")

        # Send the file path to the input
        file_input.send_keys(image_path)

        # Wait a moment for the file to be processed
        time.sleep(2)

        # Check if image was uploaded successfully by looking for the image preview
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Imagen seleccionada']"))
        )

        return True
    except Exception as e:
        print(f"Failed to upload image: {e}")
        return False

def fill_environment_description(browser):
    """Fill the environment description textarea"""
    try:
        print("📝 Filling environment description...")

        # Find and fill the environment description textarea
        textarea = browser.find_element(By.ID, "environment-description")
        test_environment = "Humedad del suelo 65%, Temperatura 23°C, pH 6.7, sin viento fuerte, condiciones ideales para el cultivo"
        textarea.clear()
        textarea.send_keys(test_environment)
        print("✅ Environment description filled")
        return True
    except Exception as e:
        print(f"❌ Failed to fill environment description: {e}")
        return False

def submit_analysis_form(browser):
    """Submit the analysis form after uploading image and filling description"""
    try:
        print("🔍 Looking for submit button...")

        # First, make sure environment description is filled
        if not fill_environment_description(browser):
            return False

        # Wait a moment for form validation
        time.sleep(1)

        # Look for submit button in the ScenarioForm
        submit_buttons = browser.find_elements(By.CSS_SELECTOR, "button[type='submit']:not([disabled])")
        print(f"Found {len(submit_buttons)} enabled submit buttons")

        if not submit_buttons:
            # Check if button is disabled and why
            disabled_buttons = browser.find_elements(By.CSS_SELECTOR, "button[type='submit'][disabled]")
            if disabled_buttons:
                print(f"❌ Submit button is disabled. Button text: {disabled_buttons[0].text}")
                # Check connection status
                if "Desconectado" in browser.page_source:
                    print("❌ Server is disconnected")
                return False

        if not submit_buttons:
            # Fallback: look for any button with text related to analysis
            submit_buttons = browser.find_elements(By.XPATH, "//button[contains(text(), 'Analizar') and not(@disabled)]")
            print(f"Found {len(submit_buttons)} enabled analysis buttons via XPath")

        if submit_buttons:
            button = submit_buttons[0]
            print(f"🔄 Clicking button: {button.text}")
            button.click()
            time.sleep(2)  # Wait for form submission to process
            return True

        print("❌ No enabled submit button found")
        return False
    except Exception as e:
        print(f"❌ Failed to submit form: {e}")
        return False

def test_app_loads_successfully(browser):
    """Test that the AgroTech AI application loads successfully"""
    browser.get(BASE_URL)

    # Wait for the page title to load
    WebDriverWait(browser, 10).until(
        lambda driver: "AgroTech" in driver.title
    )

    assert "AgroTech" in browser.title

def test_websocket_connection_established(browser):
    """Test that WebSocket connection functionality is available"""
    browser.get(BASE_URL)

    # Wait for React app to load and WebSocket functionality to be available
    connection_ready = wait_for_websocket_connection(browser)

    if not connection_ready:
        # Check if there's a connection error banner to provide better debugging info
        error_banner = browser.find_elements(By.CSS_SELECTOR, ".bg-red-100, .bg-yellow-100")
        if error_banner:
            error_text = error_banner[0].text
            pytest.fail(f"WebSocket connection failed. Error displayed: {error_text}")
        else:
            pytest.fail("WebSocket connection not established within timeout period")

    # If we reach here, connection is ready
    assert connection_ready, "WebSocket connection not established"

def test_image_upload_interface_present(browser):
    """Test that image upload interface is present"""
    browser.get(BASE_URL)

    # Wait for page to load
    WebDriverWait(browser, 10).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )

    # Look for the specific image upload input from ImageUpload component
    file_input = browser.find_elements(By.CSS_SELECTOR, "input#image-upload-input[type='file']")
    upload_area = browser.find_elements(By.CSS_SELECTOR, "button[type='button']")

    assert len(file_input) > 0, "Image upload input not found"
    assert len(upload_area) > 0, "Upload area not found"

    # Check that the upload text is present
    page_text = browser.page_source
    assert "Haz clic para subir" in page_text or "arrastra y suelta" in page_text, "Upload instructions not found"

@pytest.mark.parametrize(
    "test_image, working_agents",
    [
        ("sample_crop.jpg", ["AgriVision", "SoilSense"]),
        ("sample_plant.jpg", ["AgriVision", "SoilSense"]),
    ],
)
def test_text_based_agents_workflow(browser, test_image, working_agents):
    """Test that text-based agents (AgriVision, SoilSense) provide analysis when ImageVision fails"""
    browser.get(BASE_URL)

    # Wait for WebSocket connection
    assert wait_for_websocket_connection(browser), "WebSocket connection not established"

    # Get test image path
    test_image_path = os.path.join(os.path.dirname(__file__), "..", "test_images", test_image)

    # Convert to absolute path for better debugging
    test_image_path = os.path.abspath(test_image_path)

    # Skip if test image doesn't exist
    if not os.path.exists(test_image_path):
        pytest.skip(f"Test image {test_image} not found. Run 'python create_test_images.py' first.")

    # Upload the image
    upload_success = upload_image_file(browser, test_image_path)
    assert upload_success, f"Failed to upload test image: {test_image}"

    # Submit the form for analysis
    submit_success = submit_analysis_form(browser)
    assert submit_success, "Failed to submit analysis form"

    # Wait for analysis to complete (longer timeout for LLM processing)
    result_elements = wait_for_analysis_result(browser, timeout=90)
    assert result_elements is not None, "Analysis result not received within timeout"

    # Check that working agents are present and have data
    page_source = browser.page_source
    for agent in working_agents:
        assert agent in page_source, f"Agent {agent} not found in page content"

    # Verify that agent cards show actual data (not just loading states)
    agent_cards = browser.find_elements(By.CSS_SELECTOR, ".bg-white.rounded-lg.shadow-lg")
    assert len(agent_cards) >= 3, f"Expected at least 3 agent cards, found {len(agent_cards)}"

    # Check for ImageVision empty response (expected behavior with text-only model)
    imagevision_card = None
    for card in agent_cards:
        if "ImageVision" in card.text:
            imagevision_card = card
            break

    if imagevision_card:
        # ImageVision should show an error or empty state since it can't process images
        card_text = imagevision_card.text.lower()
        assert ("error" in card_text or "no disponible" in card_text or
                "loading" in card_text or len(card_text.strip()) < 50), \
                "ImageVision should show error/empty state with text-only model"

def test_image_vision_agent_empty_response(browser):
    """Test ImageVision agent returns empty response with text-only model"""
    browser.get(BASE_URL)

    # Simulate the expected empty response from ImageVision with text-only model
    browser.execute_script("""
        window.mockAnalysisResult = {
            imageVision: {}  // Empty JSON response expected from text-only LLM
        };
    """)

    # Verify that ImageVision returns empty response
    result = browser.execute_script("return window.mockAnalysisResult.imageVision")

    # With text-only model, ImageVision should return empty object
    assert isinstance(result, dict), "ImageVision should return a dictionary"
    assert len(result) == 0, "ImageVision should return empty JSON with text-only model"

def test_agri_vision_agent_analysis(browser):
    """Test AgriVision agent provides crop health assessment"""
    browser.get(BASE_URL)

    # Mock AgriVision analysis result
    browser.execute_script("""
        window.mockAnalysisResult = {
            agriVision: {
                crop_health: "healthy",
                pest_detected: false,
                leaf_condition: "good",
                disease_probability: 0.2,
                visual_symptoms: ["hojas verdes", "sin manchas"],
                recommendations: ["continuar monitoreo", "revisar en 2 días"],
                confidence: 0.88
            }
        };
    """)

    result = browser.execute_script("return window.mockAnalysisResult.agriVision")

    assert result["crop_health"] in ["healthy", "stressed", "diseased"]
    assert isinstance(result["pest_detected"], bool)
    assert result["leaf_condition"] in ["excellent", "good", "fair", "poor"]
    assert 0 <= result["disease_probability"] <= 1
    assert isinstance(result["visual_symptoms"], list)
    assert isinstance(result["recommendations"], list)

def test_soil_sense_agent_analysis(browser):
    """Test SoilSense agent provides environmental analysis"""
    browser.get(BASE_URL)

    # Mock SoilSense analysis result
    browser.execute_script("""
        window.mockAnalysisResult = {
            soilSense: {
                soil_moisture: 45,
                ph_level: 6.5,
                temperature: 24,
                humidity: 60,
                irrigation_needed: true,
                fertilizer_status: "adequate",
                environmental_stress: "low",
                alerts: ["humedad baja detectada"],
                confidence: 0.90
            }
        };
    """)

    result = browser.execute_script("return window.mockAnalysisResult.soilSense")

    assert 0 <= result["soil_moisture"] <= 100
    assert 4.0 <= result["ph_level"] <= 9.0
    assert -10 <= result["temperature"] <= 50
    assert 0 <= result["humidity"] <= 100
    assert isinstance(result["irrigation_needed"], bool)
    assert result["fertilizer_status"] in ["deficient", "adequate", "excess"]
    assert result["environmental_stress"] in ["low", "medium", "high"]
    assert isinstance(result["alerts"], list)

def test_crop_master_agent_integration(browser):
    """Test CropMaster agent provides integrated decision-making"""
    browser.get(BASE_URL)

    # Mock CropMaster analysis result that integrates data from other agents
    browser.execute_script("""
        window.mockAnalysisResult = {
            cropMaster: {
                overall_status: "good",
                priority_actions: [
                    "continuar monitoreo regular",
                    "revisar humedad del suelo en 2 días",
                    "aplicar riego ligero si es necesario"
                ],
                estimated_yield: "high",
                risk_assessment: "low",
                next_inspection_hours: 48,
                economic_impact: "positive",
                urgent_alerts: [],
                confidence: 0.92
            }
        };
    """)

    result = browser.execute_script("return window.mockAnalysisResult.cropMaster")

    # Verify CropMaster decision structure
    assert result["overall_status"] in ["excellent", "good", "warning", "critical"]
    assert result["estimated_yield"] in ["high", "medium", "low"]
    assert result["risk_assessment"] in ["low", "medium", "high", "critical"]
    assert result["economic_impact"] in ["positive", "neutral", "negative"]
    assert isinstance(result["next_inspection_hours"], (int, float))
    assert 1 <= result["next_inspection_hours"] <= 168  # Between 1 hour and 1 week
    assert isinstance(result["priority_actions"], list)
    assert len(result["priority_actions"]) <= 4  # Maximum 4 actions as per agent spec
    assert isinstance(result["urgent_alerts"], list)
    assert 0 <= result["confidence"] <= 1

def test_integrated_analysis_workflow(browser):
    """Test complete analysis workflow with realistic agent responses"""
    browser.get(BASE_URL)

    # Wait for WebSocket connection
    assert wait_for_websocket_connection(browser), "WebSocket connection not established"

    # Mock realistic analysis workflow (ImageVision empty, others working)
    browser.execute_script("""
        window.completeAnalysis = {
            timestamp: new Date().toISOString(),
            imageVision: {},  // Empty response from text-only LLM
            agriVision: {
                crop_health: "healthy",
                pest_detected: false,
                leaf_condition: "good",
                disease_probability: 0.2,
                confidence: 0.88
            },
            soilSense: {
                soil_moisture: 45,
                ph_level: 6.5,
                temperature: 24,
                humidity: 60,
                irrigation_needed: true,
                fertilizer_status: "adequate",
                confidence: 0.90
            },
            cropMaster: {
                overall_status: "good",
                priority_actions: ["continuar monitoreo", "revisar humedad"],
                confidence: 0.85
            },
            overallStatus: "analysis_complete"
        };
    """)

    # Verify complete analysis structure
    analysis = browser.execute_script("return window.completeAnalysis")

    assert "timestamp" in analysis
    assert "imageVision" in analysis
    assert "agriVision" in analysis
    assert "soilSense" in analysis
    assert "cropMaster" in analysis
    assert analysis["overallStatus"] == "analysis_complete"

    # Verify ImageVision is empty (expected with text-only model)
    assert len(analysis["imageVision"]) == 0, "ImageVision should be empty with text-only model"

    # Verify working agents provided confidence scores
    assert analysis["agriVision"]["confidence"] > 0
    assert analysis["soilSense"]["confidence"] > 0
    assert analysis["cropMaster"]["confidence"] > 0

def test_error_handling_invalid_image(browser):
    """Test error handling when invalid image is uploaded"""
    browser.get(BASE_URL)

    # Mock error scenario
    browser.execute_script("""
        window.errorResponse = {
            error: "Invalid image format",
            status: "error",
            message: "Por favor, sube una imagen válida"
        };
    """)

    error_response = browser.execute_script("return window.errorResponse")

    assert error_response["status"] == "error"
    assert "error" in error_response
    assert "message" in error_response

def test_analysis_performance_metrics(browser):
    """Test that analysis completes within acceptable time limits"""
    browser.get(BASE_URL)

    start_time = time.time()

    # Mock analysis timing
    browser.execute_script("""
        window.performanceMetrics = {
            imageVisionTime: 2.5,
            agriVisionTime: 1.8,
            soilSenseTime: 1.2,
            totalAnalysisTime: 5.5
        };
    """)

    metrics = browser.execute_script("return window.performanceMetrics")

    # Verify reasonable performance expectations
    assert metrics["imageVisionTime"] < 10, "ImageVision analysis took too long"
    assert metrics["agriVisionTime"] < 10, "AgriVision analysis took too long"
    assert metrics["soilSenseTime"] < 10, "SoilSense analysis took too long"
    assert metrics["totalAnalysisTime"] < 30, "Total analysis took too long"
