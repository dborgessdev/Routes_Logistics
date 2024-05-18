import requests

def deletar_cartao(uid, link):
    try:
        # Encontre o cartão pelo UID
        requisicao = requests.get(f'{link}/cartoes/.json')
        cartoes = requisicao.json()
        for cartao_id, dados_cartao in cartoes.items():
            if dados_cartao.get("uid") == uid:
                # Delete o cartão encontrado
                delete_requisicao = requests.delete(f'{link}/cartoes/{cartao_id}.json')
                if delete_requisicao.status_code == 200:
                    return True
        return False
    except Exception as e:
        print(f"Erro ao deletar o cartão: {e}")
        return False