from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

usuarios = {}

@app.route("/")
def home():
    return render_template("loginHome.html")


@app.route("/login", methods=["POST"])
def login():

    entrada = request.form["usuario"]   # pode ser user ou email
    senha = request.form["senha"]

    for usuario, dados in usuarios.items():

        if (entrada == usuario or entrada == dados["email"]) \
           and dados["senha"] == senha:

            return f"Bem-vindo {usuario}"

    return "Usuário ou senha incorretos"


@app.route("/cadastro")
def cadastro():
    return render_template("cadastroHome.html")


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    usuario = request.form["usuario"]
    email = request.form["email"]
    senha = request.form["senha"]

    usuarios[usuario] = {
        "email": email,
        "senha": senha
    }
    
    print(usuarios)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)