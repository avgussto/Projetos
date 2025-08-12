import cv2
import numpy as np
import pytesseract
import pyautogui
import time
import mss

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

REGIAO_JOGO = {
    "top": 200,
    "left": 500,
    "width": 900,
    "height": 600
}

def detectar_numeros():
    with mss.mss() as sct:
        img = np.array(sct.grab(REGIAO_JOGO))

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 15, 10
    )

    contornos, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    numeros = []

    for cnt in contornos:
        x, y, w, h = cv2.boundingRect(cnt)

        if 20 < w < 150 and 20 < h < 150:
            roi = gray[y:y+h, x:x+w]

            texto = pytesseract.image_to_string(
                roi, config="--psm 10 -c tessedit_char_whitelist=0123456789"
            )
            numero = ''.join(filter(str.isdigit, texto))

            if numero.isdigit():
                abs_x = REGIAO_JOGO["left"] + x + w // 2
                abs_y = REGIAO_JOGO["top"] + y + h // 2
                numeros.append((int(numero), abs_x, abs_y))

    return sorted(numeros)

def clicarbtn(top, left, width, height):
    print('Iniciando o código.')
    with mss.mss() as sct:
        region= {"top": top, "left": left, "width": width, "height": height}
        screenshot1 = sct.grab(region)
        img1 = np.array(screenshot1)[:, :, :3]

    target_color_np = np.array((51, 51, 51))  # cor cinza-escuro do botão start
    distance = np.linalg.norm(img1 - target_color_np, axis=2)
    mask = distance <= 10
    coords = np.argwhere(mask)

    if coords.size > 0:
        y_rel, x_rel = coords[0]
        x_click = left + x_rel
        y_click = top + y_rel
        print(f"Cor encontrada! Clicando em ({x_click}, {y_click})")
        pyautogui.click(x_click, y_click)
        time.sleep(0.5)
    else:
        print("Cor não encontrada.")
        exit()

def main(nivel_max):
    # Ajuste a região do botão start conforme seu monitor
    clicarbtn(**REGIAO_JOGO)

    nivel_atual = 1

    while nivel_atual <= nivel_max:
        numeros = detectar_numeros()

        if not numeros:
            print("Nenhum número detectado, aguardando...")
            time.sleep(0.3)
            continue

        print(f"Nível {nivel_atual} - Números detectados: {[n[0] for n in numeros]}")

        for _, x, y in numeros:
            pyautogui.click(x, y)

        nivel_atual += 1

        # Tenta clicar no continuar, se não encontrar espera um pouco e tenta de novo
        clicarbtn(**REGIAO_JOGO)

    print(f"Fim do teste! Nível máximo {nivel_max} atingido.")

if __name__ == "__main__":
    NIVEIS_DESEJADOS = 5  # Mude para o nível que quiser parar
    time.sleep(5)
    main(NIVEIS_DESEJADOS)
