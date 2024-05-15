from flask import Flask
# get_motorista_por_nome.py
import requests
import json

def get_motorista_por_nome(nome, link):
    link_motorista = f"{link}/motoristas.json"
    requisicao = requests.get(link_motorista)
    dados_motoristas = requisicao.json()
    
    for key, value in dados_motoristas.items():
        if value['nome'] == nome:
            return key, json.dumps(value)
    
    return None, None
