from fastapi import FastAPI
 
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello METANIT.COM"}
 
@app.get("/about")
def about():
    return {"message": "О сайте"}

@app.post('/index')
def index():
    return {'message': 'No index! Ha ha!'}

@app.post('/search')
def search():
    return {'message': 'No search! Ha ha!'}

