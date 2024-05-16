from flask import Flask
import requests
from get_viagens_por_motorista import get_viagens_por_motorista

def atualizar_viagem(origem, destino, data_inicio, data_fim, distancia_total, status_viagem, motorista, link):

    viagem_id, dados_viagem = get_viagens_por_motorista(motorista, link)

    if viagem_id is None:
        return False
    
    link_viagem = f"{link}/viagens/{viagem_id}.json"

    dados_atualizados = {
        'motorista': motorista,
        'origem': origem,
        'destino': destino,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'distancia_total': distancia_total,
        'status_viagem': status_viagem
    }

    requisicao = requests.patch(link_viagem, json=dados_atualizados)

    if requisicao.status_code == 200:
        return True
    else:
        return False