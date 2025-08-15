## Relampabô

O Relampabô é um bot em Python desenvolvido para automatizar o teste Reaction Time da plataforma Human Benchmark. Ele monitora constantemente a tela e, assim que detecta a cor verde de início do teste, realiza cliques automáticos para registrar o tempo de reação — tudo de forma rápida e precisa.

Caso tenha interesse no funcionamento e/ou na lógica por trás do bot, clique [aqui]() para ver um vídeo de demonstração que postei no meu LinkedIn :)

## 🚀 Funcionalidades

* Detecta automaticamente quando o teste muda para a cor verde.

* Executa cliques imediatos para registrar o tempo de reação.

* Permite definir quantas tentativas serão realizadas.

* Simples, rápido e eficiente para automação do teste.

## 🛠️ Tecnologias Utilizadas

- Python 3

- PyAutoGUI — captura de pixel da tela e automação de cliques

- time — controle de delays

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Projetos/HumanBenchmark Bots/Relampabo.git
cd Relampabo
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

▶️ Como usar

1. Abra o teste Reaction Time no navegador e posicione-o na tela.

2. Ajuste no código as coordenadas do botão de clique (ponto de captura da cor verde):
```bash
posicao = (971, 555)
```

3. Execute o bot:
```bash
python relampabo.py
```