import pyautogui
import keyboard

pontos = []

def on_key_event(event):
    global pontos

    if event.name == 'q':
        print("Saindo...")
        keyboard.unhook_all()
        exit(0)

    if len(pontos) < 2:
        pos = pyautogui.position()
        pontos.append((pos.x, pos.y))
        print(f"Capturado: {pos}")

        if len(pontos) == 2:
            x1, y1 = pontos[0]
            x2, y2 = pontos[1]
            x = min(x1, x2)
            y = min(y1, y2)
            largura = abs(x2 - x1)
            altura = abs(y2 - y1)

            print(f"\nÁrea capturada: (x={x}, y={y}, largura={largura}, altura={altura})")
            print("Pressione 'q' para sair.")

print("Pressione qualquer tecla para capturar o primeiro ponto (canto da área).")
print("Depois pressione novamente para capturar o segundo ponto (outro canto).")
print("Pressione 'q' para sair.")

keyboard.on_press(on_key_event)
keyboard.wait()
