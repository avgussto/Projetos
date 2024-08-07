# -*- coding: utf-8 -*-
"""advinhar numero.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iW49qEi3d-BFG8R5IOKudM2ta5NVEV9w
"""

import random as rd
import time

num = rd.randint(1,100)
tentativas = 10

print('Advinhe um número entre 0 a 100')
print('Você tem apenas 10 tentativas, cuidado!')

while tentativas != -1:
  chute = int(input(''))
  tentativas -= 1

  if chute > num:
    print('\nO número é menor')
  elif chute < num:
    print('\nO número é maior')
  else:
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.\n')
    print('''               _   __                                          __
              | | / /__  _______   _  _____ ___  _______ __ __/ /
              | |/ / _ \/ __/ -_) | |/ / -_) _ \/ __/ -_) // /_/
              |___/\___/\__/\__/  |___/\__/_//_/\__/\__/\_,_(_)''')
    break

  tentativas -= 1
  print(f'Tentativas restantes: {tentativas}\n')

  if tentativas == 0:
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.')
    time.sleep(0.5)
    print('.\n')
    print(f'O número era: {num}\n')
    print('''     ▄█    █▄   ▄██████▄   ▄████████    ▄████████         ▄███████▄    ▄████████    ▄████████ ████████▄     ▄████████ ███    █▄
    ███    ███ ███    ███ ███    ███   ███    ███        ███    ███   ███    ███   ███    ███ ███   ▀███   ███    ███ ███    ███
    ███    ███ ███    ███ ███    █▀    ███    █▀         ███    ███   ███    █▀    ███    ███ ███    ███   ███    █▀  ███    ███
    ███    ███ ███    ███ ███         ▄███▄▄▄            ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ ███    ███  ▄███▄▄▄     ███    ███
    ███    ███ ███    ███ ███        ▀▀███▀▀▀          ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ███    ███ ▀▀███▀▀▀     ███    ███
    ███    ███ ███    ███ ███    █▄    ███    █▄         ███          ███    █▄  ▀███████████ ███    ███   ███    █▄  ███    ███
    ███    ███ ███    ███ ███    ███   ███    ███        ███          ███    ███   ███    ███ ███   ▄███   ███    ███ ███    ███
    ▀██████▀   ▀██████▀  ████████▀    ██████████       ▄████▀        ██████████    ███    ███ ████████▀    ██████████ ████████▀
                                                                                   ███    ███                                  ''')
    break