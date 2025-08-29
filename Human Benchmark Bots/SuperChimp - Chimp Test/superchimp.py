import cv2
import numpy as np
import pytesseract
import pyautogui
import time
import mss

# Caminho do executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Região da tela onde o jogo aparece
regiao_jogo = {
    "top": 160,
    "left": 550,
    "width": 850,
    "height": 530
}

def detectar_numeros():
    with mss.mss() as sct:
        img = np.array(sct.grab(regiao_jogo))  # captura a região do jogo

    # Converte a imagem para tons de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binariza a imagem invertida para destacar números
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 10
    )

    # Detecta contornos na imagem
    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    numeros = []

    for i, cnt in enumerate(contornos):
        x, y, w, h = cv2.boundingRect(cnt)

        # Filtra retângulos com tamanho compatível com números
        if 20 < w < 150 and 20 < h < 150:
            roi = gray[y:y+h, x:x+w]

            # Pré-processa ROI -> binariza + engrossa
            roi_bin = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
            kernel = np.ones((2,2), np.uint8)
            roi_bin = cv2.dilate(roi_bin, kernel, iterations=1)

            # OCR tentativa 1
            texto = pytesseract.image_to_string(
                roi_bin, config="--psm 7 -c tessedit_char_whitelist=0123456789"
            ).strip()

            numero = ''.join(filter(str.isdigit, texto))

            # Se falhou, tenta outro modo
            if not numero.isdigit():
                texto = pytesseract.image_to_string(
                    roi_bin, config="--psm 13 -c tessedit_char_whitelist=0123456789"
                ).strip()
                numero = ''.join(filter(str.isdigit, texto))

            # Converte coordenadas relativas para absolutas na tela
            abs_x = regiao_jogo["left"] + x + w // 2
            abs_y = regiao_jogo["top"] + y + h // 2
            numeros.append((int(numero), abs_x, abs_y))

    # Retorna a lista de números detectados ordenada
    return sorted(numeros)

# Função para clicar no botão "Start" ou "Continuar"
def clicarbtn(top, left, width, height):
    print('Iniciando o código.')
    with mss.mss() as sct:
        region = {"top": top, "left": left, "width": width, "height": height}
        screenshot1 = sct.grab(region)
        img1 = np.array(screenshot1)[:, :, :3]

    # Cor alvo (cinza-escuro)
    target_color_np = np.array((51, 51, 51))
    distance = np.linalg.norm(img1 - target_color_np, axis=2)
    mask = distance <= 10
    coords = np.argwhere(mask)

    # clicando no botão
    if coords.size > 0:
        y_rel, x_rel = coords[0]
        x_click = left + x_rel
        y_click = top + y_rel
        pyautogui.click(x_click, y_click)
        time.sleep(0.5)
    else:
        print("Cor não encontrada.")
        exit()

# Função principal que roda o jogo até o nível máximo
def main(nivel_max):
    clicarbtn(**regiao_jogo)  # clica no start

    nivel_atual = 1

    while nivel_atual <= nivel_max:
        numeros = detectar_numeros()  # detecta os números na tela
        
        if not numeros:  # se não encontrou números, espera e tenta de novo
            time.sleep(0.3)
            continue

        # Clica em todos os números detectados
        for _, x, y in numeros:
            pyautogui.click(x, y)
        nivel_atual += 1

        # Tenta clicar no continuar para avançar
        clicarbtn(**regiao_jogo)

# Número de níveis que deseja jogar
niveis_desejados = 23  # ajuste conforme necessidade
time.sleep(5)  # pausa antes de iniciar
main(niveis_desejados)