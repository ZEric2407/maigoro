import os
from google.cloud import vision
import model

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
IMAGES_PATH = "images\\"

def detect_text(path, src_lang="", target_lang="en"):
    client = vision.ImageAnnotatorClient()

    with open(f"{IMAGES_PATH}{path}", "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image, image_context={"language_hints" : [src_lang]} if src_lang else {})
    texts = response.text_annotations
    
    if not texts:
        return
    
    src_lang = src_lang if src_lang else texts[0].locale
    original_text = texts[0].description

    transaction = model.TextTransaction()
    transaction.original_text = original_text
    transaction.src_language = src_lang
    transaction.target_language = target_lang
    transaction.image_url = f"{IMAGES_PATH}{path}"
    
    return transaction

if __name__ == "__main__":
    detect_text("oeuf.png", target_lang="en")
