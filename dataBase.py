# The interface for interaction with DataBase

from interface import ProcessedIndexingRequest, SearchRequest, SearchAnswer



def DBLoadVector(vector: ProcessedIndexingRequest) -> None:
    print('call DBLoadVector with:', vector.__dict__)


def DBSearchVector(vector: SearchRequest) -> SearchAnswer:
    print('call DBLoadVector with:', vector.__dict__)
    return SearchAnswer(
        content = ['text'],
        count = 1
    )
