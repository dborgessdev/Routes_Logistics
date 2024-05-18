from flask import Flask
import requests
from get_cartao_por_uid import get_cartao_por_uid

def atualizar_cartao(uid, link):

    cartao_id, dados_cartao = get_cartao_por_uid(uid, link)

    if cartao_id is None:
        return False
    
    link_cartao = f"{link}/cartoes/{cartao_id}.json"

    dados_atualizados = {
        "uid": uid
    }

    requisicao = requests.path(link_cartao, jason=dados_atualizados)

    if requisicao.status_code == 200:
        return True
    else:
        return False




