import requests
import json


class MotoristaBuilder:

    def __init__(self):
        self.dados = {}

    def nome(self, nome):
        self.dados['nome'] = nome
        return self
    
    def cpf(self, cpf):
        self.dados['cpf'] = cpf
        return self
    
    def cnh(self, cnh):
        self.dados['cnh'] = cnh
        return self
    
    def id_veiculo(self, id_veiculo):
        self.dados['id_veiculo'] = id_veiculo
        return self

    def validade_cnh(self, validade_cnh):
        self.dados['validade_cnh'] = validade_cnh
        return self

    def build(self):
        return self.dados

def cad_motoristas(nome, cpf, cnh, id_veiculo, validade_cnh, link):
    dados = { 'nome': nome, 'cpf':cpf, 'cnh':cnh, 'id_veiculo': id_veiculo, 'validade_cnh':	validade_cnh}
    requisicao = requests.post(f'{link}/motoristas/.json', data=json.dumps(dados))

    if requisicao.status_code == 200:
        return True
    else:
        return False
