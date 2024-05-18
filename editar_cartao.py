from flask import Flask, render_template, request, redirect
from get_cartao_por_uid import get_cartao_por_uid
from atualizar_cartao import atualizar_cartao
import json

app = Flask(__name__)

link = "https://projetoflask-fb-default-rtdb.firebaseio.com/"

@app.rout("/editar_cartao/<string:uid>", methods=["GET", "POST"])
def editar_cartao(uid):
    if request.method == "GET":
        cartao_id, dados_cartao = get_cartao_por_uid(uid, link)
        if dados_cartao is not None:
            cartao = json.loads(dados_cartao)
            return render_template("editar_cartao.html", cartao=cartao)
        else:
            return render_template("pagina_de_erro.html")
    elif request.method == "POST":
        uid = request.form["uid"]
        if atualizar_cartao(uid, link):
            return redirect("/cartoes")
        else:
            return render_template("pagina_de_erro.html")

if __name__ == "__main__":
    app.run()