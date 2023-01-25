from flask import Flask, jsonify, request,json
todos = [{ "label": "My first task", "done": False }]
app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    nuevo_todo = request.get_json()
    todos.append(nuevo_todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
        del todos[position]
        return jsonify(todos)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)