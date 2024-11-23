import os
import model

from google.cloud import translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials.json"

def translate(instance):
    client = translate.Client()
    translation = client.translate(instance.original_text, source_language=instance.source_language, 
                                   target_language=instance.target_language)
    instance.translated_text = translation
    
