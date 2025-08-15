import mss
import numpy as np
import pyautogui
import time

# Define a região da tela para capturar (coordenadas e tamanho)
regiao = {'top': 210, 'left': 546, 'width': 1015, 'height': 444}

# Espera 3 segundos antes de começar (tempo para você posicionar a janela/jogo)
time.sleep(3)

# Clica em um ponto inicial específico
pyautogui.click(973, 424)

# Executa o processo 31 vezes
for i in range(31):
    with mss.mss() as sct:
        # Captura a região da tela como array NumPy
        screenshot = np.array(sct.grab(regiao))[:, :, :3]  # pega apenas RGB (ignora alpha)

        # Cor alvo (branco puro)
        target_color_np = np.array((255, 255, 255))

        # Calcula a "distância" de cada píxel até a cor alvo
        distance = np.linalg.norm(screenshot - target_color_np, axis=2)

        # Cria uma máscara de pixels que estão próximos da cor alvo (tolerância <= 10)
        mask = distance <= 10

        # Pega as coordenadas (y, x) dos pixels que batem com a cor
        cords = np.argwhere(mask)

        # Pega o primeiro píxel que bateu com a cor
        y_rel, x_rel = cords[0]

        # Converte coordenadas relativas para coordenadas absolutas na tela
        x_click = regiao['left'] + x_rel
        y_click = regiao['top'] + y_rel

        # Clica nesse pixel
        pyautogui.click(x_click, y_click)
