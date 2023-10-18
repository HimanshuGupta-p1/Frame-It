from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


todos = [{'title': 'class_start', 'desc': '9.05'},
{'title': 'class_end', 'desc': '9.55'},
{'title': 'class_duration', 'desc': '100min'}]

@app.get('/')
def greet():
    return "PSIT 4A 4B, iys FastAPI time "

# List of all the todos
@app.get('/api/v1/todos')
def getAllTodos():
    return todos
# Get a specific todo
@app.get('/api/v1/todos/{title}')
def getTodo(title: str):
    result_todo = {}
    for todo in todos:
        if todo['title'] == title:
            result_todo = todo
    return result_todo

# Add a new todo to the list
@app.post('/api/v1/todos')
def createTodo(todo: dict):
    todos.append(todo)
    return {
        'data': todo,
        'message': 'todo has been added'
    }

# Delete a specific todo
@app.delete('/api/v1/todos/delete/{title}')
def deleteTodo(title: str):
    result_todo = {}
    for idx, todo in enumerate(todos):
        if todo['title'] == title:
            todos.pop(idx)
            return {
                'data': todo,
                'message': 'todo has been deleted'
            }
        
    return {
        'data': None,
        'message': 'todo could not be found'
    }

# Update any todo 
@app.put('/api/v1/todos/{title}/{desc}')
def updateTodo(title: str, desc: str):
    for todo in todos:
        if todo['title'] == title:
            todo['desc'] = desc
            return {'message': 'todo updated', 'data': todo}
    return {'message': 'could not update todo'}



