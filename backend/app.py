import os
import base64
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import uuid
import ocr.ocr
import translate.translator
import repository
from model import app, db
import logging
# import openai.openai_client

# Flask app configuration
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

logging.basicConfig(level=logging.DEBUG)

@app.route("/api/translate", methods=["POST"])
def translate_picture():
    try:
        logging.debug("Parsing JSON data from request")
        data = request.json
        image_data = data.get("image")
        src_lang = data.get("source_lang")
        target_lang = data.get("target_lang")

        if not image_data:
            logging.error("Image data not provided")
            return jsonify({"error": "Image data is required"}), 400

        logging.debug("Decoding base64 image")
        image_data = image_data.split(",")[1]
        filename = secure_filename(f"{uuid.uuid4().hex}.png")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        with open(filepath, "wb") as f:
            f.write(base64.b64decode(image_data))

        logging.debug(f"Image saved at {filepath}")

        logging.debug("Calling OCR detect_text")
        transaction = ocr.ocr.detect_text(filepath, src_lang=src_lang, target_lang=target_lang)

        logging.debug("Calling translator")
        translate.translator.translator(transaction)

        logging.debug("Saving transaction")
        repository.save(transaction)

        logging.debug("Transaction completed successfully")
        return jsonify({"transaction": str(transaction)}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/landmark", methods=["POST"])
def describe_landmark():
    try:
        # Parse JSON data from the request
        data = request.json
        url = data.get("URL")  # Use .get() to avoid KeyError
        transactions = ocr.ocr.detect_landmark(url)
        repository.save_all(transactions)
        return transactions
    
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve uploaded images."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    with app.app_context():
        # Example for testing OCR and translation
        transaction = ocr.ocr.detect_text("spanish.jpg", target_lang="en")
        translate.translator.translator(transaction)
        print(str(transaction))
        repository.save(transaction)
    app.run(host="0.0.0.0", port=5000, debug=True)
