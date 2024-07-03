# -*- coding: utf-8 -*-
"""gerador de senha.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SUbpqP-bSS3crV_hFl04m4YiTo1hIAUK
"""

import random as rd

alfa = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
special = '!@#$%^&*_+'

opcoes = [alfa,num,special]
tamanho = int(input('Digite o tamanho da senha: '))
senha = ''
for i in range(tamanho):
  n = rd.randint(0,2)
  escolha = opcoes[n]
  senha += rd.choice(escolha)

with open ('senha.txt','w') as f:
  f.write(senha)