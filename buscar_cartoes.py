from flask import Flask
import requests
import json

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

def get_cartoes():
    requisicao = requests.get(f'{link}/cartoes/.json')
    if requisicao.status_code == 200:
        dados = requisicao.json()
        print(dados)  # Adicione este print para depuração
        return dados
    else:
        return {}

if __name__ == "__main__":
    app.run()