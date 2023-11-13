from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from todo import Todo, CreateTodoRequest

router = APIRouter()

todos = [
    Todo('todo1', False),
    Todo('todo2', True)
]


@router.get('/')
def find_all():
    return JSONResponse(content={
        'status': 200,
        'message': 'Success got all todos',
        'data': {
            'todos': jsonable_encoder(todos)
        }
    })


@router.post('/')
def create(req: CreateTodoRequest):
    new_todo = Todo(
        name=req.name,
        is_done=req.is_done
    )
    todos.append(new_todo)

    return JSONResponse(content={
        'status': 200,
        'message': 'Success create todo',
        'data': jsonable_encoder(todos)
    })
