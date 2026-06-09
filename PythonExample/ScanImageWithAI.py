from spire.ocr import *
import xml.etree.ElementTree as ET

def update_config(file_path, model, api_key, api_url):
    """Update ocr.xml with AI model settings"""
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Update configuration nodes
    root.find('./configs/model').text = model
    root.find('./configs/apiKey').text = api_key
    root.find('./configs/apiUrl').text = api_url

    tree.write(file_path, encoding='utf-8', xml_declaration=True)
    print("Config updated!")


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

# Main execution
if __name__ == "__main__":
    # File paths
    image = r"Data\JapaneseSample.png"
    output = "output.txt"
    config_dir = r"D:\OCR\AI"
    config_file = config_dir + r"\ocr.xml"

    # AI model settings
    model = "AIModel"
    api_key = "ApiKey"
    api_url = "ApiUrl"

    # Run OCR
    update_config(config_file, model, api_key, api_url)
    scan_image(image, output, config_dir)