from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import mss
import numpy as np
import pyautogui
import time


# Função para iniciar o teste de memória no site Human Benchmark
def start_game():
    time.sleep(3)  # espera a página carregar completamente
    pyautogui.click(x=950, y=580)  # clica no botão 'Start' (coordenadas da tela)
    time.sleep(1)  # espera o jogo iniciar


# Função para capturar frames da região da grade do jogo
def capturar_frames(regiao_grade, duracao=1.0):

    frames = []
    start = time.time()
    with mss.mss() as sct:
        while time.time() - start < duracao:
            # Captura a região da tela como array NumPy (RGB)
            frame = np.array(sct.grab(regiao_grade))[:, :, :3]  # remove canal alpha
            frames.append(frame)
    return frames


# Função para obter as posições centrais dos quadrados da grade
def get_grid_tiles(driver):
    # Pega todos os quadrados pelo atributo style
    tiles_elements = driver.find_elements(By.CSS_SELECTOR, "div[style*='width'][style*='height'][style*='border-radius']")
    grid = []
    ajuste_y = 130  # ajuste vertical para alinhar com a tela real
    for tile in tiles_elements:
        location = tile.location
        size = tile.size
        center_x = int(location["x"] + size["width"] / 2)
        center_y = int(location["y"] + size["height"] / 2 + ajuste_y)
        grid.append((center_x, center_y))

    return grid



# Função para detectar quais quadrados "piscam" nos frames
def detectar_piscadas_por_frames(frames, tiles, regiao_grade, limiar_branco=200):

    piscadas_detectadas = set()

    for frame in frames:
        for (x, y) in tiles:
            # Converte coordenadas absolutas para relativas à região capturada
            rel_x = int(x - regiao_grade["left"])
            rel_y = int(y - regiao_grade["top"])

            # Ignora pixels fora do frame
            if rel_x < 0 or rel_y < 0 or rel_x >= frame.shape[1] or rel_y >= frame.shape[0]:
                continue

            pixel = frame[rel_y, rel_x]  # pega o pixel correspondente
            if np.mean(pixel) > limiar_branco:  # se o pixel é suficientemente claro (branco)
                piscadas_detectadas.add((x, y))

    return list(piscadas_detectadas)


# Função para clicar nos quadrados detectados
def clicar_quadrados(quadrados):
    for (x, y) in quadrados:
        pyautogui.click(x, y)


# Configuração do driver do Chrome
options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://humanbenchmark.com/tests/memory")  # abre o teste
time.sleep(90)
# Inicia o teste
start_game()

# Região da grade do jogo na tela
regiao_grade = {'top': 280,
                'left': 522,
                'width': 899,
                'height': 440}

# Loop principal para jogar até x níveis
for nivel in range(1, 101):

    # Captura frames da região da grade
    frames = capturar_frames(regiao_grade, duracao=1.0)

    # Obtém posições centrais de todos os quadrados da grade
    tiles = get_grid_tiles(driver)

    # Detecta quais quadrados piscam nos frames capturados
    piscadas = detectar_piscadas_por_frames(frames, tiles, regiao_grade)

    if not piscadas:  # se nenhum quadrado piscou, interrompe
        break

    # Clica nos quadrados detectados
    clicar_quadrados(piscadas)

    time.sleep(2)  # espera carregar próximo nível

time.sleep(190)