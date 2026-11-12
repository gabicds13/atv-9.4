from flask import Flask, jsonify, request

app = Flask(__name__)

# Exemplo didatico: dados guardados apenas na memoria.
tarefas = [{"id": 1, "descricao": "Estudar Flask"}]


@app.route("/", methods=["GET"])
def inicio():
    return jsonify({"mensagem": "API RESTful - Exercicio 9.4"})


@app.route("/tarefas", methods=["GET"])
def listar():
    return jsonify(tarefas), 200


@app.route("/tarefas", methods=["POST"])
def cadastrar():
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict) or not isinstance(dados.get("descricao"), str) or not dados["descricao"].strip():
        return jsonify({"erro": "Informe uma descricao valida"}), 400

    novo_id = max((t["id"] for t in tarefas), default=0) + 1
    nova = {"id": novo_id, "descricao": dados["descricao"].strip()}
    tarefas.append(nova)
    return jsonify(nova), 201


@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json(silent=True)
    if not isinstance(dados, dict) or not isinstance(dados.get("descricao"), str) or not dados["descricao"].strip():
        return jsonify({"erro": "Informe uma descricao valida"}), 400

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["descricao"] = dados["descricao"].strip()
            return jsonify(tarefa), 200
    return jsonify({"erro": "Tarefa nao encontrada"}), 404


@app.route("/tarefas/<int:id>", methods=["DELETE"])
def excluir(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefas.remove(tarefa)
            return jsonify({"mensagem": "Tarefa excluida"}), 200
    return jsonify({"erro": "Tarefa nao encontrada"}), 404


if __name__ == "__main__":
    app.run(debug=True)
