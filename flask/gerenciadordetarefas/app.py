from flask import Flask, request, jsonify
from models.task import Task

#__name__ = "__main__"
app = Flask(__name__)

#CRUD
#CREATE, READ, UPDATE, DELETE

tasks_list = []
tasks_id_control = 1

@app.route("/tasks", methods=['POST'])
def create_task():
    global tasks_id_control

    data = request.get_json()

    #print(data)
    #print(type(data))

    new_task = Task(id=tasks_id_control, title=data["title"], description=data.get("description", ""))
    
    #print(new_task)

    print(new_task.to_dict())
    tasks_list.append(new_task)

    tasks_id_control += 1

    return jsonify({"message": "Nova tarefa criada com sucesso", "id": new_task.id})

@app.route("/tasks", methods=['GET'])
def get_tasks():
    
    list_return = [i.to_dict() for i in tasks_list]

    total_tasks = len(tasks_list)

    retorno = {
        "tasks": list_return,
        "total_tasks": total_tasks
    }

    return jsonify(retorno) #{"message": "Lista de tarefas obtida com sucesso"})

@app.route("/tasks/<int:id>", methods=['GET'])
def get_task_by_id(id):

    desejado = None

    for t in tasks_list:
        if t.id == id:
            desejado = t.to_dict()
            break
        elif t.id > id:
            break
    
    if desejado == None:
        return jsonify({"message": "not found"}), 404
    else:
        return jsonify(desejado), 200

@app.route("/tasks/<int:id>", methods=['PUT'])
def atualizar_task(id):

    data = request.get_json()

    desejado = False

    for t in tasks_list:
        if t.id == id:
            t.title = data["title"]
            t.description = data["description"]
            t.completed = data["completed"]
            desejado = t.to_dict()
            break
        elif t.id > id:
            break
    
    if desejado == False:
        return jsonify({"message": "not found"}), 404
    else:
        return jsonify(desejado), 200

@app.route("/tasks/<int:id>", methods=['DELETE'])
def delete_task(id):

    desejado = None

    for i, t in enumerate(tasks_list):
        if t.id == id:
            deleted_task = tasks_list.pop(i)
            desejado = True
            break
        elif t.id > id:
            break
    
    if desejado == None:
        return jsonify({"message": "not found"}), 404
    else:
        return jsonify({"message": "Tarefa deletada com sucesso"}), 200

if __name__ == "__main__":
    app.run(debug=True)