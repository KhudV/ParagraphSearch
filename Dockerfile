FROM python:3.11

WORKDIR /usr/src/app

COPY models /usr/src/app/models

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY scripts /usr/src/app/scripts
COPY source /usr/src/app/source

EXPOSE 8000
# EXPOSE 6333

# CMD ["fastapi", "dev", "./server.py"]
# CMD ["cd", "source", "&&", "uvicorn", "server:app", "--reload", "--host", "0.0.0.0"]
CMD ["python", "source/startup.py"]
