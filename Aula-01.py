import pyautogui
import time

#AUTOMAZINDO CADASTRO DE ITENS 

#ESPERA DE TEMPO PARA CADA EXECUCAO 
pyautogui.PAUSE = 0.5


#Abrir o navegador (OPERA)
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

#ENTRAR NO SITE DO SISTEM

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


#ESTE FUNCIONA PARA ESPERAR O CARREGAMENTO DO SITE PARA DEPOIS PASSAR PARA A PROXIMA EXECUCAO
time.sleep(2)

#FAZENDO LOGIN NO SITE
pyautogui.click(x=710, y=358)
pyautogui.write("testelogin@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha123")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)
#ABRIR/IMPORTAR BASE DE DADOS 
 
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)   

for linha in tabela.index:
    #CODIGO DO PRODUTO
    codigo = str(tabela.loc[linha, "codigo"])
    #CLICAR NO CAMPO DO CODIGO DO PRODUTO
    pyautogui.click(x=707, y=242)

    #PREENCHER O CODIDO
    pyautogui.write(codigo)

    #PASSAR PARA O PROXIMO CAMPO
    pyautogui.press("tab")

    #marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    pyautogui.press("tab")

    #tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha,"categoria"]))

    pyautogui.press("tab")

    #preco
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))

    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha,"custo"]))

    pyautogui.press("tab")

    #obs
    obs = (str(tabela.loc[linha, "obs"]))

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    #apertar o botao
    pyautogui.press("enter")
    pyautogui.scroll(500)
