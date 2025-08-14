## TypeX

O TypeX é um bot em Python desenvolvido para automatizar o teste Typing Test da plataforma Human Benchmark. Ele captura a frase exibida na tela, processa o texto usando OCR e digita automaticamente, permitindo praticar e passar de nível de forma rápida e precisa.

Caso tenha interesse no funcionamento e/ou na lógica por trás do bot, clique aqui para ver um vídeo de demonstração que postei no meu LinkedIn :)

## 🚀 Funcionalidades

- Captura a área da tela onde o texto do teste aparece.

- Processa a imagem para melhorar a leitura pelo OCR.

- Reconhece o texto exibido usando Tesseract OCR.

- Corrige erros comuns do OCR e limpa caracteres estranhos.

- Digita automaticamente o texto, preservando pontuações como interrogações.

- Remove espaços extras e caracteres não-ASCII para maior precisão.

## 🛠️ Tecnologias Utilizadas

- Python 3

- mss — captura de tela

- Pillow — processamento de imagens
 
- PyAutoGUI — automação de teclado

- keyboard — digitação de caracteres especiais
 
- pytesseract — OCR

- re — expressões regulares

- time — gerenciamento de delays

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/TypeX.git
cd TypeX
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

4. Instale o Tesseract OCR

- Windows: [Download aqui](https://tesseract-ocr.github.io/tessdoc/Installation.html)

- Linux: sudo apt install tesseract-ocr

- Mac: brew install tesseract

Depois, atualize no código o caminho para o executável do Tesseract caso seja diferente:
```bash
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## ▶️ Como usar

1. Abra o teste Typing Test no navegador e deixe a janela pronta.

2. Ajuste no código as coordenadas da área do texto do teste:

```bash
texto = pegar_texto(370, 490, 958, 150)
```

3. Execute o bot:
```bash
python typex.py
```

O bot capturará, processará e digitará automaticamente o texto exibido no teste.