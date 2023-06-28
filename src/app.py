from flask import Flask, jsonify, request
app = Flask(__name__)


todos = [ { "label": "My first task", "done": False } ]

@app.route('/todos', methods=['GET'])
def hello_world():
    todo_list = jsonify(todos)
    return todo_list

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    todos.append(request_body)
    
    todo_list = jsonify(todos)
    return todo_list

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]

    todo_list = jsonify(todos)
    return todo_list  
git remote add origin https://github.com/danilopgon/todo-list-api.git
git branch -M main
git push -u origin main

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)