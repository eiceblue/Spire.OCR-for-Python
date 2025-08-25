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

