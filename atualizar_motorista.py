from flask import Flask
import requests
from get_motorista_por_nome import get_motorista_por_nome
# atualizar_motorista.py

def atualizar_motorista(nome, cpf, cnh, id_veiculo, validade_cnh, link):
    # Primeiro, obtemos o ID do motorista a partir do nome
    motorista_id, dados_motorista = get_motorista_por_nome(nome, link)
    
    # Se não encontrarmos o motorista, não podemos atualizá-lo
    if motorista_id is None:
        return False
    
    link_motorista = f"{link}/motoristas/{motorista_id}.json"
    
    # Atualizamos os dados do motorista
    dados_atualizados = {
        "nome": nome,
        "cpf": cpf,
        "cnh": cnh,
        "id_veiculo": id_veiculo,
        "validade_cnh": validade_cnh
    }
    
    requisicao = requests.patch(link_motorista, json=dados_atualizados)
    
    if requisicao.status_code == 200:
        return True
    else:
        return False
