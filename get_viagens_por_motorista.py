from flask import Flask, jsonify
import requests
import json

class ViagemDataManager:
    _instance = None

    def __new__(cls, link):
        if cls._instance is None:
            cls._instance = super(ViagemDataManager, cls).__new__(cls)
            cls._instance._link = link
            cls._instance._data = None
        return cls._instance
    
    def get_data(self):
        if self._data is None:
            link_viagem = f'{self._link}/viagens.json'
            requisicao = requests.get(link_viagem)
            self._data = requisicao.json()
        return self._data
    
def get_viagens_por_motorista(motorista, link):
    manager = ViagemDataManager(link)
    data = manager.get_data()
    for key, value in data.items():
        if value['motorista'] == motorista:
            return key, json.dumps(value)
    
    return None, None