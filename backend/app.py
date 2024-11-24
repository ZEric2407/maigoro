import os
import base64
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import uuid
import ocr.ocr
import translate.translator
import repository
from model import app
# import openai.openai_client

# Flask app configuration
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

# Directory to save uploaded images
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/api/translate", methods=["POST"])
def translate_picture():
    try:
        # Parse JSON data from the request
        data = request.json
        image_data = data.get("image")  # Base64 image string
        src_lang = data.get("source_lang")
        target_lang = data.get("target_lang")

        if not image_data:
            return jsonify({"error": "Image data is required"}), 400

        # Decode the base64 image data and save it to the server
        image_data = image_data.split(",")[1]  # Remove "data:image/png;base64," prefix
        filename = secure_filename(f"{uuid.uuid4().hex}.png")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        with open(filepath, "wb") as f:
            f.write(base64.b64decode(image_data))

        # Construct the file URL
        image_url = f"http://localhost:5000/uploads/{filename}"

        # Perform OCR and translation using the image URL
        transaction = ocr.ocr.detect_text(image_url, src_lang=src_lang, target_lang=target_lang)
        translate.translator.translator(transaction)

        # Optionally save the transaction
        repository.save(transaction)

        return jsonify({"transaction": str(transaction)}), 200

    except Exception as e:
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
