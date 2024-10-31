# The interface for interaction with DataBase

from qdrant_client import models, QdrantClient
from interface import ProcessedSearchRequest, SearchAnswer
from interface import ProcessedIndexRequest, IndexAnswer
from counter import counter

qdrant = QdrantClient(":memory:")
# qdrant = QdrantClient(url='http://localhost:6333')

try:
    qdrant.create_collection(
        collection_name="DataBase",
        vectors_config=models.VectorParams(
            size=768,
            distance=models.Distance.COSINE,
        ),
    )
except:
    print('Found existed collection')


def dbSearch(request: ProcessedSearchRequest) -> SearchAnswer:
    hits = qdrant.query_points(
        collection_name="DataBase",
        query=request.vector,
        limit=request.top_k,
    ).points

    ret = SearchAnswer(
        success = True,
        content = [],
        count   = 0
    )

    print('printing hints')
    for hit in hits:
        print(hit.payload, "score:", hit.score)
        ret.content.append(hit)
        ret.count += 1

    return ret


def dbIndex(request: ProcessedIndexRequest) -> IndexAnswer:
    
    qdrant.upload_points(
        collection_name="DataBase",
        points=[
            # models.PointStruct(id=1, vector=[0, 0, 0, 0, 0, 0, 0], payload={'data': '1'*7}),
            models.PointStruct(
                id      = counter(),
                vector  = request.vector,
                payload = {'content': request.content}
            ),
        ],
    )

    return IndexAnswer(success=True)
