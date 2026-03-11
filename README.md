# Spire.OCR for Python: High-Accuracy OCR API for Efficient Text Extraction from Images

![Spire.OCR for Python](https://i.imgur.com/hSbCEmL.png)

[Product Page](https://www.e-iceblue.com/Introduce/ocr-for-python.html) 丨 [Documentation](https://www.e-iceblue.com/Tutorials.html) 丨 [Examples](https://github.com/eiceblue/Spire.OCR-for-Python) 丨 [Forum](https://www.e-iceblue.com/forum/spire-ocr-f14.html) 丨 [Temporary License](https://www.e-iceblue.com/TemLicense.html) 丨 [Customized Demo](https://www.e-iceblue.com/Misc/customized-demo.html)

**[Spire.OCR for Python](https://www.e-iceblue.com/Introduce/ocr-for-python.html)** is a robust and professional Optical Character Recognition (OCR) library designed to enable developers to extract text from images in various formats, including JPG, PNG, GIF, BMP, and TIFF. This library provides an intuitive and straightforward solution for integrating OCR capabilities into Python applications, allowing users to easily extract text from popular image formats.

## Key Features
- **Text Extraction:** Extract text from images with support for commonly used fonts such as Arial, Times New Roman, Courier New, Verdana, Tahoma, and Calibri, in regular, bold, and italic styles.
- **Multilingual Support:** Recognize text in multiple languages, including English, Chinese, French, German, Japanese, and Korean, making it suitable for global applications.
- **Image Format Compatibility:** Supports extraction of text from a wide range of image file formats like JPG, PNG, BMP, GIF, and TIFF.
- **Cross-Platform:** Compatible with OCR feature on Windows, Linux and Mac operating systems.
- **Easy Integration:** Seamlessly integrate Spire.OCR for Python into your projects with a simple API that requires minimal coding effort.

## Supported Languages:
- English
- Chinese
- Japanese
- Korean
- German
- French

## Supported Fonts:
Commonly used fonts are supported, such as:
- Arial
- Times New Roman
- Courier New
- Verdana
- Tahoma
- Calibri

## Supported Font Styles:
- Regular
- Bold
- Italic

## Supported Image File Formats:
- JPG
- PNG
- BMP
- GIF
- TIFF

## Installation
To install Spire.OCR for Python, you can use pip, the Python package manager. Simply run the following command:

```shell
pip install Spire.OCR
```

Or manually [download Spire.OCR for Python](https://www.e-iceblue.com/Download/ocr-for-python.html) and import it into your project.


## Examples
**Extract Text from an Image File**
```python
from spire.ocr import *

scanner = OcrScanner()

configureOptions = ConfigureOptions()
configureOptions.ModelPath = r"D:\OCR\win-x64"
configureOptions.Language = "English"
scanner.ConfigureDependencies(configureOptions)

scanner.Scan(r"Data\Sample.png")

#output the text and the blocks
text = scanner.Text.ToString() + "\n"
for block in scanner.Text.Blocks:
    rectangle = block.Box
    postions = f"{block.Text} -> x : {rectangle.X} , y : {rectangle.Y} , w : {rectangle.Width} , h : {rectangle.Height}"
    text += postions + "\n"

with open('output.txt','a',encoding='utf-8') as file:
    file.write(text+ "\n")
```

**Extract Text from an Image Stream**
```python
from spire.ocr import *

scanner = OcrScanner()
configureOptions = ConfigureOptions()

configureOptions.ModelPath = r"D:\OCR\win-x64"
configureOptions.Language = "Japan"
scanner.ConfigureDependencies(configureOptions)

image_stream = Stream(r"Data\JapaneseSample.png")
image_format = OCRImageFormat.Png

scanner.Scan(image_stream,image_format)
text = scanner.Text.ToString()

with open('output.txt','a',encoding='utf-8') as file:
    file.write(text)
```

[Product Page](https://www.e-iceblue.com/Introduce/ocr-for-python.html) 丨 [Documentation](https://www.e-iceblue.com/Tutorials.html) 丨 [Examples](https://github.com/eiceblue/Spire.OCR-for-Python) 丨 [Forum](https://www.e-iceblue.com/forum/spire-ocr-f14.html) 丨 [Temporary License](https://www.e-iceblue.com/TemLicense.html) 丨 [Customized Demo](https://www.e-iceblue.com/Misc/customized-demo.html)

