import requests

def deletar_motorista(nome, link):
    try:
        # Enviar requisição GET para obter a lista de motoristas
        requisicao = requests.get(f'{link}/motoristas/.json')
        motoristas = requisicao.json()
        
        # Procurar pelo nome do motorista
        for motorista_id, dados_motorista in motoristas.items():
            if dados_motorista['nome'] == nome:
                # Deletar o motorista encontrado
                delete_requisicao = requests.delete(f'{link}/motoristas/{motorista_id}.json')
                if delete_requisicao.status_code == 200:
                    return True
        return False
    except Exception as e:
        print(f"Erro ao deletar o motorista: {e}")
        return False
