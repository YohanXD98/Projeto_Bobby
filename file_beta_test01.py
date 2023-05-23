import time

def dialog(texto, pausa):
    for palavra in texto.split():
        print(palavra, end=' ', flush=True)
        time.sleep(pausa)

print("============BETA_TEST============")
text = "Olá! Eu sou o bobby :)"
pause = 0.5 

dialog(text, pause)
input()
if text == "sol":
    print("Ok, vamos falar sobre o sol")
