import os

from google.cloud import vision

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"
IMAGES_PATH = "images\\"

def detect_text(path):
    client = vision.ImageAnnotatorClient()

    with open(f"{IMAGES_PATH}{path}", "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print("Texts:")

    for text in texts:
        print(f"\n'{text.description}'")

if __name__ == "__main__":
    pass
