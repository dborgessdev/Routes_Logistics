from flask import Flask, render_template, request, redirect
import requests
import json
from buscar_veiculos import get_veiculos
from buscar_motoristas import get_motoristas
from buscar_viagens import get_viagens
from cadastrar_veiculos import cad_veiculos
from cadastrar_motoristas import cad_motoristas
from cadastrar_viagens import cad_viagens
from get_motorista_por_nome import get_motorista_por_nome
from atualizar_motorista import atualizar_motorista

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/veiculos")
def veiculos():
    requisicao_veiculos, dados_veiculos = get_veiculos()
    veiculos = json.loads(dados_veiculos)
    return render_template("veiculos.html", veiculos=veiculos)

@app.route("/veiculos_cadastro")
def veiculos_cadastro():
    return render_template("veiculos_cadastro.html")

@app.route("/cadastrar_veiculo", methods=["POST"])
def cadastrar_veiculo():
    if request.method == "POST":
        placa = request.form["placa"]
        marca = request.form["marca"]
        modelo = request.form["modelo"]
        ano_fabricacao = request.form["ano_fabricacao"]
        tipo_veiculo = request.form["tipo_veiculo"]
        capacidade_carga = request.form["capacidade_carga"]
        tag_rfid = request.form["tag_rfid"]
        cad_veiculos(placa, marca, modelo, ano_fabricacao, tipo_veiculo, capacidade_carga, tag_rfid)  # Chamada da função para cadastrar veículo
        return redirect("/veiculos")
    else:
        return "Erro: Método de requisição falhou ou não é POST!"

@app.route("/motoristas")
def motoristas():
    requisicao_motoristas, dados_motoristas = get_motoristas()
    motoristas = json.loads(dados_motoristas)  # Convertendo os dados para um dicionário
    return render_template("motoristas.html", motoristas=motoristas)

@app.route("/motoristas_cadastro")
def motoristas_cadastro():
    return render_template("motoristas_cadastro.html")

@app.route("/cadastrar_motorista", methods=["POST"])
def cadastrar_motorista():
    if request.method == "POST":
        nome = request.form["nome"]
        cpf = request.form["cpf"]
        cnh = request.form["cnh"]
        id_veiculo = request.form["id_veiculo"]
        validade_cnh = request.form["validade_cnh"]
        cad_motoristas(nome, cpf, cnh, id_veiculo, validade_cnh)
        return redirect("/motoristas")
    else:
        return "Erro: Método de requisição falhou ou não é POST!"
    
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

@app.route("/viagens")
def viagens():
    requisicao_viagem, dados_viagem = get_viagens()
    viagens = json.loads(dados_viagem)  # Convertendo os dados para um dicionário
    return render_template("viagens.html", viagens=viagens)

@app.route("/viagens_cadastro")
def viagens_cadastro():
    return render_template("viagens_cadastro.html")

@app.route("/cadastrar_viagem", methods=["POST"])
def cadastrar_viagem():
    if request.method == "POST":
        dados_inicio = request.form["dados_inicio"]
        dados_fim = request.form["dados_fim"]
        distancia_total = request.form["distancia_total"]
        status_viagem = request.form["status_viagem"]
        cad_viagens(dados_inicio, dados_fim, distancia_total, status_viagem)  # Chamada da função para cadastrar viagem
        return redirect("/viagens")
    else:
        return "Erro: Método de requisição falhou ou não é POST!"

if __name__ == "__main__":
    app.run(debug=True)
