# The interface for interaction with DataBase

from interface import ProcessedIndexingRequest, SearchRequest, SearchAnswer
from qdrant_client import models, QdrantClient

qdrant = QdrantClient(":memory:")

qdrant.create_collection(
    collection_name="my_books",
    vectors_config=models.VectorParams(
        size=7,
        distance=models.Distance.COSINE,
    ),
)




# qdrant.upload_points(
#     collection_name="my_books",
#     points=[
#         models.PointStruct(id=1, vector=[0, 0, 0, 0, 0, 0, 0], payload={'data': '1'*7}),
#         models.PointStruct(id=2, vector=[0, 7, 0, 7, 0, 7, 0], payload={'data': '2'*7}),
#         models.PointStruct(id=3, vector=[7, 0, 7, 0, 7, 0, 7], payload={'data': '3'*7}),
#     ],
# )


def DBLoadVector(vector: ProcessedIndexingRequest) -> None:
    print('call DBLoadVector with:', vector.__dict__)
    hits = qdrant.query_points(
        collection_name="my_books",
        query=[1, 1, 1, 0, 0, 0, 7],
        limit=2,
    ).points

    for hit in hits:
        print(hit.payload, "score:", hit.score)
    print('77777777777777777777')


def DBSearchVector(vector: SearchRequest) -> SearchAnswer:
    print('call DBLoadVector with:', vector.__dict__)
    return SearchAnswer(
        content = ['text'],
        count = 1
    )


def dbSearch(request: ProcessedSearchRequest) -> SearchAnswer:
    pass

def dbIndex(request: ProcessedIndexRequest) -> IndexAnswer:
    pass