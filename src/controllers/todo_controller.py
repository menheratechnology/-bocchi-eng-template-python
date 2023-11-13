from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from todo import CreateTodoRequest
from repositories import todo_repository

router = APIRouter()


@router.get('/')
def find_all():
    todos = todo_repository.fetch_all()
    return JSONResponse(content={
        'status': 200,
        'message': 'Success got all todos',
        'data': {
            'todos': jsonable_encoder(todos)
        }
    })


@router.post('/')
def create(req: CreateTodoRequest):
    todos = todo_repository.create(req.name, req.is_done)
    return JSONResponse(content={
        'status': 200,
        'message': 'Success create todo',
        'data': jsonable_encoder(todos)
    })
