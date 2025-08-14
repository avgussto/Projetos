# AimBot

O AimBot é um bot em Python desenvolvido para automatizar o teste Aim Trainer da plataforma Human Benchmark. Ele captura a tela, identifica os alvos brancos dentro da área do teste e realiza cliques automaticamente, ajudando a passar de nível com precisão e velocidade.

Caso tenha interesse no funcionamento e/ou na lógica por trás do bot, clique [aqui] para ver um vídeo de demonstração que postei no meu LinkedIn :)

## 🚀 Funcionalidades

 - Captura a tela em tempo real na área do Aim Trainer.

- Detecta pixels brancos (alvos) com tolerância de cor configurável.

- Calcula as coordenadas do alvo na tela.

- Executa cliques automaticamente sobre o alvo.

- Loop de execução para passar várias rodadas do teste sem intervenção manual.


## 🛠️ Tecnologias Utilizadas

- Python 3

- mss — captura de tela

- NumPy — manipulação de arrays e cálculos

- PyAutoGUI — automação de mouse

- time — gerenciamento de delays

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/AimBot.git
cd AimBot
```

2. (Opcional) Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```
## ▶️ Como usar

1. Abra o teste Aim Trainer no navegador e deixe a janela pronta.

2. Ajuste no código a região da tela onde os alvos aparecem:
```bash
regiao = {'top':210, 'left':546,'width':1015, 'height':444}
```

3. Ajuste a posição inicial do clique, se necessário:
```bash
pyautogui.click(973, 424)
```

Execute o bot:
```bash
python aimbot.py
```

O bot detectará e clicará automaticamente nos alvos dentro da área definida, passando os níveis do teste.