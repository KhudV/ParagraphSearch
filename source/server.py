# Server is aimed to process user requests and send them to the DataBase

from interface import SearchAnswer, IndexRequest, SearchRequest
from dataBase import dbIndex, dbSearch
from exceptions import BadRequest, InternalError
from processing import processIndex, processSearch
from fastapi import FastAPI, Body
import traceback


app = FastAPI()

@app.post('/search')
async def search(request: SearchRequest) -> SearchAnswer:
    '''search in DataBase with given json'''

    try:
        # print(request.__dict__)
        request = processSearch(request)
        request = dbSearch(request)
        return request
    # except BadRequest | InternalError as e:
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return SearchAnswer(
            success = False,
            content = [],
            count = 0
        )


@app.post('/index')
async def index(request: IndexRequest):
    '''Loads given json to DataBase'''

    try:
        print(request.__dict__)
        # request = indexingRequestToClass(request)
        request = processIndex(request)
        print(len(request.vector))
        dbIndex(request)
        return {'status': 'ok'}
    except Exception as e:
        print(e)
        print(traceback.format_exc())
        return {'status': 'error'}
