import mss
from PIL import Image
import pyautogui
import keyboard
import pytesseract
import time
import re

# Caminho do executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def pegar_texto(top, left, width, height):
    # Captura a região da tela nas coordenadas passadas
    with mss.mss() as sct:
        region = {"top": top, "left": left, "width": width, "height": height}
        screenshot = sct.grab(region)

    # Converte o print para imagem PIL
    img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)

    # Salva imagem para debug
    img.save("debug.png")

    # Configuração e funcionamento do OCR
    custom_config = r'--oem 3 --psm 3'
    ocr_bruto = pytesseract.image_to_string(img, config=custom_config)

    # Limpa caracteres estranhos no início
    ocr_limpo = re.sub(r'^[\[|l]+', '', ocr_bruto)

    # Corrige alguns erros comuns do OCR
    ocr_corrigido = re.sub(r'(^|\.\s+)\|', r'\1I', ocr_limpo)

    # Ajusta a primeira letra para maiúscula e remove espaços extras
    ocr_final = ocr_corrigido[0].upper() + ocr_corrigido[1:].strip()

    print(ocr_final)
    return ocr_final


# noinspection PyShadowingNames
def preparar_para_digitacao():
    # Captura o texto da tela
    texto = pegar_texto(370, 490, 958, 150)

    # Remove quebras de linha e espaços múltiplos
    texto = texto.replace('\n', ' ').replace('\r', ' ').strip()
    texto = re.sub(r'\s+', ' ', texto)

    # Remove caracteres não-ASCII
    texto = texto.encode('ascii', errors='ignore').decode('ascii')

    return texto


# noinspection PyShadowingNames
def digitar_texto(texto):
    # Divide o texto preservando interrogações
    partes = re.split(r'(\?)', texto)

    for parte in partes:
        if parte == '?':
            # Digita "?" com combinação de teclas
            keyboard.press_and_release('shift+/')
        else:
            # Digita o restante normalmente
            pyautogui.write(parte)


# Espera 3 segundos antes de começar
time.sleep(3)

# Captura, prepara e digita o texto
texto = preparar_para_digitacao()
digitar_texto(texto)