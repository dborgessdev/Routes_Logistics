from flask import Flask, render_template, request, redirect
import requests
import json
from buscar_veiculos import get_veiculos
from buscar_motoristas import get_motoristas
from buscar_viagens import get_viagens
from cadastrar_veiculos import cad_veiculos
from cadastrar_motoristas import cad_motoristas
from cadastrar_viagens import cad_viagens

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

# 1) criar primeira pagina

"""
1.2)
Toda página no Flask sempre tem um "route" e uma função
route = link / caminho da página depois do domínio https ex: meuprojetoflask.com ou podemos criar a rota para a pagina de login meuprojetoflask.com/login
função = é o que queremos exibir em uma página

"""
#1.3) criando a rota / route através do decorator - atribui uma nova funcionalidade para a função logo abaixo dela
@app.route("/")
#1.4) criando a função:
def homepage():
    #1.5 solicitamos como retorno utilizando a função render template, o acesso a pagina através do arquivo html na pasta templates
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

#2 - Criando rotas dinâmicas
#aqui vemos que o route (decorator) passa a receber como complemento da url o parametro <nome_usuario> isso quer dizer que no momento em que quando preenchemos a url meusiteemflask/usuarios/davi o Flask irá criar automaticamente uma pogina para o usuário informado 
@app.route("/usuarios/<nome_usuario>")
#2.1 Criando a função:
#aqui vemos que o nome da rota (usuarios) continua a se repetir porém a função receberá como parametro a variável nome_usuario
def usuarios(nome_usuario):
    #2.2 Em nosso retorno, dentro da função importada render template informamos normalmente o nome do arquivo designado para essa pagina, criado na pasta templates e informamos que o arquivo irá chamar a função nome_usuario, que recebe como parametro o nome do usuário, assim, de maneira dinâmica, ao digitar: http://127.0.0.1:5000/usuarios/davi será gerado automaticamente através do html, uma página do usuario "davi"
    return render_template("usuarios.html", nome_usuario=nome_usuario)

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

#colocar o site no ar
if __name__ == "__main__":
    #OBS: utiliza-se app.run(debug=True) para ligrar o debug, porém o console retornará o comando executado 2x gerando 2x dados para o banco de dados 
    app.run(debug=True)
