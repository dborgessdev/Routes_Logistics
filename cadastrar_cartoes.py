import requests
import json

link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

def cad_cartoes(uid):
    dados = {'uid': uid}
    requisicao = requests.post(f'{link}/cartoes.json', data=json.dumps(dados))
    if requisicao.status_code == 200:
        return True
    else:
        return False
