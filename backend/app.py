from flask import Flask, request, jsonify
from flask_cors import CORS
import ocr.ocr
import translate.translator
import repository
from model import app
# import openai.openai_client


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

@app.route("/api/translate", methods=["POST"])
def translate_picture():
    try:
        # Parse JSON data from the request
        data = request.json
        url = data.get("URL")  # Use .get() to avoid KeyError
        src_lang = data.get("source_lang")
        target_lang = data.get("target_lang")

        if not url:
            return jsonify({"error": "URL is required"}), 400

        # Perform OCR and translation
        transaction = ocr.ocr.detect_text(url, src_lang=src_lang, target_lang=target_lang)
        translate.translator.translator(transaction)
        return jsonify({"transaction": str(transaction)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    with app.app_context():
        transaction = ocr.ocr.detect_text("spanish.jpg", target_lang="en")
        translate.translator.translator(transaction)
        print(str(transaction))
        repository.save(transaction)