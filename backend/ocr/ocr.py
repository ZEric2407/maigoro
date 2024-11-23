from google.cloud import vision

from translate.translator import *

IMAGES_PATH = "images\\"

def detect_text(path, src_lang="", target_lang="en"):
    client = vision.ImageAnnotatorClient()

    with open(f"{IMAGES_PATH}{path}", "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content, image_context={"language_hints" : [src_lang]} if src_lang else {})

    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    if not texts:
        return
    
    src_lang = src_lang if src_lang else texts[0].locale
    original_text = "\n".join([f"\n'{text.description}'" for text in texts])
    
    transaction = model.text_translation()
    transaction.original_text = original_text
    transaction.src_language = src_lang
    transaction.target_language = target_lang
    transaction.image_url = f"{IMAGES_PATH}{path}"

    translate(transaction)

    print(transaction.jsoninfy())
    return transaction


if __name__ == "__main__":
    detect_text("oeuf.png", target_lang="en")
