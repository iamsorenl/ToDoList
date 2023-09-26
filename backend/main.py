from flask import Flask, jsonify
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
@app.route('/tasks', methods=['GET'])
def all_tasks():
    return jsonify({
        'tasks': TASKS,
        'status': 'success',
    })

if __name__ == "__main__":
    app.run(debug=True)
