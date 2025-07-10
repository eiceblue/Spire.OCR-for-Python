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
