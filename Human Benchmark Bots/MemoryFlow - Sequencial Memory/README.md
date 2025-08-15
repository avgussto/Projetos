## MemoryFlow

O MemoryFlow automatiza o teste Sequence Memory do Human Benchmark.
Ele detecta visualmente quando cada quadrado acende, grava a sequência correta e depois a reproduz automaticamente clicando nos mesmos quadrados na ordem exibida.

Caso tenha interesse no funcionamento e/ou na lógica por trás do bot, clique aqui para ver um vídeo de demonstração que postei no meu LinkedIn :)

## 🚀 Funcionalidades

- Armazena as coordenadas de cada quadrado

- Checa continuamente por pixels brancos para identificar os quadrados que acenderam.

- Armazena as coordenadas dos quadrados em sequência.

- Clica na mesma sequência que foi apresentada.

## 🛠️ Tecnologias Utilizadas

- Python 3

- PyAutoGUI — automação de teclado

- keyboard — digitação de caracteres especiais

- time — gerenciamento de delays

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Projetos/Human Benchmark Bots/MemoryFlow.git
cd MemoryFlow
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

1. Abra o teste Sequence Memory no navegador e deixe a janela pronta.

2. Ajuste no código as coordenadas da área do grid no teste (se necessário):

```bash
quadrados = [
    (819, 358), (938, 360), (1080, 362),
    (814, 491), (951, 492), (1086, 492),
    (812, 620), (969, 616), (1075, 618)
]
```

3. Execute o bot:
```bash
python memoryflow.py
```