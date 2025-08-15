## ReLembra

O ReLembra é um bot em Python desenvolvido para automatizar o teste Verbal Memory da plataforma Human Benchmark.
Ele reconhece a palavra exibida na tela por meio de OCR, armazena mentalmente (em código) as palavras já vistas e clica automaticamente em "SEEN" ou "NEW" conforme necessário, permitindo avançar no teste sem erros.

Caso tenha interesse no funcionamento e/ou na lógica por trás do bot, clique [aqui]() para ver um vídeo de demonstração que postei no meu LinkedIn :)

## 🚀 Funcionalidades

- Localiza e clica automaticamente no botão Start do teste.

- Captura a palavra exibida e a processa com Tesseract OCR.

- Armazena internamente todas as palavras já vistas.

- Decide automaticamente se a palavra é nova ou já apareceu.

- Clica em NEW para palavras inéditas e em SEEN para palavras repetidas.

- Funciona em loop até atingir a pontuação definida.

## 🛠️ Tecnologias Utilizadas

- Python 3

- mss — captura de tela

- Pillow — processamento de imagens

- NumPy — manipulação de arrays

- PyAutoGUI — automação de cliques

- pytesseract — OCR

- time — controle de delays

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Projetos/Human Benchmark Bots/ReLembra.git
cd ReLembra
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

4. Instale o Tesseract OCR:

- Windows: [Download aqui](https://tesseract-ocr.github.io/tessdoc/Installation.html)
- Linux: sudo apt install tesseract-ocr
- Mac: brew install tesseract

5. Depois, ajuste no código o caminho para o executável do Tesseract se necessário:
```bash
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

▶️ Como usar

1. Abra o teste Verbal Memory no navegador e posicione-o na tela.

2. Ajuste no código as coordenadas:
```bash
Botão Start → clicar_start(...)

Área da palavra → coleta_palavra(...)

Botão SEEN → coord_seen

Botão NEW → coord_new
```

3. Execute:
```bash
python relemabra.py
```