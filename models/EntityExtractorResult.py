from dataclasses import dataclass,field
from interfaces.IEntityExtractor import IEntityExtractorResult
import json

@dataclass 
class EntityExtractorResult(IEntityExtractorResult):
    _entities : list = field(default_factory=list)

    def AddEntities(self, word: str, label: str, explain: str):
        self._entities.append([word,label,explain])
    
    def result(self) -> dict:
        _ret = {
            "entities" : self._entities
        }
        return _ret

    def toJson(self) -> str:
        _ret = {
            "entities" : self._entities
        }
        return json.dumps(_ret,ensure_ascii=False).encode('utf-8')
    
