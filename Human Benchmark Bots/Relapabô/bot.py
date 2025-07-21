import pyautogui
import time

posicao = (971, 555)

def tela_verde():
    r, g, b = pyautogui.screenshot().getpixel(posicao)
    return r > 65 and g > 200 and b > 95

time.sleep(3)
pyautogui.click(*posicao)
cliques = 0

while cliques != 5:
    if tela_verde():
        pyautogui.click(*posicao)
        time.sleep(0.5)
        pyautogui.click(*posicao)
        cliques +=1