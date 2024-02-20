from fastapi import FastAPI

app = FastAPI(docs_url='/api/docs/')


@app.get('/')
def get_hello():
    return 'Hello!'
