from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

""" def cad_motorista, através dessa function utilizamos as bibliotecas JSON e REQUESTS
para o preenchimento de dados (através da variavel dados) no banco de dados do firebase da tabela de motoristas"""

def cad_motorista(nome, cpf,cnh , id_veiculo,validade_cnh):
    dados = { 'nome': nome, 'cpf':cpf, 'cnh':cnh, 'id_veiculo': id_veiculo, 'validade_cnh':	validade_cnh}
    requisicao = requests.post(f'{link}/motoristas/.json', data=json.dumps(dados))
    #criar um motorista
    """print(requisicao)
    print(requisicao.text) 
    pode ser usado como forma de debug; 
    """
cad_motorista("Luiz", "00090040013", "02523654" , "kajsdh5465aksj16","15/11/26")


""" def cad_veiculo, através dessa function utilizamos as bibliotecas JSON e REQUESTS
para o preenchimento de dados (através da variavel dados) no banco de dados do firebase da tabela de motoristas"""

def cad_veiculo(placa, marca, modelo, ano_fabricacao, tipo_veiculo, capacidade_clarga, tag_rfid):
    dados = { 'placa': placa, 'marca': marca, 'modelo': modelo, 'ano_fabricacao': ano_fabricacao, 'tipo_veiculo':	tipo_veiculo, 'capacidade_clarga': capacidade_clarga, 'tag_rfid': tag_rfid}
    requisicao = requests.post(f'{link}/veiculos/.json', data=json.dumps(dados))
    #criar um veiculo
    """print(requisicao)
    print(requisicao.text) 
    pode ser usado como forma de debug; 
    """
cad_veiculo("Luiz", "00090040013", "02523654" , "kajsdh5465aksj16","15/11/26", "asdasd" , "asdsadas" )

""" cad viagens """
def cad_viagem(dados_inicio, dados_fim, distancia_total, status_viagem):
    dados = {'dados_inicio': dados_inicio, 'dados_fim': dados_fim, 'distancia_total': distancia_total, 'status_viagem': status_viagem}
    requisicao = requests.post(f'{link}/viagens/.json', data=json.dumps(dados))

cad_viagem("02/05, 15:25, São Paulo", "03/05, 15:25, Feira de Santana", "200Km", "concluida")

#Editar

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

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)