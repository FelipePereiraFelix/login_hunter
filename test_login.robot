*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Login Com Sucesso
    Open Browser    http://localhost:5000/login    chrome
    Input Text    name=email    hunter@red.com
    Input Text    name=senha    senha123
    Press Keys    name=senha    ENTER
    Page Should Contain    Login realizado com sucesso
