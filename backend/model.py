import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
import json

def create_app(config = None):
    app = flask.Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///session.db"
    return app

app = create_app()

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class TextTransaction(Base):
    __tablename__ = "translation"
    _id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement=True)
    _src_language: Mapped[str] = mapped_column(name="src_language")
    _target_language: Mapped[str] = mapped_column(name="target_language")
    _cultural_significance: Mapped[str] = mapped_column(name="cultural_significance")
    _image_url: Mapped[str] = mapped_column(name="image_url")
    _original_text: Mapped[str] = mapped_column(name="original_text")
    _translated_text: Mapped[str] = mapped_column(name="translated_text")

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

    def __str__(self):
        fields = {field.strip("_") : val for field, val in self.__dict__.items() if not field in ["_sa_instance_state"]}
        return json.dumps(fields)
    
class LandmarkTransaction(Base):
    __tablename__ = "landmark"
    _id: Mapped[int] = mapped_column(name="id", primary_key=True, autoincrement=True)
    _description: Mapped[str] = mapped_column(name="description")
    _cultural_significance: Mapped[str] = mapped_column(name="cultural_significance")

    def __init__(self, description = "", cultural_significance = ""):
        self._description = description
        self._cultural_significance = cultural_significance

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, desc):
        self._description = desc

    @property
    def cultural_significance(self):
        return self._cultural_significance
    
    @cultural_significance.setter
    def cultural_significance(self, trivia):
        self._cultural_significance = trivia

    def __str__(self):
        fields = {field.strip("_") : val for field, val in self.__dict__.items() if not field in ["_sa_instance_state"]}
        return json.dumps(fields)

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()