from flask import Flask
import requests
import json


app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

def get_motoristas():
    requisicao = requests.get(f'{link}/motoristas/.json')
    if requisicao.status_code == 200:
        dados = requisicao.json()
        if dados:
            return True, dados
        else:
            return False, ""  # Retorna uma string vazia quando não há motoristas cadastrados
    else:
        return False, ""
