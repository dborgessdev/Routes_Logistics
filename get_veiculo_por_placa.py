from flask import Flask
import requests
import json

def get_veiculo_por_placa(placa, link):
    link_veiculo = f'{link}/veiculos.json'
    requisicao = requests.get(link_veiculo)
    dados_veiculos = requisicao.json()

    for key, value in dados_veiculos.items():
        if value['placa'] == placa:
            return key, json.dumps(value)

    return None, None