# Spire.OCR Python Example
## Perform OCR scanning on an image and extract text with position information
```python
# Create OCR scanner
scanner = OcrScanner()

# Configure scanner options
configureOptions = ConfigureOptions()
configureOptions.ModelPath = r"D:\OCR\win-x64"
configureOptions.Language = "English"
scanner.ConfigureDependencies(configureOptions)

# Scan image file
scanner.Scan(r"Data\Sample.png")

# Extract text and block information
text = scanner.Text.ToString() + "\n"
for block in scanner.Text.Blocks:
    rectangle = block.Box
    postions = f"{block.Text} -> x : {rectangle.X} , y : {rectangle.Y} , w : {rectangle.Width} , h : {rectangle.Height}"
    text += postions + "\n"
```

---

# OCR Image Stream Processing
## Perform OCR on an image stream using Spire.OCR library
```python
# Create OCR scanner
scanner = OcrScanner()
configureOptions = ConfigureOptions()

# Set OCR configuration
configureOptions.ModelPath = r"D:\OCR\win-x64"
configureOptions.Language = "Japan"
scanner.ConfigureDependencies(configureOptions)

# Create image stream and set format
image_stream = Stream(r"Data\JapaneseSample.png")
image_format = OCRImageFormat.Png

# Scan image and extract text
scanner.Scan(image_stream, image_format)
text = scanner.Text.ToString()
```

---

# spire.ocr python core functionality
## Keep Layout Text - scan image and produce layout-preserved text
```python
# Create an instance of OcrScanner
scanner = OcrScanner()

# Set up scanner configuration
configureOptions = ConfigureOptions()
# Set the model path for OCR engine
configureOptions.ModelPath = r"D:\OCR\win-x64"
# Specify the language for text recognition, default is English (supported languages: English, Chinese, ChineseTraditional, French, German, Japanese, and Korean)
configureOptions.Language = "English"
# Apply the configuration to the scanner
scanner.ConfigureDependencies(configureOptions)

# Scan an image
scanner.Scan(r"Data\KeepLayoutText.png")

# Create a VisualTextAligner object to align and format the recognized text
visualText = VisualTextAligner(scanner.Text)

# Convert the aligned visual text object to a string
text = visualText.ToString()
```

---

# Spire.OCR Python Core Functionality  
## Scan image with AI model and extract text  

```python
def scan_image(image_path, output_path, config_dir):
    """Scan image and extract text using AI model"""
    scanner = OcrScanner()

    # Setup configuration
    options = ConfigureOptions()
    options.ModelPath = config_dir
    options.Language = "Japanese"
    scanner.ConfigureDependencies(options)

    # Scan and save result
    scanner.Scan(image_path)
    text = scanner.Text.ToString()

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
```

---

# spire.ocr python core functionality  
## Scan rotating image with auto-rotate configuration  
```python
# Create an OCR scanner instance
scanner = OcrScanner()

# Configure scanner with auto-rotate enabled
configureOptions = ConfigureOptions()
configureOptions.AutoRotate = True  # Enable automatic image rotation
scanner.ConfigureDependencies(configureOptions)

# Perform OCR scan on the image
scanner.Scan(r"Data\RotatingImage.png")
```

---

