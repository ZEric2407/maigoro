import json

class text_translation:
    def __init__(self, src_language = "en", target_language = "en", cultural_significance = "", image_url = "", original_text = "",
                 translated_text = ""):
        self._src_language = src_language
        self._target_language = target_language
        self._cultural_significance = cultural_significance
        self._image_url = image_url
        self._original_text = original_text
        self._translated_text = translated_text

    @property
    def src_language(self):
        return self._src_language
    
    @src_language.setter
    def src_language(self, lang):
        self._src_language = lang
    
    @property
    def target_language(self):
        return self._target_language
    
    @target_language.setter
    def target_language(self, lang):
        self._target_language = lang
    
    @property
    def cultural_significance(self):
        return self._cultural_significance
    
    @target_language.setter
    def cultural_significance(self, trivia):
        self._cultural_significance = trivia

    @property
    def image_url(self):
        return self._image_url
    
    @image_url.setter
    def image_url(self, url):
        self._image_url = url

    @property
    def original_text(self):
        return self._original_text
    
    @original_text.setter
    def original_text(self, txt):
        self._original_text = txt

    @property
    def translated_text(self):
        return self._translated_text
    
    @translated_text.setter
    def translated_text(self, txt):
        self._translated_text = txt

    def __string__(self):
        fields = {field.strip("_") : val for field, val in self.__dict__.items()}
        return json.dumps(fields)