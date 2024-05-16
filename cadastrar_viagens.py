from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"


""" cad viagens """
def cad_viagens(origem, destino, data_inicio, data_fim, distancia_total, status_viagem, motorista):
    dados = {'origem': origem, 'destino': destino, 'data_inicio': data_inicio, 'data_fim': data_fim, 'distancia_total': distancia_total, 'status_viagem': status_viagem, 'motorista': motorista}
    requisicao = requests.post(f'{link}/viagens/.json', data=json.dumps(dados))

    ('Feira de Santana', 'São Paulo', '02/05, 15:25', '03/05, 15:25', '200Km', 'concluida', 'José')

#colocar o site no ar
if __name__ == "__main__":
    #OBS: utiliza-se app.run(debug=True) para ligrar o debug, porém o console retornará o comando executado 2x gerando 2x dados para o banco de dados 
    app.run()