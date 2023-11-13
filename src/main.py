from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/')
async def hello():
    return JSONResponse(content={
        'status': 200,
        'message': 'Success',
        'data': {
            'message': 'Hello, world!'
        }
    })


@app.get('/health')
async def getHealth():
    return JSONResponse(content={
        'status': 200,
        'message': 'Success',
        'data': {
            'health': 'status ok'
        }
    })
