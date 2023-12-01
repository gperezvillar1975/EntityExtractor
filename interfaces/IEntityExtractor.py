from abc import ABC,abstractmethod, abstractproperty

class IEntityExtractorResult(ABC):
    @abstractproperty
    def AddEntities(self, word: str, label: str, explain: str):
        pass
    @abstractmethod
    def result(self) -> str:
        pass
    @abstractmethod
    def toJson(self) -> str:
        pass


class IEntityExtractor(ABC):
    @abstractmethod
    def extractEntities( self, text: str ) -> IEntityExtractorResult:
        pass
