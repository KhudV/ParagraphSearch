import uvicorn



if __name__ == "__main__":
    print('starting')
    uvicorn.run('server:app', host="0.0.0.0", port=8000, reload=True)
    print('ending')
