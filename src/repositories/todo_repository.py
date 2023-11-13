from todo import Todo


todos = [
    Todo('todo1', False),
    Todo('todo2', True)
]


def fetch_all():
    return todos


def create(name: Todo.name, is_done: Todo.is_done):
    new_todo = Todo(
        name=name,
        is_done=is_done
    )
    todos.append(new_todo)

    return todos
