import pyttsx3  
import datetime  
import speech_recognition as sr  
import pyautogui as pa  
import time  

# Inicializa o TTS (Texto para Fala)
texto_fala = pyttsx3.init()
texto_fala.setProperty("rate", 195)  # Velocidade da fala
voices = texto_fala.getProperty('voices')
texto_fala.setProperty('voice', voices[0].id)  # Definir voz (0 = Masculino, 1 = Feminino)

def falar(mensagem):
    texto_fala.say(mensagem)
    texto_fala.runAndWait()

def escutar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando sua fala...")
        r.pause_threshold = 1  
        try:
            audio = r.listen(source)  
            comando = r.recognize_google(audio, language='pt-BR').lower()  
            print(f"Você disse: {comando}")
            return comando
        except sr.RequestError:
            falar("Erro na conexão. Tente novamente mais tarde.")
            quit()
            return None

def abrir(programa):
    pa.press('win')
    time.sleep(1)
    pa.write(programa)
    pa.press('enter')
    time.sleep(1)
    falar(f"Pronto! {programa} aberto")

def obter_hora():
    hora = datetime.datetime.now().strftime("%H:%M")
    falar(f"Agora são {hora}.")
    print(f"Horas: {hora}")

def obter_data():
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho",
             "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    agora = datetime.datetime.now()
    falar(f"Hoje é {agora.day} de {meses[agora.month - 1]} de {agora.year}.")
    print(f"Data de hoje: {agora.day}/{meses[agora.month - 1]}/{agora.year}")

def saudacao():
    hora = datetime.datetime.now().hour
    if hora < 12:
        mensagem = "Bom dia! O que posso fazer?"
    elif hora < 18:
        mensagem = "Boa tarde! O que posso fazer?"
    else:
        mensagem = "Boa noite! O que posso fazer?"
    falar(mensagem)

# Execução do programa
if __name__ == "__main__":
    saudacao()
    while True:
        comando = escutar()
        if comando:
            if "abrir" in comando:
                if "spotify" in comando:
                    abrir('spotify')
                    continue
                elif "discord" in comando:
                    abrir('discord')
                    continue
                elif "valorant" in comando:
                    abrir('valorant')
                    continue
                else:
                    falar("Não consigo abrir esse programa")
            elif "horas" in comando:
                obter_hora()
                continue
            elif "data" in comando:
                obter_data()
                continue
            elif "encerrar" in comando:
                falar("Espero ter ajudado")
                print("Encerrando...")
                quit()
            else:
                falar("Não entendi o comando")
                print("Não entendi o comando")
