from flask import Flask, render_template, request, redirect
from get_cartoes_por_uid import get_cartoes_por_uid
from atualizar_cartao import atualizar_cartao
import json

app = Flask(__name__)

link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

@app.route("/editar_cartao/<string:uid>", methods=["GET", "POST"])
def editar_cartao(uid):
    if request.method == "GET":
        # Chama a função para obter os detalhes do cartão pelo UID
        cartao_id, dados_cartao = get_cartoes_por_uid(uid, link)
        if dados_cartao is not None:
            cartao = json.loads(dados_cartao)
            return render_template("editar_cartao.html", cartao=cartao)
        else:
            # Se o cartão não for encontrado, redireciona para alguma página de erro
            return render_template("pagina_de_erro.html")
    elif request.method == "POST":
        # Processa os dados enviados do formulário de edição e atualiza o cartão
        novo_uid = request.form["uid"]
        if atualizar_cartao(uid, novo_uid, link):
            return redirect("/cartoes")
        else:
            # Se a atualização falhar, redireciona para alguma página de erro
            return render_template("pagina_de_erro.html")

if __name__ == "__main__":
    app.run(debug=True)
