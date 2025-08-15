import pyautogui
import time

# Coordenada do ponto que vamos monitorar
posicao = (971, 555)

# Função para detectar se a tela está verde nessa posição
def tela_verde():
    r, g, b = pyautogui.screenshot().getpixel(posicao)
    # Considera verde se o píxel tiver bastante verde e pouco vermelho/azul
    return r > 65 and g > 200 and b > 95

# Espera 3 segundos antes de começar (tempo para posicionar o jogo/janela)
time.sleep(3)

# Clica na posição inicial para iniciar
pyautogui.click(*posicao)

cliques = 0  # contador de cliques realizados

# Loop principal: repete até fazer 5 cliques na tela verde
while cliques != 5:
    if tela_verde():  # se detectar verde na posição
        pyautogui.click(*posicao)  # clica uma vez
        time.sleep(0.5)            # espera meio segundo
        pyautogui.click(*posicao)  # clica novamente
        cliques += 1               # incrementa o contador
