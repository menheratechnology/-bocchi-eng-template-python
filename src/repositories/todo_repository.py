from todo import Todo


todos = [
    Todo('todo1', False),
    Todo('todo2', True)
]


def fetch_all():
    # TODO: ここでtodosを返す
    return todos


def create(name: Todo.name, is_done: Todo.is_done):
    # TODO: ここでtodos配列に新しいTodoアイテムを追加し、todosを返す
    new_todo = Todo(
        name=name,
        is_done=is_done
    )
    todos.append(new_todo)
    return todos
