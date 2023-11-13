from pydantic import BaseModel


class Todo:
    name = ''
    is_done = False

    def __init__(self, name, is_done):
        self.name = name
        self.is_done = is_done

    def done(self):
        self.is_done = True

    def undone(self):
        self.is_done = False


class CreateTodoRequest(BaseModel):
    name: str
    is_done: bool
