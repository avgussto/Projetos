## Visual Learn

O Visual Learn é um bot em Python desenvolvido para automatizar o teste Visual Memory da plataforma Human Benchmark. Ele captura a grade de quadrados, detecta piscadas (novos quadrados que acendem) e clica automaticamente na sequência correta.

Caso tenha interesse no funcionamento e/ou na lógica por trás do bot, clique [aqui]() para ver um vídeo de demonstração que postei no meu LinkedIn :)

## 🚀 Funcionalidades

- Abre automaticamente o teste no navegador com Selenium.

- Captura frames da grade de quadrados.

- Detecta piscadas nos quadrados com base no brilho.

- Clica na sequência correta de quadrados.

- Avança automaticamente pelos níveis.

## 🛠️ Tecnologias Utilizadas

- Python 3

- Selenium — automação do navegador

- mss — captura de tela

- NumPy — processamento de arrays

- PyAutoGUI — clique automático

- time — delays

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/VisualLearn.git
cd VisualLearn
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


4. [Baixe o ChromeDriver](https://sites.google.com/chromium.org/driver/getting-started) compatível com sua versão do Chrome.

5. Coloque o executável no PATH ou na mesma pasta do script.

## ▶️ Como usar

1. Abra o script **visual_learn.py.**

2. Ajuste, se necessário, as coordenadas da região da grade.

3. Execute:
```bash
python visual_learn.py
```