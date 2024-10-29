# Server is aimed to process user requests and send them to the DataBase

from interface import SearchAnswer, IndexRequest, SearchRequest
# from dataBase import DBLoadVector, DBSearchVector
from exceptions import BadRequest, InternalError
from processing import processIndex, processSearch
from fastapi import FastAPI, Body



app = FastAPI()

@app.post('/search')
async def search(request: SearchRequest) -> SearchAnswer:
    '''search in DataBase with given json'''

    try:
        print(request.__dict__)
        # return DBSearchVector(request)

    except BadRequest | InternalError as e:
        return {'error': e}


@app.post('/index')
async def index(request: IndexRequest):
    '''Loads given json to DataBase'''

    try:
        print(request.__dict__)
        # request = indexingRequestToClass(request)
        request = processIndex(request)
        print(len(request.vector))
        # DBLoadVector(request)
        return {'status': 'ok'}
    except BadRequest | InternalError as e:
        return {'error': e}
