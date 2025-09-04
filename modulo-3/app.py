#sistema de autenticação integrado a um banco de dados que vai armazenar
#usuários e a partir dele gerenciamento de perfis que define
#qual usuário e o que ele pode fazer dentro de cada endpoint da API

from flask import Flask

app = Flask(__name__) #Name para executar de forma manual

@app.route("/")
def hello_world():
    return "hello world"

@app.route("/about")
def about():
    return "Pagina Sobre kk"

if __name__ == "__main__":
    app.run(debug=True) #Uso apenas em desenvolvimento local