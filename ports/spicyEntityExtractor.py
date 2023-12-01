from dataclasses import dataclass
from interfaces.IEntityExtractor import IEntityExtractor,IEntityExtractorResult
import spacy
from spacy import displacy
from models.EntityExtractorResult import EntityExtractorResult
from bs4 import BeautifulSoup
import html2text

@dataclass
class spicyEntityExtrator(IEntityExtractor):
    _nlpModel = spacy.load('es_core_news_md')
    _result = EntityExtractorResult()
    _textToExtract : str = ""

    def extractEntities( self, text: str ) -> IEntityExtractorResult:
        if text:
            # Si el texto es HTML lo convierte a texto plano
            if bool(BeautifulSoup(text, "html.parser").find()):
                self._textToExtract = html2text.html2text(html=text)
            else:
                self._textToExtract = text

            texto = self._nlpModel(text=text)        
            for word in texto.ents:
                 if word.label_ != 'MISC':
                    self._result.AddEntities(word.text,word.label_,spacy.explain(word.label_))

        return self._result