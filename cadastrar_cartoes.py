import requests
import json

def cad_cartao(uid, link):
    dados = {'uid': uid}
    requisicao = requests.post(f'{link}/cartoes/.json', data=json.dumps(dados))

    if requisicao.status_code == 200:
        return True
    else:
        return False
