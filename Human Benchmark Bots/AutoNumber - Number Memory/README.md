
# AutoNumber

O **AutoNumber** é um bot em Python desenvolvido para automatizar o teste **Number Memory** da plataforma [Human Benchmark](https://humanbenchmark.com/tests/number-memory). Ele captura a tela, reconhece os números exibidos usando OCR e digita automaticamente a sequência, passando para o próximo nível de forma totalmente autônoma.

Caso tenha interesse no funcionamento e/ou a lógica por trás do bot, clique [aqui]() para ver o vídeo de showcase que postei no meu LinkedIn :)


## 🚀 Funcionalidades

- Localiza e clica automaticamente no botão **Start**.
- Captura a área da tela onde o número é exibido.
- Processa a imagem (binarização, contraste, *unsharp mask*) para otimizar a leitura.
- Reconhece os números via **Tesseract OCR**.
- Digita a sequência reconhecida e avança de nível.
- Ajusta dinamicamente o tempo de digitação conforme a dificuldade aumenta.


## 🛠️ Tecnologias Utilizadas

- **Python 3**
- [mss](https://github.com/BoboTiG/python-mss) — captura de tela
- [Pillow](https://pillow.readthedocs.io/en/stable/) — processamento de imagens
- [NumPy](https://numpy.org/) — manipulação de arrays
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) — automação de teclado e mouse
- [pytesseract](https://pypi.org/project/pytesseract/) — OCR
- [re](https://docs.python.org/3/library/re.html) — expressões regulares para limpeza do texto


## 📦 Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Projetos/Human Benchmark Bots/AutoNumber.git
   cd AutoNumber

2. **(Opcional) Crie e ative um ambiente virtual**:
   ```bash
    python -m venv venv
    source venv/bin/activate    # Linux/Mac
    venv\Scripts\activate       # Windows

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt

4. **Instale o Tesseract OCR**
    
- Windows: [Download aqui](https://tesseract-ocr.github.io/tessdoc/Installation.html)

- Linux: sudo apt install tesseract-ocr

- Mac: brew install tesseract

   Depois, atualize no código o caminho para o executável do Tesseract caso seja       diferente:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

## ▶️ Como usar
1. Abra o teste Number Memory no navegador e deixe a janela pronta.

2. Ajuste no código as coordenadas da sua tela para:
- Botão de Start
- Área do OCR (números)

3. Execute:
   ```bash
   python autonumber.py

4. Volte para a janela do teste

5. O bot fará o resto sozinho