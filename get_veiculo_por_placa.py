from flask import Flask, jsonify
import requests
import json

class VeiculoDataManager:
    _instance = None

    def __new__(cls, link):
        if cls._instance is None:
            cls._instance = super(VeiculoDataManager, cls).__new__(cls)
            cls._instance._link = link
            cls._instance._data = None
        return cls._instance
    
    def get_data(self):
        if self._data is None:
            link_veiculos = f'{self._link}/veiculos/.json'
            requisicao = requests.get(link_veiculos)
            self._data = requisicao.json()
        return self._data
    
def get_veiculo_por_placa(placa, link):
    manager = VeiculoDataManager(link)
    dados_veiculos = manager.get_data()
    
    for key, value in dados_veiculos.items():
        if value['placa'] == placa:
            return key, json.dumps(value)
    
    return None, None
