from flask import Flask, render_template
import requests
import json


app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

""" def cad_motorista, através dessa function utilizamos as bibliotecas JSON e REQUESTS
para o preenchimento de dados (através da variavel dados) no banco de dados do firebase da tabela de motoristas"""

def cad_motoristas(nome, cpf, cnh, id_veiculo, validade_cnh):
    dados = { 'nome': nome, 'cpf':cpf, 'cnh':cnh, 'id_veiculo': id_veiculo, 'validade_cnh':	validade_cnh}
    requisicao = requests.post(f'{link}/motoristas/.json', data=json.dumps(dados))
    #criar um motorista
    """print(requisicao)
    print(requisicao.text) 
    pode ser usado como forma de debug; 
    """
    ("Putin", "00090040013", "02523654" , "kajsdh5465aksj16","15/11/26")

#colocar o site no ar
if __name__ == "__main__":
    #OBS: utiliza-se app.run(debug=True) para ligrar o debug, porém o console retornará o comando executado 2x gerando 2x dados para o banco de dados 
    app.run()