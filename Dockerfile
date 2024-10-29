FROM python:3.11

WORKDIR /usr/src/app

COPY server.py .
COPY processing.py .
COPY interface.py .
COPY dataBase.py .
COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install qdrant-client

# EXPOSE 8000

# CMD ["fastapi", "dev", "./server.py"]
CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0"]


