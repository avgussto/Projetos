import mss
from PIL import Image, ImageFilter, ImageOps
import numpy as np
import pyautogui
import pytesseract
import time
import re

# função para clicar no botão start
def clicar_start(top,left,width,height):
    print('Iniciando o código.')
    time.sleep(5) # delay para trocar de tela
    with mss.mss() as sct:
        region1 = {"top": top, "left": left, "width": width, "height": height} # coordenadas para o print
        screenshot1 = sct.grab(region1) # tirando o print das coordenadas
        img1 = np.array(screenshot1)[:, :, :3] # transformando a imagem em array rgb

    target_color_np = np.array((51, 51, 51)) # definindo a cor a ser buscada (cinza escuro)
    distance = np.linalg.norm(img1 - target_color_np, axis=2) # buscando a cor na array
    mask = distance <= 10 # definindo uma tolerância para as cores para não depender da qualidade do print
    cords = np.argwhere(mask) # salvando as coordenadas da cor

    if cords.size > 0:
        y_rel, x_rel = cords[0] # passando a primeira coordenada para levar o mouse
        x_click = left + x_rel
        y_click = top + y_rel
        print(f"Cor encontrada! Clicando em ({x_click}, {y_click})")
        pyautogui.click(x_click, y_click) # clicando na cor
    else:
        print("Cor não encontrada.")
        exit() # encerrando o código caso a cor não seja encontrada

# função para coletar os números
def coletar_numero(ocr_top,ocr_left,ocr_width,ocr_height):
    time.sleep(0.5) # delay para garantir funcionamento
    with mss.mss() as sct:
        ocr_region = {"top": ocr_top, "left": ocr_left, "width": ocr_width, "height": ocr_height}
        screenshot2 = sct.grab(ocr_region)
        img2 = Image.frombytes("RGB", screenshot2.size, screenshot2.rgb) # carregando a imagem para tratamento

        img2 = img2.convert("L") # deixando a imagem em escala de cinza
        img2 = img2.point(lambda x: 0 if x < 140 else 255) # binarizando
        img2 = img2.resize((img2.width * 2, img2.height * 2), Image.Resampling.LANCZOS) # dando zoom com resize
        img2 = ImageOps.autocontrast(img2) # adicionando contraste
        img2 = img2.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3)) # colocando um filtro para deixar os números mais claros
        img2.save("ocr_debug.png") # salvando a imagem para debugar

    # Melhor psm + limpeza com regex
    ocr = pytesseract.image_to_string(img2, config='--psm 6 outputbase digits') # transcrevendo os números da imagem
    ocr_limpo = ocr.replace("\n", "").replace(" ", "").strip() # removendo espaços e quebra de linhas
    ocr_final = re.sub(r'\D', '', ocr_limpo) # garantindo que só tenham números na string


    print('\n\nTexto extraído:')
    print(texto)
    return texto # retornando a string com os números

# função para digitar o número
def digitar_numero(texto):
    global tempo # acessando a função de tempo
    time.sleep(tempo) # delay para dar tempod e digitar
    pyautogui.write(texto, interval=0.03) # escrevendo
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("enter") # dois enters para ir pro próximo level
    print("\nTexto digitado com sucesso!")


ciclo = 0 # contagem de níveis ou ciclos
continua = True # condição para parar o loop
tempo = 3 # tempo para escrever

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# chamando a função do start e passando as coordenadas
clicar_start(154,46,1843,524)

# começando o loop
while continua:

    # coletando os números
    texto = coletar_numero(140,90,1696,500)

    # digitando os números
    digitar_numero(texto)

    # aumentando o tempo para dar tempo de digitar sem demorar demais
    tempo += 0.87

    # aumentado o ciclo
    ciclo += 1

    # cláusula para encerrar o loop
    if ciclo > 40:
        continua = False