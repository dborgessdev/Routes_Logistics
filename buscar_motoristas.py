from flask import Flask
import requests
import json


app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

def get_motoristas():
    try:
        response = requests.get(f'{link}/motoristas.json')
        motoristas = response.json()
        if motoristas:
            return True, motoristas
        return False, {}
    except Exception as e:
        print(f"Erro ao obter motoristas: {e}")
        return False, {}
