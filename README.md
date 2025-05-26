# 🕵️‍♂️ Login Hunter
Projeto simples pra caçar bugs no login com Python, Pytest, Selenium e Robot Framework. Seja o caçador, não a caça.

## ⚙️ Funcionalidades
✅ Testes automatizados com Pytest (Python)

🌐 Automação web com Selenium

🤖 Testes com Robot Framework

📁 Pastas organizadas, código limpo

 🔒 Proteção contra subir dados sensíveis

🚀 Como usar
Clone o repo e entre na pasta:

```bash
git clone https://github.com/FelipePereiraFelix/login_hunter
cd login_hunter
```
### Instale as dependências:

```bash
pip install -r requirements.txt
```

### Configure os usuários (credenciais locais):

```bash
cp users_template.py users.py
```

Edite users.py com suas credenciais reais, ou credenciais fake para testes.

## ⚠️ Nunca envie users.py pro GitHub, mantenha seus dados seguros!

🧪 Rodando os testes
Pytest (Python):

```bash
pytest test_login.py
```
## Robot Framework:

Nome do Arquivo: robot test_login.robot

### 🗂 Estrutura do projeto
```bash
login_hunter/
├── test_login.py
├── test_login.robot
├── users_template.py
├── .gitignore
├── requirements.txt
└── README.md
```
🔥 Sobre

Feito para testes e aprendizados de Selenium, Robot Framework, Python, Pytest e Cybersecurity. 
