import requests

link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

def get_cartao_por_uid(uid, link):
    requisicao = requests.get(f"{link}/cartoes.json")
    dados_cartoes = requisicao.json()
    for key, value in dados_cartoes.items():
        if 'uid' in value and value['uid'] == uid:
            return key, value
    return None, None