# 🧠 Human Benchmark Bots

Este repositório contém bots desenvolvidos em Python para automatizar testes do Human Benchmark.  
O objetivo é explorar automação, visão computacional e processamento de imagens aplicados em mini-jogos de reflexo e memória.

Todos os bots receberam vídeos de demonstração no meu [LinkedIn](https://www.linkedin.com/in/sergio-augusto-soares), se estiver interessado em ver o funcionamento sem precisar rodar nada, so entrar lá :)

#### ⚠️ Aviso

Esses scripts são apenas para **fins educacionais** e estudo de automação/visão computacional.
Não use para trapacear em competições ou rankings públicos.

## 📋 Bots disponíveis

### ⚡ Relampabô — Reaction Time Test
Bot feito para o teste Reaction Time, detecta automaticamente quando a tela fica verde e clica o mais rápido possível.

**Bibliotecas usadas:** `pyautogui`, `time`

**Funcionamento:**
- Aguarda a tela ficar verde.
- Clica instantaneamente.
- Repete por 5 tentativas.


### 📝 ReLembra — Verbal Memory Test
Bot feito para o teste Verbal Memory, usando OCR para identificar as palavras exibidas e decidir se são novas ou já vistas.

**Bibliotecas usadas:** `mss`, `Pillow`, `pytesseract`, `numpy`, `pyautogui`, `time`

**Funcionamento:**
- Detecta e clica no botão "Start".
- Usa OCR para ler a palavra exibida.
- Mantém um histórico das palavras vistas.
- Clica em "SEEN" se já tiver aparecido, ou "NEW" se for nova.


### 🐵 SuperChimp — Chimp Test
Bot feito para o teste Chimp Test, detectando números na tela e clicando na ordem correta.

**Bibliotecas usadas:** `opencv`, `numpy`, `pytesseract`, `mss`, `pyautogui`, `time`

**Funcionamento:**
- Clica no botão "Start".
- Detecta as posições e valores dos números.
- Ordena e clica na sequência correta.
- Avança automaticamente até o nível desejado.



### 🔢 AutoNumber — Number Memory
Bot feito para o teste Number Memory, reconhecendo os números exibidos na tela e digitando automaticamente a sequência.

**Bibliotecas usadas:** `mss`, `Pillow`, `numpy`, `pyautogui`, `pytesseract`, `re`

**Funcionamento:**
- Localiza e clica no botão "Start".
- Captura a área do número e processa com OCR.
- Digita a sequência reconhecida.
- Ajusta dinamicamente o tempo de digitação conforme aumenta a dificuldade.


### 🎯 AimBot — Aim Trainer
Bot feito para o teste Aim Trainer, detectando alvos brancos na tela e clicando automaticamente.

**Bibliotecas usadas:** `mss`, `numpy`, `pyautogui`, `time`

**Funcionamento:**
- Captura a tela em tempo real.
- Detecta pixels brancos representando os alvos.
- Clica nos alvos automaticamente.


### ⌨️ TypeX — Typing Test
Bot feito para o teste Typing Test, lendo a frase exibida na tela e digitando automaticamente.

**Bibliotecas usadas:** `mss`, `Pillow`, `pyautogui`, `keyboard`, `pytesseract`, `re`, `time`

**Funcionamento:**
- Captura a frase exibida.
- Processa o texto para correção de caracteres.
- Digita automaticamente a frase, preservando pontuação.


### 🔳 Sequence Memory Bot — Sequence Memory Test
Bot feito para o teste Sequence Memory, identificando quadrados que acendem e reproduzindo a sequência correta.

**Bibliotecas usadas:** `pyautogui`, `keyboard`, `time`

**Funcionamento:**
- Detecta visualmente quais quadrados acendem.
- Armazena a sequência exibida.
- Reproduz clicando nos quadrados na ordem correta.

### 👀 Visual Learn — Visual Memory Test

Bot feito para o teste Visual Memory, detectando quais quadrados piscam na grade e clicando na sequência correta.

**Bibliotecas usadas:** selenium, mss, numpy, pyautogui, time

**Funcionamento:**

- Abre o teste no navegador automaticamente.
- Captura frames da região da grade.
- Detecta piscadas nos quadrados usando análise de brilho.
- Clica nos quadrados que piscam na sequência correta.
- Repete por múltiplos níveis, avançando automaticamente.

## ⚙️ Requisitos

- Python 3.8+  
- Tesseract OCR instalado (para bots que usam OCR)
- Chromium WebDriver (para o bot que usa o selenium)

