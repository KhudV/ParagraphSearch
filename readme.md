# Pargraph Search

Service for searching paragraphs.


## Dependences

This solution uses:
+ qdrant
+ docker
+ multilingual-e5
+ FastAPI


## Solution scheme
![Изображение](doc/scheme.png "Scheme")


## API
Server run on *'localhost:5000'*.

*POST /searching*

```json
JSON{
    "text"      : str,
    "top_k"     : int,
    "filter_by" : str | null,
    "keywords"  : List[str]
}
```

*POST /indexing*
```json
JSON{
    "content"              : str,
    "queries"              : List[str] | null,
    "keywords_or_phrases"  : List[Dict[str, str | None]],
    "chunk_id"             : str | null
}
```


## Installation

Pull docker image <https://hub.docker.com/r/largenumberofones/paragraph_search>
```bash
docker pull largenumberofones/paragraph_search
```
and then run docker compose with this docker-compose.yaml.
```yaml
services:
	server:
		image: largenumberofones/paragraph_search
		ports:
			- '5000:8000'
	qdrant:
		image: qdrant/qdrant
		ports:
			- '6333:6333'
```


## Run

```bash
docker compose up
```