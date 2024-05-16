from flask import Flask
import requests
from get_veiculo_por_placa import get_veiculo_por_placa

def atualizar_veiculo(placa, marca, modelo, ano_fabricacao, tipo_veiculo, capacidade_carga, tag_rfidplaca, link):

    veiculo_id, dados_veiculo = get_veiculo_por_placa(placa, link)

    if veiculo_id is None:
        return False
    link_veiculo = f"{link}/veiculos/{veiculo_id}.json"

    dados_atualizados = {
        "placa": placa,
        "marca": marca,
        "modelo": modelo,
        "ano_fabricacao": ano_fabricacao,
        "tipo_veiculo": tipo_veiculo,
        "capacidade_carga": capacidade_carga,
        "tag_rfid": tag_rfidplaca
    }

    requisicao = requests.patch(link_veiculo, json=dados_atualizados)

    if requisicao.status_code == 200:
        return True
    else:
        return False