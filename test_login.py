import requests

BASE_URL = "http://localhost:5000/login"

def test_login_sucesso():
    data = {
        "email": "hunter@red.com",
        "senha": "senha123"
    }
    response = requests.post(BASE_URL, data=data)
    assert "Login realizado com sucesso" in response.text

def test_login_falha_senha_errada():
    data = {
        "email": "hunter@red.com",
        "senha": "errada"
    }
    response = requests.post(BASE_URL, data=data)
    assert "Usuário ou senha inválido" in response.text

def test_login_falha_email_inexistente():
    data = {
        "email": "guts@berserk.com",
        "senha": "grrr"
    }
    response = requests.post(BASE_URL, data=data)
    assert "Usuário ou senha inválido" in response.text
