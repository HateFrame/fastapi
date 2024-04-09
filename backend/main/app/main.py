from fastapi import FastAPI

app = FastAPI(docs_url='/api/docs/')


@app.get(path='/', description='Hello message')
def get_hello():
    return 'Hello!'
