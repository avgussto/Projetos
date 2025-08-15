import pyautogui
import keyboard
import time

# Coordenadas dos quadrados do jogo (de 0 a 8)
quadrados = [
    (819, 358), (938, 360), (1080, 362),
    (814, 491), (951, 492), (1086, 492),
    (812, 620), (969, 616), (1075, 618)
]

# Coordenada do botão "Start" do jogo
botao_iniciar = (968, 540)

# Função para verificar se o quadrado está aceso (iluminado)
def quadrado_aceso(posicao):
    r, g, b = pyautogui.screenshot().getpixel(posicao)
    return r > 200 and g > 200 and b > 200  # considera "aceso" se RGB for alto

# Lista para armazenar a sequência de quadrados acesos
sequencia = []

# Armazena o tempo do último quadrado aceso detectado
tempo_ultimo_aceso = None

# Tempo máximo de espera para considerar que a sequência terminou
limite_espera = 1  # segundos

# Pequena pausa antes de começar
time.sleep(3)

# Clica no botão "Start" para iniciar o jogo
pyautogui.click(*botao_iniciar)

nivel = 0  # contador de níveis completados

# Loop principal do bot
while nivel < 50:
    # Para o bot se a tecla 'q' for pressionada
    if keyboard.is_pressed('q'):
        break

    aceso_nesse_loop = None

    # Verifica cada quadrado para ver se está aceso
    for indice, posicao in enumerate(quadrados):
        if quadrado_aceso(posicao):
            # Adiciona à sequência se for novo ou diferente do último
            if len(sequencia) == 0 or sequencia[-1] != indice:
                sequencia.append(indice)
                aceso_nesse_loop = time.time()
                time.sleep(0.3)  # evita múltiplas detecções seguidas

    # Atualiza o tempo do último quadrado aceso
    if aceso_nesse_loop:
        tempo_ultimo_aceso = aceso_nesse_loop

    # Se passou tempo suficiente sem novo quadrado aceso, digita a sequência
    if sequencia and tempo_ultimo_aceso and (time.time() - tempo_ultimo_aceso) > limite_espera:
        for indice in sequencia:
            if keyboard.is_pressed('q'):
                break
            x, y = quadrados[indice]
            pyautogui.click(x, y)  # clica na posição do quadrado
        sequencia.clear()  # limpa a sequência
        nivel += 1  # incrementa nível
        tempo_ultimo_aceso = None

    time.sleep(0.1)  # pausa pequena para não sobrecarregar CPU

print("Bot finalizado.")  # mensagem quando o bot termina
