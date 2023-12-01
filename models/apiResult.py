from dataclasses import dataclass,field
import json

@dataclass
class apiResult():
    _code : str = ""
    _description : str = ""
    _result : dict = field(default_factory=dict)

    @property
    def code( self ) -> str:
        return self._code
    @code.setter
    def code( self, value: str) -> None:
        self._code = value
    @property
    def description( self ) -> str:
        return self._description
    @description.setter
    def description( self, value: str) -> None:
        self._description = value
    @property
    def result( self ) -> dict:
        return self._result
    @result.setter
    def result( self, value: dict) -> None:
        self._result = value        
    
    def toJSON(self):
        _value = {
            "code" : self._code,
            "description" : self.description,
            "result" : self._result
        }
        return json.dumps(_value,ensure_ascii=False).encode('utf-8')