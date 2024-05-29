from flask import Flask, request, redirect
import requests
import json

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

class VeiculoBuilder:
    def __init__(self):
        self.dados = {}

    def placa(self, placa):
        self.dados['placa'] = placa
        return self

    def marca(self, marca):
        self.dados['marca'] = marca
        return self

    def modelo(self, modelo):
        self.dados['modelo'] = modelo
        return self

    def ano_fabricacao(self, ano_fabricacao):
        self.dados['ano_fabricacao'] = ano_fabricacao
        return self

    def tipo_veiculo(self, tipo_veiculo):
        self.dados['tipo_veiculo'] = tipo_veiculo
        return self

    def capacidade_carga(self, capacidade_carga):
        self.dados['capacidade_carga'] = capacidade_carga
        return self

    def tag_rfid(self, tag_rfid):
        self.dados['tag_rfid'] = tag_rfid
        return self

    def build(self):
        return self.dados

def cad_veiculos(builder):
    dados = builder.build()
    requisicao = requests.post(f'{link}/veiculos/.json', data=json.dumps(dados))
    if requisicao.status_code == 200:
        return True
    else:
        return False



if __name__ == "__main__":
    app.run(debug=True)
