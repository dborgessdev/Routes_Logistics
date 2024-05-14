from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

def cad_veiculos(placa, marca, modelo, ano_fabricacao, tipo_veiculo, capacidade_carga, tag_rfid):
    dados = { 'placa': placa, 'marca': marca, 'modelo': modelo, 'ano_fabricacao': ano_fabricacao, 'tipo_veiculo':	tipo_veiculo, 'capacidade_carga': capacidade_carga, 'tag_rfid': tag_rfid}
    requisicao = requests.post(f'{link}/veiculos/.json', data=json.dumps(dados))
    #criar um veiculo
    """print(requisicao)
    print(requisicao.text) 
    pode ser usado como forma de debug; 
    """
    ("Luiz", "00090040013", "02523654" , "kajsdh5465aksj16","15/11/26", "asdasd" , "asdsadas", )


#colocar o site no ar
if __name__ == "__main__":
    #OBS: utiliza-se app.run(debug=True) para ligrar o debug, porém o console retornará o comando executado 2x gerando 2x dados para o banco de dados 
    app.run()