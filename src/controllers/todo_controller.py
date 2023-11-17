from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from todo import CreateTodoRequest
# ↓このモジュールを呼び出してください
from repositories import todo_repository

router = APIRouter()


@router.get('/')
def find_all():
    # TODO: ここでtodo_repositoryのfetch_allを呼び出す
    # TODO: todo_repositoryのfetch_allメソッドから受け取ったtodosを代入する
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
    # TODO: ここでtodo_repositoryのcreateを呼び出す
    todos = [] # TODO: todo_repositoryのcreateメソッドから受け取った新しいtodosを代入する
    return JSONResponse(content={
        'status': 200,
        'message': 'Success create todo',
        'data': jsonable_encoder(todos)
    })
