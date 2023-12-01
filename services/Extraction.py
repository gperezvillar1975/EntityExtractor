from dataclasses import dataclass
from interfaces.IEntityExtractor import IEntityExtractor, IEntityExtractorResult

@dataclass
class ExtractionService():

    def doExtraction( self, text : str, Extractor : IEntityExtractor):
        
        return Extractor.extractEntities( text )