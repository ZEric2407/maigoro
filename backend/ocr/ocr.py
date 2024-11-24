import os
from google.cloud import vision
from model import TextTransaction, LandmarkTransaction

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
IMAGES_PATH = "images\\"

def detect_text(path, src_lang="", target_lang="en"):
    response = load_image(path=path, is_landmark=False, src_lang=src_lang)
    texts = response.text_annotations
    
    if not texts:
        return
    
    src_lang = src_lang if src_lang else texts[0].locale
    original_text = texts[0].description

    transaction = TextTransaction()
    transaction.original_text = original_text
    transaction.src_language = src_lang
    transaction.target_language = target_lang
    transaction.image_url = f"{IMAGES_PATH}{path}"
    
    return transaction

def detect_landmark(path):
    response = load_image(path=path, is_landmark=True)
    landmarks = response.landmark_annotations
    return [LandmarkTransaction(landmark.description) for landmark in landmarks]     

def load_image(path, is_landmark, src_lang=""):
    client = vision.ImageAnnotatorClient()
    func = client.landmark_detection if is_landmark else client.text_detection
    with open(f"{IMAGES_PATH}{path}", "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = func(image=image, image_context={"language_hints" : [src_lang]} if src_lang else {})
    return response

if __name__ == "__main__":
    detect_text("oeuf.png", target_lang="en")
