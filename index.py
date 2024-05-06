from flask import Flask, render_template


app = Flask(__name__)

# 1) criar primeira pagina

"""
1.2)
Toda página no Flask sempre tem um "route" e uma função

route = link / caminho da página depois do domínio https ex: meuprojetoflask.com ou podemos criar a rota para a pagina de login meuprojetoflask.com/login

função = é o que queremos exibir em uma página

"""
#1.3) criando a rota / route através do decorator - atribui uma nova funcionalidade para a função logo abaixo dela
@app.route("/")
#1.4) criando a função:
def homepage():
    #1.5 solicitamos como retorno utilizando a função render template, o acesso a pagina através do arquivo html na pasta templates
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

#2 - Criando rotas dinâmicas
#aqui vemos que o route (decorator) passa a receber como complemento da url o parametro <nome_usuario> isso quer dizer que no momento em que quando preenchemos a url meusiteemflask/usuarios/davi o Flask irá criar automaticamente uma pogina para o usuário informado 
@app.route("/usuarios/<nome_usuario>")
#2.1 Criando a função:
#aqui vemos que o nome da rota (usuarios) continua a se repetir porém a função receberá como parametro a variável nome_usuario
def usuarios(nome_usuario):
    #2.2 Em nosso retorno, dentro da função importada render template informamos normalmente o nome do arquivo designado para essa pagina, criado na pasta templates e informamos que o arquivo irá chamar a função nome_usuario, que recebe como parametro o nome do usuário, assim, de maneira dinâmica, ao digitar: http://127.0.0.1:5000/usuarios/davi será gerado automaticamente através do html, uma página do usuario "davi"
    return render_template("usuarios.html", nome_usuario=nome_usuario)

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)