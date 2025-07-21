import mss
from PIL import Image, ImageFilter, ImageOps
import pyautogui
import pytesseract
import time
import re
import keyboard

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def pegar_texto(top,left,width,height):
    with mss.mss() as sct:
        region = {"top": top, "left": left, "width": width, "height": height} # coordenadas para o print
        screenshot = sct.grab(region) # tirando o print das coordenadas
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb) # carregando a imagem para tratamento
        img = img.convert("L") # deixando a imagem em escala de cinza
        img = ImageOps.autocontrast(img) # adicionando contraste
        img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))
        img.save("debug.png")

    custom_config = r'--oem 3 --psm 3'
    texto = pytesseract.image_to_string(img, config=custom_config)
    texto_limpo = re.sub(r'^[\[|l]+', '', texto)
    texto_corrigido= re.sub(r'(^|\.\s+)\|', r'\1I', texto_limpo)
    texto_final = texto_corrigido[0].upper() + texto_corrigido[1:].strip()


    print(texto_final)
    return texto_final

def preparar_para_digitacao():
    texto= pegar_texto(408, 490, 958, 140)
    texto = texto.replace('\n', ' ').replace('\r', ' ').strip()
    texto = re.sub(r'\s+', ' ', texto)
    texto = texto.encode('ascii', errors='ignore').decode('ascii')
    return texto


def digitar_texto(texto):
    partes = re.split(r'(\?)', texto)

    for parte in partes:
        if parte == '?':
            keyboard.press_and_release('shift+/')
        else:
            pyautogui.write(parte)


time.sleep(3)
texto_final = preparar_para_digitacao()
digitar_texto(texto_final)

