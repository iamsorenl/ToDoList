from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}}, supports_credentials=True)

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return "Hello World!"

@app.route('/shark', methods=['GET'])
def shark():
    return "Shark"

TASKS = []

# The GET and POST route handler
@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
    response_object = {'status': 'success'}
    if request.method == "POST":
        post_data = request.get_json()
        TASKS.append({
            'id': uuid.uuid4().hex,
            'task': post_data.get('task'),
            'deadline': post_data.get('deadline'),
            'completed': post_data.get('completed')})
        response_object['message'] = 'Task Added'
    else:
        response_object['tasks'] = TASKS
    return jsonify(response_object)

# PUT and DELETE route handler
@app.route('/tasks/<task_id>', methods=['PUT', 'DELETE'])
def single_task(task_id):
    response_object = {'status': 'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        if remove_task(task_id):
            TASKS.append({
                'id': uuid.uuid4().hex,
                'task': post_data.get('task'),
                'deadline': post_data.get('deadline'),
                'completed': post_data.get('completed')})
            response_object['message'] = 'Task Updated'
        else:
            response_object['message'] = 'Task not found'
    elif request.method == "DELETE":
        if remove_task(task_id):
            response_object['message'] = 'Task Deleted'
        else:
            response_object['message'] = 'Task not found'
    return jsonify(response_object)

# removing the task to update
def remove_task(task_id):
    for task in TASKS:
        if task['id'] == task_id:
            TASKS.remove(task)
            return True
    return False

if __name__ == "__main__":
    app.run(debug=True)
