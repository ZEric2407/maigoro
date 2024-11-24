import flask
import ocr.ocr
import translate.translator
import repository
from model import app
# import openai.openai_client

@app.route("/translate", methods=["POST"])
def translate_picture():
    data = flask.request.form
    url = data["URL"]
    src_lang = data["source_lang"]
    target_lang = data["target_lang"]
    transaction = ocr.ocr.detect_text(url, src_lang=src_lang if src_lang else None, target_lang=target_lang if target_lang else None)
    translate.translator.translator(transaction)
    return str(transaction)

if __name__ == "__main__":
    with app.app_context():
        transaction = ocr.ocr.detect_text("spanish.jpg", target_lang="en")
        translate.translator.translator(transaction)
        print(str(transaction))
        repository.save(transaction)