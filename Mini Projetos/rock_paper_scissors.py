# -*- coding: utf-8 -*-
"""rock paper scissors.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17BPPgXdFvcoFnpsdQj5KdyXBI-etqnCR
"""

import random as rnd

opcoes = ['pedra', 'papel', 'tesoura']
regras = {
    'pedra': 'tesoura',
    'papel': 'pedra',
    'tesoura': 'papel'
}

escolha = rnd.choice(opcoes)

escolha_jogador = str(input('Pedra, papel ou tesoura?\n')).lower()

if escolha_jogador == escolha:
    resultado = 'empate :L'
elif regras[escolha_jogador] == escolha:
    resultado = 'você venceu :)'
else:
    resultado = 'você perdeu :('

print(f'\nVocê escolheu {escolha_jogador} e o computador escolheu {escolha}, {resultado}!')