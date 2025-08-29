import mss
from PIL import Image
import numpy as np
import pyautogui
import pytesseract
import time

# Caminho do executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Função para clicar no botão "Start" do jogo
def clicar_start(top, left, width, height):
    time.sleep(3)  # pequena pausa para trocar de tela/janela
    with mss.mss() as sct:
        # Define a região da tela para capturar
        region = {"top": top, "left": left, "width": width, "height": height}
        screenshot = sct.grab(region)
        # Converte para array NumPy RGB
        img = np.array(screenshot)[:, :, :3]

    # Cor alvo (cinza-escuro) que representa o botão start
    target_color_np = np.array((51, 51, 51))
    # Calcula a "distância" de cada píxel até a cor alvo
    distance = np.linalg.norm(img - target_color_np, axis=2)
    # Máscara de pixels próximos da cor alvo (tolerância 10)
    mask = distance <= 10
    coords = np.argwhere(mask)  # pega coordenadas desses píxeis

    if coords.size > 0:
        y_rel, x_rel = coords[0]  # pega a primeira coordenada encontrada
        x_click = left + x_rel
        y_click = top + y_rel
        pyautogui.click(x_click, y_click)  # clica na cor encontrada
    else:
        raise ValueError("Cor de início não encontrada!")  # erro se não encontrar

# Função para capturar a palavra da tela usando OCR
def coleta_palavra(top, left, width, height):
    with mss.mss() as sct:
        region = {"top": top, "left": left, "width": width, "height": height}
        screenshot = sct.grab(region)
        img = Image.frombytes("RGB", screenshot.size, screenshot.rgb)  # converte para imagem PIL

    # Configuração do Tesseract: só letras, página com uma linha
    custom_config = r'--oem 3 --psm 8 -c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    texto = pytesseract.image_to_string(img, config=custom_config)
    texto = texto.strip().lower()  # remove espaços e coloca em minúsculas

    return texto

# Função principal para jogar o jogo de palavras
def jogar(coord_seen, coord_new): 
    score = 0
    palavras_vistas = set()  # conjunto para armazenar palavras já vistas
    clicar_start(154, 46, 1843, 524)  # inicia o jogo

    while score <= 250:  # repete até atingir a pontuação

        palavra = coleta_palavra(385, 766, 413, 80)  # captura a palavra da tela

        if palavra not in palavras_vistas:  # se a palavra é nova
            palavras_vistas.add(palavra)
            pyautogui.click(*coord_new)  # clica no botão "novo"
            time.sleep(0.05)
        else:  # se já viu a palavra
            pyautogui.click(*coord_seen)  # clica no botão "visto"
            time.sleep(0.05)

        score += 1  # incrementa a pontuação

# Chama a função para jogar passando coordenadas dos botões
jogar((904, 495), (1041, 495))
