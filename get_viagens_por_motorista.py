from flask import Flask
import requests
import json

def get_viagens_por_motorista(motorista, link):
    link_viagem = f'{link}/viagens.json'
    requisicao = requests.get(link_viagem)
    dados_viagem = requisicao.json()

    for key, value in dados_viagem.items():
        if value['motorista'] == motorista:
            return key, json.dumps(value)
    
    return None, None