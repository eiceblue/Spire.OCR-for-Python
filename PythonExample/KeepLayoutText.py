from spire.ocr import *

#Create an instance of OcrScanner
scanner = OcrScanner()

# Set up scanner configuration
configureOptions = ConfigureOptions()
# Set up scanner configuration
configureOptions.ModelPath = r"D:\OCR\win-x64"
# Specify the language for text recognition, default is English (supported languages: English, Chinese, ChineseTraditional, French, German, Japanese, and Korean)
configureOptions.Language = "English"
# Apply the configuration to the scanner
scanner.ConfigureDependencies(configureOptions)

scanner.Scan(r"Data\KeepLayoutText.png")

# Create a VisualTextAligner object to align and format the recognized text
visualText = VisualTextAligner(scanner.Text)

# Convert the aligned visual text object to a string
text = visualText.ToString()

with open(r'output.txt','a',encoding='utf-8') as file:
    file.write(text+ "\n")
