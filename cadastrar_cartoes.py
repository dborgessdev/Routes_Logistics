# cadastrar_cartoes.py
from flask import Flask
import requests
import json

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

def cad_cartoes(uid, placa_veiculo):
    dados = {'uid': uid, 'placa_veiculo': placa_veiculo}
    requisicao = requests.post(f'{link}/cartoes/.json', data=json.dumps(dados))
    if requisicao.status_code == 200:
        return True
    else:
        return False

if __name__ == '__main__':
    app.run()
