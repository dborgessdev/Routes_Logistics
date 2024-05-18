from flask import Flask
import requests
import json

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

def get_cartoes():
    requisicao = requests.get(f'{link}/cartoes/.json')
    return requisicao, requisicao.text

requisicao_cartoes = requests.get(f'{link}/cartoes/.json')

print(requisicao_cartoes)
print(requisicao_cartoes.text)

if __name__ == "__main__":
    app.run()

