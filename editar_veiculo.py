from flask import Flask, render_template, request, redirect
from get_veiculo_por_placa import get_veiculo_por_placa
from atualizar_veiculo import atualizar_veiculo
import json

app = Flask(__name__)

link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

@app.route("editar_veiculo/<string:placa>", methods=["GET", "POST"])
def editar_veiculo(placa):
    if request.method == "GET":
        # Chama a função para obter os detalhes do veículo pelo nome
        veiculo_id, dados_veiculo = get_veiculo_por_placa(placa, link)
        if dados_veiculo is not None:
            veiculo = json.loads(dados_veiculo)
            return render_template("editar_veiculo.html", veiculo=veiculo)
        else:
            # Se o veículo não for encontrado, redireciona para alguma página de erro
            return render_template("pagina_de_erro.html")
    elif request.method == "POST":
        # Processa os dados enviados do formulário de edição e atualiza o veículo
        marca = request.form["marca_marca"]
        modelo = request.form["modelo"]
        ano_fabricacao = request.form["ano_fabricacao"]
        tipo_veiculo = request.form["tipo_veiculo"]
        capacidade_carga = request.form["capacidade_carga"]
        tag_rfid = request.form["tag_rfid"]
        if atualizar_veiculo(placa, marca, modelo, ano_fabricacao, tipo_veiculo, capacidade_carga, tag_rfid, link):
            return redirect("/veiculos")
        else:
            return render_template("pagina_de_erro.html")
        
if __name__ == "__main__":
    app.run()