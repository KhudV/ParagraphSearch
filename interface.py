from pydantic import BaseModel
from typing import List


# class SearchRequest:
#     '''Message: WEB-server -> DataBase'''

#     def __init__(
#         self,
#         text      : str,
#         top_k     : int,
#         filter_by : Optional[str] = None,
#         keywords  : List[str] = []
#     ) -> None:
#         self.text      = text
#         self.filter_by = filter_by
#         self.keywords  = keywords
#         self.top_k     = top_k


# class SearchAnswer:
#     '''Message: DataBase -> WEB-server'''

#     def __init__(
#         self,
#         content : List[str],
#         count   : int
#     ) -> None:
#         self.content = content
#         self.count   = count


# class IndexingRequestSP:
#     '''Message: WEB-server -> Processor'''
    
#     def __init__(
#         self,
#         content   : str,
#         queries   : List[str] = None,
#         keywords  : List[str] = [],
#         chunk_id  : Optional[str] = None
#     ) -> None:
#         self.content   = content
#         self.queries   = queries
#         self.keywords  = keywords
#         self.chunk_id  = chunk_id


# class IndexingRequestPDB:
#     '''Message: Processor -> DataBase'''

#     def __init__(
#         self,
#         content   : str,
#         vector    : List[float],
#         dataframe : Optional[str] = None,
#         keywords  : List[str] = []
#     ) -> None:
#         pass


class SearchRequest(BaseModel):
    '''Message: WEB-server -> DataBase'''

    text      : str
    top_k     : int = 3
    filter_by : str | None = None
    keywords  : List[str] = []

class IndexRequest(BaseModel):
    '''Message: WEB-server -> DataBase'''

    content   : str
    queries   : List[str]  = []
    keywords  : List[str]  = []
    chunk_id  : str | None = None


class ProcessedIndexingRequest(BaseModel):
    '''Message: Processor -> DataBase'''

    content   : str
    vector    : List[float]

class SearchAnswer(BaseModel):
    '''Message: DataBase -> WEB-server'''

    content   : List[str]
    count     : int