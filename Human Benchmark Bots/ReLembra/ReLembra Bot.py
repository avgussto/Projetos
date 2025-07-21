import mss
from PIL import Image, ImageFilter, ImageOps
import numpy as np
import pyautogui
import pytesseract
import time

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def clicar_start(top,left,width,height):

    time.sleep(3) # delay para trocar de tela
    with mss.mss() as sct:
        region = {"top": top, "left": left, "width": width, "height": height} # coordenadas para o print
        screenshot = sct.grab(region) # tirando o print das coordenadas
        img = np.array(screenshot)[:, :, :3] # transformando a imagem em array rgb

    target_color_np = np.array((51, 51, 51)) # definindo a cor a ser buscada (cinza escuro)
    distance = np.linalg.norm(img - target_color_np, axis=2) # buscando a cor na array
    mask = distance <= 10 # definindo uma tolerância para as cores para não depender da qualidade do print
    coords = np.argwhere(mask) # salvando as coordenadas da cor

    if coords.size > 0:
        y_rel, x_rel = coords[0] # passando a primeira coordenada para levar o mouse
        x_click = left + x_rel
        y_click = top + y_rel
        pyautogui.click(x_click, y_click) # clicando na cor
    else:
       raise ValueError("Cor de início não encontrada!")


def coleta_palavra(top,left,width,height):

    with mss.mss() as sct:
        region = {"top": top, "left": left, "width": width, "height": height}  # coordenadas para o print
        screenshot = sct.grab(region)  # tirando o print das coordenadas

        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb) # carregando a imagem para tratamento
        img = img.convert("L") # deixando a imagem em escala de cinza
        img = img.point(lambda x: 0 if x < 140 else 255) # binarizando
        img = ImageOps.autocontrast(img) # adicionando contraste
        img = img.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))

    custom_config = r'--oem 3 --psm 8 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto = pytesseract.image_to_string(img, config=custom_config)
    texto = texto.strip().lower()

    return texto

def jogar(coord_seen, coord_new):
    score = 0
    palavras_vistas = set()
    clicar_start(154, 46, 1843, 524)

    while score <= 250:

        palavra = coleta_palavra(385, 766, 413, 80)

        if palavra not in palavras_vistas:
            palavras_vistas.add(palavra)
            pyautogui.click(*coord_new)
            time.sleep(0.05)

        else:
            pyautogui.click(*coord_seen)
            time.sleep(0.05)

        score += 1

jogar((904, 495),(1041, 495))



