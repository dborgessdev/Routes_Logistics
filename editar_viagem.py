# editar_viagem.py

from flask import Flask, render_template, request, redirect
from get_viagens_por_motorista import get_viagens_por_motorista
from atualizar_viagem import atualizar_viagem
import json

app = Flask(__name__)

link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

@app.route("/editar_viagem/<string:motorista>", methods=["GET", "POST"])
def editar_viagem(motorista):
    if request.method == "GET":
        # Chama a função para obter os detalhes da viagem pelo motorista
        viagem_id, dados_viagem = get_viagens_por_motorista(motorista, link)
        if dados_viagem is not None:
            viagem = json.loads(dados_viagem)
            return render_template("editar_viagem.html", viagem=viagem)
        else:
            # Se a viagem não for encontrada, redireciona para alguma página ou retorna uma mensagem
            return "Viagem não encontrada.", 404
    elif request.method == "POST":
        # Processa os dados enviados do formulário de edição e atualiza a viagem
        origem = request.form["origem"]
        destino = request.form["destino"]
        data_inicio = request.form["data_inicio"]
        data_fim = request.form["data_fim"]
        distancia_total = request.form["distancia_total"]
        status_viagem = request.form["status_viagem"]
        # Chama a função para atualizar a viagem
        if atualizar_viagem(origem, destino, data_inicio, data_fim, distancia_total, status_viagem, motorista, link):
            return redirect("/viagens")
        else:
            # Se a atualização falhar, redireciona para alguma página ou retorna uma mensagem
            return "Falha ao atualizar a viagem.", 500

if __name__ == "__main__":
    app.run(debug=True)
