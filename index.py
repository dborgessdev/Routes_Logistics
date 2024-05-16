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
from get_viagens_por_motorista import get_viagens_por_motorista
from atualizar_viagem import atualizar_viagem
from get_veiculo_por_placa import get_veiculo_por_placa
from atualizar_veiculo import atualizar_veiculo

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
    
@app.route("/editar_veiculo/<string:placa>", methods=["GET", "POST"])
def editar_veiculo(placa):
    if request.method == "GET":
        # Chama a função para obter os detalhes do veículo pelo placa
        veiculo_id, dados_veiculo = get_veiculo_por_placa(placa, link)
        if dados_veiculo is not None:
            veiculo = json.loads(dados_veiculo)
            return render_template("editar_veiculo.html", veiculo=veiculo)
        else:
            # Se o veículo não for encontrado, redireciona para alguma página ou retorna uma mensagem
            return "Veículo não encontrado.", 404
    elif request.method == "POST":
        # Processa os dados enviados do formulário de edição e atualiza o veículo
        placa = request.form["placa"]
        marca = request.form["marca"]
        modelo = request.form["modelo"]
        ano_fabricacao = request.form["ano_fabricacao"]
        tipo_veiculo = request.form["tipo_veiculo"]
        capacidade_carga = request.form["capacidade_carga"]
        tag_rfid = request.form["tag_rfid"]
        # Chama a função para atualizar o veículo
        if atualizar_veiculo(placa, marca, modelo, ano_fabricacao, tipo_veiculo, capacidade_carga, tag_rfid, link):
            return redirect("/veiculos")


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
            return render_template("editar_motorista.html",motorista=motorista)
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
        origem = request.form["origem"]
        destino = request.form["destino"]
        data_inicio = request.form["data_inicio"]
        data_fim = request.form["data_fim"]
        distancia_total = request.form["distancia_total"]
        status_viagem = request.form["status_viagem"]
        motorista = request.form["motorista"]
        cad_viagens(origem, destino, data_inicio, data_fim, distancia_total, status_viagem, motorista)  # Chamada da função para cadastrar viagem
        return redirect("/viagens")
    else:
        return "Erro: Método de requisição falhou ou não é POST!"
    
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
        
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)