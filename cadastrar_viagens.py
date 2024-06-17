import requests
import json
class ViagemBuilder:

    def __init__(self):
        self.dados = {}
    
    def origem(self, origem):
        self.dados['origem'] = origem
        return self
    
    def destino(self, destino):
        self.dados['destino'] = destino
        return self
    
    def data_inicio(self, data_inicio):
        self.dados['data_inicio'] = data_inicio
        return self
    
    def data_fim(self, data_fim):
        self.dados['data_fim'] = data_fim
        return self
    
    def distancia_total(self, distancia_total):
        self.dados['distancia_total'] = distancia_total
        return self
    
    def status_viagem(self, status_viagem):
        self.dados['status_viagem'] = status_viagem
        return self
    
    def motorista(self, motorista):
        self.dados['motorista'] = motorista
        return self
    
    def build(self):
        return self.dados

def cad_viagens(origem, destino, data_inicio, data_fim, distancia_total, status_viagem, motorista, link):
    dados = {'origem': origem, 'destino': destino, 'data_inicio': data_inicio, 'data_fim': data_fim, 'distancia_total': distancia_total, 'status_viagem': status_viagem, 'motorista': motorista}
    requisicao = requests.post(f'{link}/viagens/.json', data=json.dumps(dados))

    if requisicao.status_code == 200:
        return True
    else:
        return False

