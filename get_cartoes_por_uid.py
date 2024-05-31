import requests
import json

def get_cartoes_por_uid(uid, link):
    try:
        requisicao = requests.get(f'{link}/cartoes/.json')
        cartoes = requisicao.json()
        for cartao_id, dados_cartao in cartoes.items():
            if dados_cartao.get("uid" ) == uid:
                return cartao_id, json.dumps(dados_cartao)
        return None, None
    except Exception as e:
        print(f"Erro ao obter o cartão pelo UID: {e}")
        return None, None