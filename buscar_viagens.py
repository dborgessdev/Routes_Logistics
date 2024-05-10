from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"


#criando uma função para requisição de dados especificos separadamente viagens

def get_viagens():
    requisicao = requests.get(f'{link}/viagens/.json')
    return requisicao, requisicao.text

requisicao_viagem = requests.get(f'{link}/viagens/.json')
print(requisicao_viagem)
print(requisicao_viagem.text)

#colocar o site no ar
if __name__ == "__main__":
    #OBS: utiliza-se app.run(debug=True) para ligrar o debug, porém o console retornará o comando executado 2x gerando 2x dados para o banco de dados 
    app.run()