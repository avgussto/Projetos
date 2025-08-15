## SuperChimp

O SuperChimp é um bot em Python desenvolvido para automatizar o teste Chimp Test da plataforma Human Benchmark. Ele detecta os números exibidos na tela e clica automaticamente na sequência correta, avançando de nível sem intervenção manual.

Caso tenha interesse no funcionamento e/ou na lógica por trás do bot, clique aqui para ver um vídeo de demonstração que postei no meu LinkedIn :)

## 🚀 Funcionalidades

- Detecta e clica no botão Start automaticamente.

- Captura a região do jogo em tempo real.

- Identifica os números exibidos na tela usando OCR.

- Ordena os números e clica na sequência correta.
 
- Avança automaticamente até o nível desejado.

## 🛠️ Tecnologias Utilizadas

- Python 3

- OpenCV — processamento de imagens

- NumPy — manipulação de arrays

- mss — captura de tela

- PyAutoGUI — clique automático
 
- pytesseract — OCR

- time — delays

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Projetos/Human Benchmark Bots/SuperChimp.git
cd SuperChimp
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

Windows: [Download aqui](https://tesseract-ocr.github.io/tessdoc/Installation.html)

Linux: sudo apt install tesseract-ocr

Mac: brew install tesseract

5. Depois, ajuste no código o caminho do executável se necessário:
```bash
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## ▶️ Como usar

1. Abra o teste Chimp Test no navegador e ajuste a região do jogo no código se necessário.

2. Execute:
```bash
python superchimp.py
```