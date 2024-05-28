from flask import Flask, render_template, request, redirect, send_file, url_for, flash, session
import requests
import json
#AUTH IMPORTS
import firebase_admin
from firebase_admin import auth
import firebase_config  # Importando as configurações do Firebase
import pyrebase
from functools import wraps
#DASHBOARD IMPORTS
import pandas as pd
import plotly.express as px
from io import BytesIO
#VEICULOS
from buscar_veiculos import get_veiculos
from cadastrar_veiculos import cad_veiculos
from get_veiculo_por_placa import get_veiculo_por_placa
from atualizar_veiculo import atualizar_veiculo
from deletar_veiculo import deletar_veiculo
#MOTORISTAS
from buscar_motoristas import get_motoristas
from cadastrar_motoristas import cad_motoristas
from get_motorista_por_nome import get_motorista_por_nome
from atualizar_motorista import atualizar_motorista
from deletar_motorista import deletar_motorista
#VIAGENS
from buscar_viagens import get_viagens
from cadastrar_viagens import cad_viagens
from get_viagens_por_motorista import get_viagens_por_motorista
from atualizar_viagem import atualizar_viagem
from deletar_viagem import deletar_viagem
#CARTOES
from buscar_cartoes import get_cartoes
from cadastrar_cartoes import cad_cartao
from get_cartoes_por_uid import get_cartoes_por_uid
from atualizar_cartao import atualizar_cartao
from deletar_cartao import deletar_cartao



app = Flask(__name__)
link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"
app.secret_key = 'p1y2t3h4o5n6p1y2t3h4o5n6p1y2t3h4o5n6'  # Use uma chave secreta mais segura em produção

firebase_config = {

'apiKey': "AIzaSyB4D4mZeuXfT1fSCqpkSljotPWh3YfjCGY",
'authDomain': "projetoflask-fb.firebaseapp.com",
'databaseURL': "https://projetoflask-fb-default-rtdb.firebaseio.com",
'projectId': "projetoflask-fb",
'storageBucket': "projetoflask-fb.appspot.com",
'messagingSenderId': "134324160615",
'appId': "1:134324160615:web:8ed0bb84526c5c146b6cc2",
'measurementId': "G-ZVZ9B7PQP3"
};


firebase = pyrebase.initialize_app(firebase_config)
auth_pyrebase = firebase.auth()



#### AUTH ##### Rota para a página de login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']
        
        try:
            # Simulação de verificação de senha
            user = auth.get_user_by_email(email)
            session['user'] = user.uid
            return redirect(url_for('show_dashboard'))
        except Exception as e:
            flash('Credenciais inválidas, tente novamente.')
            return redirect(url_for('login'))
    
    return render_template('login.html')

# Rota para a página de registro
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        username = request.form['firstname']
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['userType']
        
        try:
            user = auth.create_user(
                email=email,
                password=password,
                display_name=username
            )
            flash('Usuário registrado com sucesso!')
            return redirect(url_for('login'))
        except Exception as e:
            flash('Erro ao registrar usuário, tente novamente.')
            return redirect(url_for('registrar'))
    
    return render_template('registrar.html')

# Rota para logout
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

# Verificação de autenticação
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Protegendo a rota do dashboard
@app.route('/dashboard')
@login_required
def show_dashboard():
    requisicao = requests.get(f'{link}/viagens.json')
    viagens = requisicao.json()
    
    if not viagens:
        return render_template('sem_viagens.html')
    
    data = []
    for key, viagem in viagens.items():
        motorista = viagem.get('motorista')
        distancia = float(viagem.get('distancia_total', 0))
        data.append([motorista, distancia])
    
    df = pd.DataFrame(data, columns=['Motorista', 'Distancia'])
    fig = px.bar(df, x='Motorista', y='Distancia', title='Distância Total por Motorista')
    graph_html = fig.to_html(full_html=False)
    
    return render_template('dashboard.html', graph_html=graph_html)

@app.route('/homepage')
@login_required
def homepage():
    return render_template('homepage.html')

#### DASHBOARD ####
# Rota para exibir o dashboard
@app.route('/dashboard')
def dashboard_view():
    requisicao = requests.get(f'{link}/viagens.json')
    viagens = requisicao.json()
    
    if not viagens:
        # Se não houver viagens, renderize uma página informando isso
        return render_template('sem_viagens.html')
    
    data = []
    for key, viagem in viagens.items():
        motorista = viagem.get('motorista')
        distancia = float(viagem.get('distancia_total', 0))
        data.append([motorista, distancia])
    
    df = pd.DataFrame(data, columns=['Motorista', 'Distancia'])
    fig = px.bar(df, x='Motorista', y='Distancia', title='Distância Total por Motorista')
    graph_html = fig.to_html(full_html=False)
    
    return render_template('dashboard.html', graph_html=graph_html)

# Rota para baixar o arquivo Excel
@app.route('/download_excel')
def download_excel():
    import pandas as pd
    import io
    
    # Obter dados das viagens do Firebase
    response = requests.get(f'{link}/viagens.json')
    viagens = response.json()
    
    # Processar os dados
    data = []
    for key, viagem in viagens.items():
        motorista = viagem.get('motorista')
        distancia_total = float(viagem.get('distancia_total', 0))
        data.append({'Motorista': motorista, 'Distancia Total': distancia_total})
    
    df = pd.DataFrame(data)
    output = io.BytesIO()
    
    # Gerar arquivo Excel com Pandas
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Viagens')
    
    output.seek(0)
    
    return send_file(output, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                     download_name='viagens.xlsx', as_attachment=True)
#### VEICULOS ####

@app.route("/veiculos")
def veiculos():
    requisicao_veiculos, dados_veiculos = get_veiculos()
    veiculos = json.loads(dados_veiculos)
    return render_template("veiculos.html", veiculos=veiculos)

@app.route("/veiculos_cadastro")
def veiculos_cadastro():
    return render_template("veiculos_cadastro.html")

@app.route("/cadastrar_veiculo", methods=["POST"])
def cadastrar_veiculo():
    if request.method == "POST":
        placa = request.form["placa"]
        marca = request.form["marca"]
        modelo = request.form["modelo"]
        ano_fabricacao = request.form["ano_fabricacao"]
        tipo_veiculo = request.form["tipo_veiculo"]
        capacidade_carga = request.form["capacidade_carga"]
        tag_rfid = request.form["tag_rfid"]
        cad_veiculos(placa, marca, modelo, ano_fabricacao, tipo_veiculo, capacidade_carga, tag_rfid)  # Chamada da função para cadastrar veículo
        return redirect("/veiculos")
    else:
        return "Erro: Método de requisição falhou ou não é POST!"
    
@app.route("/editar_veiculo/<string:placa>", methods=["GET", "POST"])
def editar_veiculo(placa):
    if request.method == "GET":
        # Chama a função para obter os detalhes do veículo pelo placa
        veiculo_id, dados_veiculo = get_veiculo_por_placa(placa, link)
        if dados_veiculo is not None:
            veiculo = json.loads(dados_veiculo)
            return render_template("editar_veiculo.html", veiculo=veiculo)
        else:
            # Se o veículo não for encontrado, redireciona para alguma página ou retorna uma mensagem
            return "Veículo não encontrado.", 404
    elif request.method == "POST":
        # Processa os dados enviados do formulário de edição e atualiza o veículo
        placa = request.form["placa"]
        marca = request.form["marca"]
        modelo = request.form["modelo"]
        ano_fabricacao = request.form["ano_fabricacao"]
        tipo_veiculo = request.form["tipo_veiculo"]
        capacidade_carga = request.form["capacidade_carga"]
        tag_rfid = request.form["tag_rfid"]
        # Chama a função para atualizar o veículo
        if atualizar_veiculo(placa, marca, modelo, ano_fabricacao, tipo_veiculo, capacidade_carga, tag_rfid, link):
            return redirect("/veiculos")
        
@app.route("/deletar_veiculo", methods=["POST"])
def del_deletar_veiculo():
    placa = request.form["placa"]
    if deletar_veiculo(placa, link):  # Passando os parâmetros corretos para deletar_veiculo
        return redirect("/veiculos")
    else:
        return "Erro ao deletar veículo."

#### MOTORISTAS ####

@app.route('/motoristas')
@login_required
def motoristas():
    has_motoristas, motoristas = get_motoristas()
    if has_motoristas:
        motoristas = json.loads(json.dumps(motoristas))  # Convertendo para um dicionário
    else:
        motoristas = {}

    return render_template('motoristas.html', motoristas=motoristas)

@app.route("/motoristas_cadastro")
def motoristas_cadastro():
    return render_template("motoristas_cadastro.html")

@app.route("/cad_motorista", methods=["POST"])
def cad_motorista():
    if request.method == "POST":
        nome = request.form["nome"] 
        cpf = request.form["cpf"]
        cnh = request.form["cnh"]
        id_veiculo = request.form["id_veiculo"]
        validade_cnh = request.form["validade_cnh"]
        cad_motoristas(nome, cpf, cnh, id_veiculo, validade_cnh)
        return redirect("/motoristas")
    else:
        return "Erro: Método de requisição falhou ou não é POST!"
    
@app.route("/editar_motorista/<string:nome>", methods=["GET", "POST"])
def editar_motorista(nome):
    if request.method == "GET":
        # Chama a função para obter os detalhes do motorista pelo nome
        motorista_id, dados_motorista = get_motorista_por_nome(nome, link)
        if dados_motorista is not None:
            motorista = json.loads(dados_motorista)
            return render_template("editar_motorista.html",motorista=motorista)
        else:
            # Se o motorista não for encontrado, redireciona para alguma página de erro
            return render_template("pagina_de_erro.html")
    elif request.method == "POST":
        # Processa os dados enviados do formulário de edição e atualiza o motorista
        cpf = request.form["cpf"]
        cnh = request.form["cnh"]
        id_veiculo = request.form["id_veiculo"]
        validade_cnh = request.form["validade_cnh"]
        # Chama a função para atualizar o motorista
        if atualizar_motorista(nome, cpf, cnh, id_veiculo, validade_cnh, link):
            return redirect("/motoristas")
        else:
            # Se a atualização falhar, redireciona para alguma página de erro
            return render_template("pagina_de_erro.html")
        
@app.route("/deletar_motorista", methods=["POST"])
def del_deletar_motorista():
    nome = request.form["nome"]
    if deletar_motorista(nome, link):  # Passando os parâmetros corretos para deletar_motorista
        return redirect("/motoristas")
    else:
        return "Erro ao deletar motorista."
    
##### VIAGENS #####

@app.route("/viagens")
def viagens():
    requisicao_viagem, dados_viagem = get_viagens()
    viagens = json.loads(dados_viagem)  # Convertendo os dados para um dicionário
    return render_template("viagens.html", viagens=viagens)


@app.route('/viagens_cadastro')
def viagens_cadastro():
    has_motoristas, motoristas = get_motoristas()
    if not has_motoristas:
        return render_template('sem_motoristas.html')
    return render_template('viagens_cadastro.html', motoristas=motoristas)

@app.route("/cadastrar_viagem", methods=["POST"])
def cadastrar_viagem():
    if request.method == "POST":
        origem = request.form["origem"]
        destino = request.form["destino"]
        data_inicio = request.form["data_inicio"]
        data_fim = request.form["data_fim"]
        distancia_total = request.form["distancia_total"]
        status_viagem = request.form["status_viagem"]
        motorista = request.form["motorista"]
        cad_viagens(origem, destino, data_inicio, data_fim, distancia_total, status_viagem, motorista)  # Chamada da função para cadastrar viagem
        return redirect("/viagens")
    else:
        return "Erro: Método de requisição falhou ou não é POST!"
    
@app.route("/editar_viagem/<string:motorista>", methods=["GET", "POST"])
def editar_viagem(motorista):
    if request.method == "GET":
        # Chama a função para obter os detalhes da viagem pelo motorista
        viagem_id, dados_viagem = get_viagens_por_motorista(motorista, link)
        if dados_viagem is not None:
            viagem = json.loads(dados_viagem)
            return render_template("editar_viagem.html", viagem=viagem)
        else:
            # Se a viagem não for encontrada, redireciona para alguma página ou retorna uma mensagem
            return "Viagem não encontrada.", 404
    elif request.method == "POST":
        # Processa os dados enviados do formulário de edição e atualiza a viagem
        origem = request.form["origem"]
        destino = request.form["destino"]
        data_inicio = request.form["data_inicio"]
        data_fim = request.form["data_fim"]
        distancia_total = request.form["distancia_total"]
        status_viagem = request.form["status_viagem"]
        # Chama a função para atualizar a viagem
        if atualizar_viagem(origem, destino, data_inicio, data_fim, distancia_total, status_viagem, motorista, link):
            return redirect("/viagens")
        else:
            # Se a atualização falhar, redireciona para alguma página ou retorna uma mensagem
            return "Falha ao atualizar a viagem.", 500
        
@app.route("/deletar_viagem", methods=["POST"])
def del_deletar_viagem():
    motorista = request.form["motorista"]
    if deletar_viagem(motorista, link):  # Passando os parâmetros corretos para deletar_viagem
        return redirect("/viagens")
    else:
        return "Erro ao deletar viagem."

#### CARTÕES ####
@app.route("/cartoes")
def cartoes():
    dados_cartao = get_cartoes()
    return render_template("cartoes.html", cartoes=dados_cartao)

@app.route("/cartoes_cadastro")
def cartoes_cadastro():
    return render_template("cartoes_cadastro.html")

@app.route("/cadastrar_cartao", methods=["POST"])  # Rota para cadastrar cartão
def cadastrar_cartao():
    if request.method == "POST":
        uid = request.form["uid"]  # Obtendo o UID do formulário
        if cad_cartao(uid, link):  # Chamando a função para cadastrar cartão
            return redirect("/cartoes")  # Redirecionando após o cadastro
        else:
            return "Erro ao cadastrar cartão."  # Retornando mensagem de erro em caso de falha
    else:
        return "Erro: Método de requisição falhou ou não é POST!"  # Tratamento para método de requisição diferente de POST
    
@app.route("/editar_cartao/<string:uid>", methods=["GET", "POST"])
def editar_cartao_route(uid):
    if request.method == "GET":
        cartao_id, dados_cartao = get_cartoes_por_uid(uid, link)
        if dados_cartao is not None:
            cartao = json.loads(dados_cartao)
            return render_template("editar_cartao.html", cartao=cartao)
        else:
            return render_template("pagina_de_erro.html")
    elif request.method == "POST":
        novo_uid = request.form["uid"]
        if atualizar_cartao(uid, novo_uid, link):
            return redirect("/cartoes")
        else:
            return render_template("pagina_de_erro.html")


@app.route("/deletar_cartao/<string:uid>", methods=["POST"])
def deletar_cartao_route(uid):
    if deletar_cartao(uid, link):
        return redirect("/cartoes")
    else:
        return "Erro ao deletar cartão."
    
    
if __name__ == "__main__":
    app.run(debug=True)