import pyautogui
import keyboard
import time

# Coordenadas dos quadrados (índices de 0 a 8)
quadrados = [
    (819, 358), (938, 360), (1080, 362),
    (814, 491), (951, 492), (1086, 492),
    (812, 620), (969, 616), (1075, 618)
]

# Coordenada do botão "Start"
botao_iniciar = (968, 540)

# Verifica se o quadrado está aceso (iluminado)
def quadrado_aceso(posicao):
    r, g, b = pyautogui.screenshot().getpixel(posicao)
    return r > 200 and g > 200 and b > 200

sequencia = []
tempo_ultimo_aceso = None
limite_espera = 1  # segundos para considerar que a sequência terminou

time.sleep(3)
pyautogui.click(*botao_iniciar)

while True:
    if keyboard.is_pressed('q'):
        break

    aceso_nesse_loop = None
    for indice, posicao in enumerate(quadrados):
        if quadrado_aceso(posicao):
            if len(sequencia) == 0 or sequencia[-1] != indice:
                sequencia.append(indice)
                aceso_nesse_loop = time.time()
                time.sleep(0.3)  # evita múltiplas detecções seguidas
    if aceso_nesse_loop:
        tempo_ultimo_aceso = aceso_nesse_loop

    if sequencia and tempo_ultimo_aceso and (time.time() - tempo_ultimo_aceso) > limite_espera:
        for indice in sequencia:
            if keyboard.is_pressed('q'):
                break
            x, y = quadrados[indice]
            pyautogui.click(x, y)
        sequencia.clear()
        tempo_ultimo_aceso = None
    time.sleep(0.1)

print("Bot finalizado.")
