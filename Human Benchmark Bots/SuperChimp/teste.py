# import pyautogui
# import keyboard
# import time
#
# print("Posicione o mouse no canto SUPERIOR ESQUERDO da área e pressione Enter...")
# keyboard.wait('enter')
# x1, y1 = pyautogui.position()
# print(f"Primeiro ponto: ({x1}, {y1})")
#
# time.sleep(0.5)
#
# print("Agora posicione o mouse no canto INFERIOR DIREITO da área e pressione Enter...")
# keyboard.wait('enter')
# x2, y2 = pyautogui.position()
# print(f"Segundo ponto: ({x2}, {y2})")
#
# largura = x2 - x1
# altura = y2 - y1
#
# print("\n📏 Área capturada:")
# print(f"Posição inicial: ({x1}, {y1})")
# print(f"Tamanho: {largura} x {altura}")


import cv2
import mss
import numpy as np
import time

REGIAO_JOGO = {
    "top": 160,
    "left": 529,
    "width": 1000,
    "height": 500
}

time.sleep(3)
with mss.mss() as sct:
    img = np.array(sct.grab(REGIAO_JOGO))

# Cópia para debug visual
    img_debug = img.copy()
# Conversão para escala de cinza e binarização adaptativa
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 10
    )

    # Encontrar contornos
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imwrite("img_original.png", img)
    cv2.imwrite("img_debug.png", img_debug)
    cv2.imwrite("img_thresh.png", thresh)