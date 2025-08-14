import mss
import numpy as np
import pyautogui
import time

regiao = {'top':210, 'left':546,'width':1015, 'height':444}
time.sleep(3)
pyautogui.click(973, 424)

for i in range(31):
    with mss.mss() as sct:
        screenshot = np.array(sct.grab(regiao))[:,:,:3]

        target_color_np = np.array((255, 255, 255))
        distance = np.linalg.norm(screenshot - target_color_np, axis=2)
        mask = distance <= 10
        cords = np.argwhere(mask)
        y_rel, x_rel = cords[0]
        x_click = regiao['left'] + x_rel
        y_click = regiao['top'] + y_rel
        pyautogui.click(x_click, y_click)