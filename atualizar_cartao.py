import requests
import json
from get_cartoes_por_uid import get_cartoes_por_uid

def atualizar_cartao(uid_antigo, uid_novo, status, link):
    try:
        # Busca o cartão existente pelo UID antigo
        cartao_id, _ = get_cartoes_por_uid(uid_antigo, link)
        if cartao_id:
            # Atualiza os dados do cartão com o novo UID e status
            dados = {"uid": uid_novo, "status": status}
            requisicao = requests.put(f'{link}/cartoes/{cartao_id}.json', data=json.dumps(dados))
            if requisicao.status_code == 200:
                return True
        return False
    except Exception as e:
        print(f"Erro ao atualizar o cartão: {e}")
        return False
