# Server is aimed to process user requests and send them to the DataBase

from interface import SearchRequest, ProcessedSearchRequest, SearchAnswer
from interface import IndexRequest, ProcessedIndexRequest, IndexAnswer
from dataBase import dbIndex, dbSearch
from processing import processIndex, processSearch
from fastapi import FastAPI
from simpleLogger import log, logact, logerr
import traceback



app = FastAPI()

@app.post('/searching')
async def search(request: SearchRequest) -> SearchAnswer:
    '''search in DataBase with given json'''

    try:
        logact('Search request:', request)
        request = processSearch(request)
        request = dbSearch(request)
        logact('Get answer from DB:', request)
        return request
    except Exception as e:
        logerr(traceback.format_exc())
        return SearchAnswer(
            success = False,
            content = [],
            count = 0
        )


@app.post('/indexing')
async def index(request: IndexRequest) -> IndexAnswer:
    '''Loads given json to DataBase'''

    try:
        logact('Index request:', request)
        request = processIndex(request)
        dbIndex(request)
        return IndexAnswer(
            success = True
        )
    except Exception as e:
        logerr(traceback.format_exc())
        return IndexAnswer(
            success = False
        )
