import requests
import json

class CartaoDataManager:
    _instance = None

    def __new__(cls, link):
        if cls._instance is None:
            cls._instance = super(CartaoDataManager, cls).__new__(cls)
            cls._instance._link = link
            cls._instance._data = None
        return cls._instance

    def get_data(self):
        if self._data is None:
            link_cartoes = f'{self._link}/cartoes/.json'
            requisicao = requests.get(link_cartoes)
            self._data = requisicao.json()
        return self._data

def get_cartoes_por_uid(uid, link):
    try:
        manager = CartaoDataManager(link)
        cartoes = manager.get_data()
        
        for cartao_id, dados_cartao in cartoes.items():
            if dados_cartao.get("uid") == uid:
                return cartao_id, json.dumps(dados_cartao)
        
        return None, None
    except Exception as e:
        print(f"Erro ao obter o cartão pelo UID: {e}")
        return None, None
