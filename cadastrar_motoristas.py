from flask import Flask
import requests
import json


app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"


def cad_motoristas(nome, cpf, cnh, id_veiculo, validade_cnh):
    dados = { 'nome': nome, 'cpf':cpf, 'cnh':cnh, 'id_veiculo': id_veiculo, 'validade_cnh':	validade_cnh}
    requisicao = requests.post(f'{link}/motoristas/.json', data=json.dumps(dados))

    ("Putin", "00090040013", "02523654" , "kajsdh5465aksj16","15/11/26")


if __name__ == "__main__":
    app.run()