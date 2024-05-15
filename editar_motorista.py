from flask import Flask, render_template, request, redirect
from get_motorista_por_nome import get_motorista_por_nome
from atualizar_motorista import atualizar_motorista
import json

app = Flask(__name__)

link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

@app.route("/editar_motorista/<string:nome>", methods=["GET", "POST"])
def editar_motorista(nome):
    if request.method == "GET":
        # Chama a função para obter os detalhes do motorista pelo nome
        motorista_id, dados_motorista = get_motorista_por_nome(nome, link)
        if dados_motorista is not None:
            motorista = json.loads(dados_motorista)
            return render_template("editar_motorista.html", motorista=motorista)
        else:
            # Se o motorista não for encontrado, redireciona para alguma página de erro
            return render_template("pagina_de_erro.html")
    elif request.method == "POST":
        # Processa os dados enviados do formulário de edição e atualiza o motorista
        cpf = request.form["cpf"]
        cnh = request.form["cnh"]
        id_veiculo = request.form["id_veiculo"]
        validade_cnh = request.form["validade_cnh"]
        # Chama a função para atualizar o motorista
        if atualizar_motorista(nome, cpf, cnh, id_veiculo, validade_cnh, link):
            return redirect("/motoristas")
        else:
            # Se a atualização falhar, redireciona para alguma página de erro
            return render_template("pagina_de_erro.html")

if __name__ == "__main__":
    app.run(debug=True)