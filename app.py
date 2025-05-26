from flask import Flask, render_template, request
from users import USERS

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo ao Login Hunter! Vá para /login'

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        if email in USERS and USERS[email] == senha:
            message = 'Login realizado com sucesso'
        else:
            message = 'Usuário ou senha inválido'

    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
