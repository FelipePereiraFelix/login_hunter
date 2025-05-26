from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_login_selenium():
    driver = webdriver.Chrome()  # Usa o ChromeDriver no PATH

    driver.get("http://localhost:5000/login")

    # Localiza os campos de e-mail e senha
    campo_email = driver.find_element(By.NAME, "email")
    campo_senha = driver.find_element(By.NAME, "senha")

    campo_email.send_keys("hunter@red.com")
    campo_senha.send_keys("senha123")

    campo_senha.send_keys(Keys.RETURN)  # Simula o Enter

    time.sleep(1)  # Espera a página carregar a resposta

    assert "Login realizado com sucesso" in driver.page_source

    driver.quit()
