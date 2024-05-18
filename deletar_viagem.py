import requests

def deletar_viagem(motorista, link):
    try:
        # Enviar requisição GET para obter a lista de viagens
        requisicao = requests.get(f'{link}/viagens/.json')
        viagens = requisicao.json()
        
        # Procurar pela viagem do motorista
        for viagem_id, dados_viagem in viagens.items():
            if dados_viagem['motorista'] == motorista:
                # Deletar a viagem encontrada
                delete_requisicao = requests.delete(f'{link}/viagens/{viagem_id}.json')
                if delete_requisicao.status_code == 200:
                    return True
        return False
    except Exception as e:
        print(f"Erro ao deletar a viagem: {e}")
        return False
