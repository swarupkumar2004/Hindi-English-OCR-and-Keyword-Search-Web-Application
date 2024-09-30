import easyocr
from PIL import Image
import numpy as np

# Initialize EasyOCR Reader for Hindi and English
reader = easyocr.Reader(['en', 'hi'])

def process_image(image: Image.Image):
    # Convert the image to a numpy array
    img_array = np.array(image)

    # Perform OCR using EasyOCR
    results = reader.readtext(img_array)

    # Extract the detected text
    extracted_text = ' '.join([result[1] for result in results])
    return extracted_text
