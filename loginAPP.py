from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("loginHome.html")

@app.route("/loginHome.html", methods=["POST"])
def login():
    usuario = request.form["usuario"]
    senha = request.form["senha"]

    if usuario == "admin" and senha == "1234":
        return "Login realizado com sucesso!"
    else:
        return "Usuário ou senha incorretos"

if __name__ == "__main__":
    app.run(debug=True)