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
