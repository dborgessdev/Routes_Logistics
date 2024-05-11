from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"


""" cad viagens """
def cad_viagens(dados_inicio, dados_fim, distancia_total, status_viagem):
    dados = {'dados_inicio': dados_inicio, 'dados_fim': dados_fim, 'distancia_total': distancia_total, 'status_viagem': status_viagem}
    requisicao = requests.post(f'{link}/viagens/.json', data=json.dumps(dados))

    ("02/05, 15:25, São Paulo", "03/05, 15:25, Feira de Santana", "200Km", "concluida")

#colocar o site no ar
if __name__ == "__main__":
    #OBS: utiliza-se app.run(debug=True) para ligrar o debug, porém o console retornará o comando executado 2x gerando 2x dados para o banco de dados 
    app.run()