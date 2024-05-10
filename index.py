from flask import Flask, render_template, request, redirect
import requests
import json

from cadastrar_motoristas import cad_motoristas
from buscar_motoristas import get_motoristas

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

#colocar o site no ar
if __name__ == "__main__":
    #OBS: utiliza-se app.run(debug=True) para ligrar o debug, porém o console retornará o comando executado 2x gerando 2x dados para o banco de dados 
    app.run(debug=True)