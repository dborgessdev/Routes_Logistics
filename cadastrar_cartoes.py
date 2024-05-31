import requests
import json

class CartaoBuilder:
    def __init__(self):
        self.dados = {}

    def uid(self, uid):
        self.dados['uid'] = uid
        return self

    def status(self, status):
        self.dados['status'] = status
        return self

    def build(self):
        return self.dados

def cad_cartao(uid, status, link):
    dados = {'uid': uid, 'status': status}
    requisicao = requests.post(f'{link}/cartoes/.json', data=json.dumps(dados))

    if requisicao.status_code == 200:
        return True
    else:
        return False