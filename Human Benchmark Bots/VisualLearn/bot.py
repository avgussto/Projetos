from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import mss
import numpy as np
import pyautogui
import time

def start_game(driver):
    driver.get("https://humanbenchmark.com/tests/memory")
    time.sleep(3)
    pyautogui.click(x=950, y=580)
    print("[INFO] Jogo iniciado.")
    time.sleep(1)

def capturar_frames(regiao_grade, duracao=1.0):
    frames = []
    start = time.time()
    with mss.mss() as sct:
        while time.time() - start < duracao:
            frame = np.array(sct.grab(regiao_grade))[:, :, :3]  # remove alpha
            frames.append(frame)
    print(f"[INFO] Capturados {len(frames)} frames.")

    return frames

def get_grid_tiles(driver):
    tiles_elements = driver.find_elements(By.CSS_SELECTOR, ".css-lxtdud.eut2yre1")
    grid = []
    ajuste_y = 130
    for tile in tiles_elements:
        location = tile.location
        size = tile.size
        center_x = int(location["x"] + size["width"] / 2)
        center_y = int(location["y"] + size["height"] / 2 + ajuste_y)
        grid.append((center_x, center_y))
    print(f"[INFO] {len(grid)} quadrados detectados.")
    return grid

def detectar_piscadas_por_frames(frames, tiles, regiao_grade, limiar_branco=200):
    piscadas_detectadas = set()

    for frame in frames:
        for (x, y) in tiles:
            rel_x = int(x - regiao_grade["left"])
            rel_y = int(y - regiao_grade["top"])

            if rel_x < 0 or rel_y < 0 or rel_x >= frame.shape[1] or rel_y >= frame.shape[0]:
                continue

            pixel = frame[rel_y, rel_x]
            if np.mean(pixel) > limiar_branco:
                piscadas_detectadas.add((x, y))

    print(f"[INFO] Quadrados detectados após análise: {len(piscadas_detectadas)}")
    return list(piscadas_detectadas)

def clicar_quadrados(quadrados):
    print("[INFO] Clicando nos quadrados detectados...")
    for (x, y) in quadrados:
        pyautogui.click(x, y)

if __name__ == "__main__":
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    start_game(driver)

    regiao_grade = {'top': 280,
                    'left': 522,
                    'width': 899,
                    'height': 440}

    for nivel in range(1,101):
        print(f"\n[INFO] Nível {nivel} iniciado")

        frames = capturar_frames(regiao_grade, duracao=1.0)

        tiles = get_grid_tiles(driver)

        piscadas = detectar_piscadas_por_frames(frames, tiles, regiao_grade)

        if not piscadas:
            print("[WARN] Nenhuma piscada detectada. Encerrando loop.")
            break

        clicar_quadrados(piscadas)

        print(f"[INFO] Nível {nivel} concluído.")
        time.sleep(2)  # tempo para próximo nível carregar

    print("\n[FIM] Loop de níveis finalizado.")