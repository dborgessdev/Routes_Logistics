from flask import Flask, jsonify
import requests
import json

class MotoristaDataManager:
    _instance = None

    def __new__(cls, link):
        if cls._instance is None:
            cls._instance = super(MotoristaDataManager, cls).__new__(cls)
            cls._instance._link = link
            cls._instance._data = None
        return cls._instance

    def get_data(self):
        if self._data is None:
            link_motorista = f'{self._link}/motoristas.json'
            requisicao = requests.get(link_motorista)
            self._data = requisicao.json()
        return self._data

def get_motorista_por_nome(nome, link):
    manager = MotoristaDataManager(link)
    dados_motoristas = manager.get_data()
    
    for key, value in dados_motoristas.items():
        if value['nome'] == nome:
            return key, json.dumps(value)
    
    return None, None
