from pydantic import BaseModel
from typing import List, Dict


# search
class SearchRequest(BaseModel):
    '''Search message: WEB-server -> Processor'''

    text      : str
    top_k     : int = 3
    filter_by : str | None = None
    keywords  : List[str] = []


class ProcessedSearchRequest(BaseModel):
    '''Search message: Processor -> WEB-server -> DataBase'''

    vector    : List[float]
    top_k     : int = 3
    filter_by : str | None = None
    keywords  : List[str] = []


class SearchAnswer(BaseModel):
    '''Search message: DataBase -> WEB-server'''

    success   : bool
    content   : List[str]
    count     : int


# index
class IndexRequest(BaseModel):
    '''Index message: WEB-server -> DataBase'''

    content   : str
    queries   : List[str]  = []
    keywords  : List[Dict[str, str]]  = []
    chunk_id  : str | None = None


class ProcessedIndexRequest(BaseModel):
    '''Index message: Processor -> WEB-server -> DataBase'''

    vector    : List[float]
    content   : str
    queries   : List[str]  = []
    keywords  : List[str]  = []
    chunk_id  : str | None = None


class IndexAnswer(BaseModel):
    '''Index message: DataBase -> WEB-server'''

    success   : bool
