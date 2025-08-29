import mss 
import time
import numpy as np
import cv2

time.sleep(3)

regiao_jogo = {'top': 260,
                    'left': 700,
                    'width': 500,
                    'height': 410}

with mss.mss() as sct:
    img = sct.grab(regiao_jogo)
    mss.tools.to_png(img.rgb, img.size, output="debug.png")
