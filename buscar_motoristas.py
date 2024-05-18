from flask import Flask
import requests
import json


app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

#criando uma função para requisição de dados especificos separadamente motoristas

def get_motoristas():
    requisicao = requests.get(f'{link}/motoristas/.json')
    return requisicao, requisicao.text

requisicao_motoristas = requests.get(f'{link}/motoristas/.json')
print(requisicao_motoristas)
print(requisicao_motoristas.text)

#colocar o site no ar
if __name__ == "__main__":
    #OBS: utiliza-se app.run(debug=True) para ligrar o debug, porém o console retornará o comando executado 2x gerando 2x dados para o banco de dados 
    app.run()