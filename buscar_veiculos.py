from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

#criando uma função para requisição de dados especificos separadamente veiculos

def get_veiculos():
    requisicao = requests.get(f'{link}/veiculos/.json')
    return requisicao, requisicao.text

requisicao_veiculos = requests.get(f'{link}/veiculos/.json')
print(requisicao_veiculos)
print(requisicao_veiculos.text)

#colocar o site no ar
if __name__ == "__main__":
    #OBS: utiliza-se app.run(debug=True) para ligrar o debug, porém o console retornará o comando executado 2x gerando 2x dados para o banco de dados 
    app.run()