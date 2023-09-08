from fastapi import FastAPI

app = FastAPI()
todos = [{'title': 'class_start', 'desc': '9.05'},
{'title': 'class_end', 'desc': '9.55'},
{'title': 'class_duration', 'desc': '100min'}]

@app.get('/')
def greet():
    return "PSIT 4A 4B, iys FastAPI time "

@app.get('/api/v1/todos')
def getAllTodos():
    return todos

@app.get('/api/v1/todos/{title}')
def getTodo(title: str):
    result_todo = {}
    for todo in todos:
        if todo['title'] == title:
            result_todo = todo
    return result_todo

@app.post('/api/v1/todos')
def createTodo(todo: dict):
    todos.append(todo)
    return {
        'data': todo,
        'message': 'todo has been added'
    }

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


@app.put('/api/v1/todos/{title}/{desc}')
def updateTodo(title: str, desc: str):
    for todo in todos:
        if todo['title'] == title:
            todo['desc'] = desc
            return {'message': 'todo updated', 'data': todo}
    return {'message': 'could not update todo'}
