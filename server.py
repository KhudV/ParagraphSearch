# Server is aimed to process user requests and send them to the DataBase

from interface import SearchAnswer, IndexRequest, SearchRequest
from dataBase import DBLoadVector, DBSearchVector
from processing import process

from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
from typing import Union
import json
import sys



class BadRequest(BaseException):
    def __init__(self):
        super().__init__('BadRequest')

class InternalError(BaseException):
    def __init__(self):
        super().__init__('InternalError')

# def searchRequestToClass(request: dict) -> SearchRequest:
#     '''Convers from json to searchRequest'''

#     try:
#         request.setdefault('filter_by', '')
#         request.setdefault('keywords', [])

#         return SearchRequest(
#             text      = request['text'],
#             top_k     = request['top_k'],
#             filter_by = request['filter_by'],
#             keywords  = request['keywords']
#         )
#     except:
#         raise BadRequest()


# def indexingRequestToClass(request: dict) -> IndexingRequestSP:
#     '''Convers indexingRequest from json to python class'''

#     try:
#         return IndexingRequestSP(
#             content   = request['content'],
#             queries   = request['queries'],
#             keywords  = request['keywords_or_phrases'],
#             chunk_id  = request['chunk_id'],
#         )
#     except:
#         raise BadRequest()

#//? ######################################################################

app = FastAPI()

@app.post('/search')
async def search(request: SearchRequest) -> SearchAnswer:
    '''search in DataBase with given json'''

    try:
        print(request.__dict__)
        return DBSearchVector(request)
    except BadRequest | InternalError as e:
        return {'error': e}


@app.post('/index')
async def index(request: IndexRequest):
    '''Loads given json'''

    try:
        print(request.__dict__)
        # request = indexingRequestToClass(request)
        request = process(request)
        DBLoadVector(request)
        return {'status': 'ok'}
    except BadRequest | InternalError as e:
        return {'error': e}



# @app.post('/load_train')
# def loadTrain(path: str):
#     '''Loads all json from file to Data Base'''

#     with open(path, 'r') as file:
#         data = json.load(file)
#         for q in data:
#             index(q)
