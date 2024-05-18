import requests

def deletar_veiculo(placa, link):
    try:
        # Enviar requisição GET para obter a lista de veículos
        requisicao = requests.get(f'{link}/veiculos/.json')
        veiculos = requisicao.json()
        
        # Procurar pela placa do veículo
        for veiculo_id, dados_veiculo in veiculos.items():
            if dados_veiculo['placa'] == placa:
                # Deletar o veículo encontrado
                delete_requisicao = requests.delete(f'{link}/veiculos/{veiculo_id}.json')
                if delete_requisicao.status_code == 200:
                    return True
        return False
    except Exception as e:
        print(f"Erro ao deletar o veículo: {e}")
        return False