import os
import logging
from google.cloud import vision
from model import TextTransaction, LandmarkTransaction

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

def detect_text(path, src_lang="", target_lang="en"):
    try:
        logging.debug(f"Starting text detection for image: {path}")
        response = load_image(path=path, is_landmark=False, src_lang=src_lang)
        texts = response.text_annotations

        if not texts:
            logging.warning("No text detected in the image.")
            return None

        src_lang = src_lang if src_lang else texts[0].locale
        original_text = texts[0].description

        logging.debug(f"Detected text: {original_text}")
        logging.debug(f"Detected language: {src_lang}")

        transaction = TextTransaction()
        transaction.original_text = original_text
        transaction.src_language = src_lang
        transaction.target_language = target_lang
        transaction.image_url = f"{path}"

        logging.info(f"Text detection completed successfully for image: {path}")
        return transaction
    except Exception as e:
        logging.error(f"Error during text detection: {e}")
        raise

def detect_landmark(path):
    try:
        logging.debug(f"Starting landmark detection for image: {path}")
        response = load_image(path=path, is_landmark=True)
        landmarks = response.landmark_annotations

        if not landmarks:
            logging.warning("No landmarks detected in the image.")
            return []

        transactions = [LandmarkTransaction(landmark.description) for landmark in landmarks]
        logging.info(f"Landmark detection completed successfully for image: {path}")
        return transactions
    except Exception as e:
        logging.error(f"Error during landmark detection: {e}")
        raise

def load_image(path, is_landmark, src_lang=""):
    try:
        logging.debug(f"Loading image: {path}")
        client = vision.ImageAnnotatorClient()
        func = client.landmark_detection if is_landmark else client.text_detection
        
        with open(f"{path}", "rb") as image_file:
            content = image_file.read()

        logging.debug(f"Image read successfully: {path}")
        image = vision.Image(content=content)

        if src_lang:
            logging.debug(f"Using language hint: {src_lang}")
            response = func(image=image, image_context={"language_hints": [src_lang]})
        else:
            response = func(image=image)

        logging.debug(f"Image processing completed for: {path}")
        return response
    except FileNotFoundError:
        logging.error(f"Image file not found: {path}")
        raise
    except Exception as e:
        logging.error(f"Error while loading and processing image: {e}")
        raise

if __name__ == "__main__":
    try:
        logging.info("Starting text detection test.")
        transaction = detect_text("oeuf.png", target_lang="en")
        if transaction:
            logging.info(f"TextTransaction: {transaction}")
        else:
            logging.warning("No transaction created. Text detection might have failed.")
    except Exception as e:
        logging.critical(f"Critical error in main execution: {e}")
