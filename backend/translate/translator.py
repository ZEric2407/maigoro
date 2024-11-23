import os
import model

from google.cloud import translate_v2 as translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

def translator(instance):
    client = translate.Client()
    translation = client.translate(instance.original_text, source_language=instance.src_language, 
                                   target_language=instance.target_language, format_="text")
    instance.translated_text = translation["translatedText"]
    
