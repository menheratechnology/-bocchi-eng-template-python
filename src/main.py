from fastapi import FastAPI
from fastapi.responses import JSONResponse
from controllers import todo_controller

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
        'data': 'status ok'
    })


app.include_router(
    todo_controller.router,
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}},
)
