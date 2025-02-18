from ultralytics import YOLO
import cv2
import pytesseract
import pyttsx3
import datetime
import random
import os
import speech_recognition as sr
import threading
import time

# Configurando o Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Lista de tradução de itens detectados
traducao_itens = {
    'bottle': 'garrafa',
    'mouse': 'mouse',
    'keyboard': 'teclado',
    'tv': 'tv',
    'book': 'livro',
    'person': 'pessoa',
    'couch': 'sofá',
    'tie': 'gravata',
    "remote":"controle remoto",
    "cell phone": "celular"
}

class AssistenteVirtual:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.eventos = []
        self.reconhecedor = cv2.face.EigenFaceRecognizer_create()
        self.reconhecedor.read('classificadoreigen.yml')
        self.detectorFace = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        self.camera = cv2.VideoCapture(0)
        self.nome_usuario = ""
        self.reconhecimento_iniciado = False
        self.recognizer = sr.Recognizer()  # Inicializa o reconhecedor de fala
        self.modelo_yolo = YOLO('yolov5m.pt')  # Modelo YOLOv5 para detecção de objetos
        self.executando = True  # Atributo para controle do loop principal

    def falar(self, texto):
        print(f"Ana: {texto}")  # Print da fala da Ana
        self.engine.say(texto)
        self.engine.runAndWait()

    def capturar_imagem(self):
        """Captura uma imagem da câmera"""
        status, imagem = self.camera.read()
        return imagem

    def controle_comandos(self):
        """Controle de comandos após reconhecimento facial"""
        self.falar("Aguardando comandos.")
        while self.executando:
            comando = self.ouvir_comando().lower()

            if 'sair' in comando:
                self.falar("Até logo!")
                self.executando = False  # Interrompe o loop principal
                break
            elif 'criar evento' in comando:
                self.criar_evento()
            elif 'checar eventos' in comando:
                self.checar_eventos()
            elif 'estação do ano' in comando:
                self.informar_estacao()
            elif 'hora' in comando:
                self.informar_hora()
            elif 'data' in comando:
                self.informar_data()
            elif 'piada' in comando:
                self.contar_piada()
            elif 'fato' in comando:
                self.contar_fato()
            elif 'ler texto' in comando:
                self.reconhecer_texto()
            elif 'quais itens estão na tela' in comando:
                self.detectar_itens_yolo()
            else:
                print("Comando não reconhecido.")

    def ouvir_comando(self):
        # Captura e reconhece a fala do usuário
        with sr.Microphone() as mic:
            self.recognizer.adjust_for_ambient_noise(mic, duration=2)
            print(f"Ana está ouvindo...")
            try:
                audio = self.recognizer.listen(mic, timeout=15)
                texto = self.recognizer.recognize_google(audio, language='pt')
                print(f"Usuário: {texto}")
                return texto
            except sr.UnknownValueError:
                self.falar("Desculpe, não consegui entender o que você disse.")
                return ""
            except sr.RequestError:
                self.falar("Erro de conexão com o serviço de reconhecimento de fala.")
                return ""

    def detectar_itens_yolo(self):
        self.falar("Analisando itens na tela.")
        itens_detectados = set()  # Usamos um set para evitar itens repetidos

        tempo_inicial = time.time()
        while time.time() - tempo_inicial < 5:  # Detecta por 5 segundos
            imagem = self.capturar_imagem()
            resultados = self.modelo_yolo(imagem)

            for resultado in resultados:
                for item in resultado.boxes.data:
                    nome_item = resultado.names[int(item[5])]
                    itens_detectados.add(traducao_itens.get(nome_item, nome_item))

        if itens_detectados:
            lista_itens = ', '.join(itens_detectados)
            self.falar(f"Itens que foram apresentados: {lista_itens}")
        else:
            self.falar("Nenhum item foi detectado na tela.")

    def criar_evento(self):
        resposta = 'positivo'
        while True:
            self.falar('Certo, qual evento você quer cadastrar?')
            evento = self.ouvir_comando()
            if evento:
                self.eventos.append(evento)
                self.falar(f"Evento {evento} cadastrado com sucesso.")

            self.falar('Certo, mais algum evento que deseja cadastrar? Responda positivo para continuarmos')
            resposta = self.ouvir_comando()

            if resposta != 'positivo':
                break

        self.criar_arquivo_eventos()

    def criar_arquivo_eventos(self):
        """Salva os eventos cadastrados em um arquivo"""
        if self.eventos:
            topicos = "\n".join([f"- {evento}" for evento in self.eventos])
            caminho_area_de_trabalho = os.path.join(os.path.expanduser("~"), "Desktop", "eventos.txt")

            with open(caminho_area_de_trabalho, "w", encoding="utf-8") as arquivo:
                arquivo.write(topicos)

            self.falar("Os eventos foram salvos na sua área de trabalho.")
        else:
            self.falar("Nenhum evento para salvar.")

    def checar_eventos(self):
        caminho_area_de_trabalho = os.path.join(os.path.expanduser("~"), "Desktop", "eventos.txt")
        try:
            with open(caminho_area_de_trabalho, "r", encoding="utf-8") as arquivo:
                conteudo = arquivo.read()
                self.falar(f"Aqui estão os eventos da sua agenda:\n{conteudo}")

        except FileNotFoundError:
            self.falar("O arquivo eventos.txt não foi encontrado na sua área de trabalho.")

    def informar_data(self):
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y")
        self.falar(f"Hoje é {data_atual}.")

    def informar_hora(self):
        hora_atual = datetime.datetime.now().strftime("%H:%M")
        self.falar(f"Agora são {hora_atual}.")

    def informar_estacao(self):
        mes_atual = datetime.datetime.now().month
        if mes_atual in [12, 1, 2]:
            estacao = "verão"
        elif mes_atual in [3, 4, 5]:
            estacao = "outono"
        elif mes_atual in [6, 7, 8]:
            estacao = "inverno"
        else:
            estacao = "primavera"
        self.falar(f"A estação atual é {estacao}.")

    def contar_piada(self):
        piadas = [
            "Por que o livro de matemática se suicidou? Porque tinha muitos problemas.",
            "O que é o que é: Feito para andar e não anda? A rua!",
            "Qual é o animal mais antigo? A zebra, porque está em preto e branco."
        ]
        self.falar(random.choice(piadas))

    def contar_fato(self):
        fatos = [
            "Você sabia que o coração humano bate em média 100 mil vezes por dia?",
            "O Monte Everest cresce cerca de 4 milímetros por ano.",
            "A Terra é o único planeta que não tem o nome de um deus."
        ]
        self.falar(random.choice(fatos))

    def reconhecer_texto(self):
        self.falar("Por favor, mostre o texto para a câmera.")
        imagem = self.capturar_imagem()
        texto = pytesseract.image_to_string(imagem, lang='por')
        if texto:
            self.falar(f"O texto que encontrei é: {texto}")
        else:
            self.falar("Não consegui reconhecer nenhum texto.")

    def iniciar_interacao(self):
        """Inicia a interação após reconhecimento facial"""
        self.falar(f"Olá {self.nome_usuario}, o que posso fazer por você?")
        self.controle_comandos()

    def iniciar(self):
        """Inicia o reconhecimento facial e o controle de comandos"""
        while self.executando:
            imagem = self.capturar_imagem()
            imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            facesDetectadas = self.detectorFace.detectMultiScale(imagemCinza, scaleFactor=1.5, minSize=(30, 30))

            for x, y, l, a in facesDetectadas:
                imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (220, 220))
                cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)

                try:
                    nome, confianca = self.reconhecedor.predict(imagemFace)
                    if nome == 1:
                        self.nome_usuario = 'Sergio'

                    cv2.putText(imagem, str(self.nome_usuario), (x, y + 220 - 20), cv2.QT_FONT_NORMAL, 2, (0, 0, 255))

                    if self.nome_usuario == 'Sergio' and not self.reconhecimento_iniciado:
                        self.reconhecimento_iniciado = True
                        threading.Thread(target=self.iniciar_interacao).start()

                except:
                    self.falar("Rosto não reconhecido.")
                    pass

            cv2.imshow("Reconhecimento Facial", imagem)

            if cv2.waitKey(1) == ord('q') or not self.executando:
                break

        self.camera.release()
        cv2.destroyAllWindows()


# Iniciando a assistente virtual
if __name__ == "__main__":
    ana = AssistenteVirtual()
    ana.iniciar()
