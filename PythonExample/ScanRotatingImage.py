from spire.ocr import *

#Create an instance of OcrScanner
scanner = OcrScanner()

# Set up scanner configuration
configureOptions = ConfigureOptions()
#  Set up scanner configuration
configureOptions.ModelPath = r"D:\OCR\win-x64"
# Specify the language for text recognition, default is English (supported languages: English, Chinese, ChineseTraditional, French, German, Japanese, and Korean)
configureOptions.Language = "English"
# Set whether the image rotates or not
configureOptions.AutoRotate = True
# Apply the configuration to the scanner
scanner.ConfigureDependencies(configureOptions)

scanner.Scan(r"Data\RotatingImage.png")

#output the text and the blocks
text = scanner.Text.ToString() + "\n"

with open(r'output.txt','a',encoding='utf-8') as file:
    file.write(text+ "\n")
