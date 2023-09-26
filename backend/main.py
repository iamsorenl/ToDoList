from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(__name__)

CORS(app, resources={r"/*":{'origins':"*"}})

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return("Hello World!")

@app.route('/shark', methods=['GET'])
def shark():
    return("Shark")

TASKS = [
    {
        'task':'wash dishes',
        'deadline':'tonight',
        'completed':False,
    },
    {
        'task':'clean room',
        'deadline':'tomorrow',
        'completed':False,
    },
    {
        'task':'pay rent',
        'deadline':'friday',
        'completed':True,
    },
    {
        'task':'take out trash',
        'deadline':'tuesday',
        'completed':True,
    }
]

# The GET route handler
@app.route('/tasks', methods=['GET', 'POST'])
def all_tasks():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        TASKS.append({
            'task': post_data.get('task'),
            'deadline': post_data.get('deadline'),
            'completed': post_data.get('completed')})
        response_object['message'] = 'Task Added'
    else:
        response_object['tasks'] = TASKS
    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True)
