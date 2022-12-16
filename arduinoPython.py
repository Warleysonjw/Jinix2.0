import serial
import threading
import time
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
contar = 0;
for vozes in voices: # Lista de vozes
    print(contar, vozes.name)
    contar+=1

voz = 0
engine.setProperty('voice', voices[voz].id)

r = sr.Recognizer()

mic = sr.Microphone()

conectado = False
porta = 'COM5' # Linux ou mac em geral ->  '/dev/ttyS0
velocidadeBaud = 115200

mensagensRecebidas = 1;
desligarArduinoThread = False

falarTexto = False;
textoRecebido = ""

try:
    SerialArduino = serial.Serial(porta,velocidadeBaud, timeout = 0.2)
except:
    print("Verificar porta serial ou religar arduino")

def handle_data(data):
    global mensagensRecebidas, engine, falarTexto, textoRecebido
    print("Recebi " + str(mensagensRecebidas) + ": " + data)
    
    mensagensRecebidas += 1
    textoRecebido = data
    falarTexto = True

def read_from_port(ser):
    global conectado, desligarArduinoThread

    while not conectado:
        conectado = True

        while True:
            reading = ser.readline().decode()
            if reading != "":
                handle_data(reading)
            if desligarArduinoThread:
                print("Desligando Arduino")
                break

lerSerialThread = threading.Thread(target=read_from_port, args=(SerialArduino,))
lerSerialThread.start()

print("Preparando Arduino")
time.sleep(2)
print("Arduino Pronto")

while (True):
    if falarTexto:
        engine.say(textoRecebido)
        engine.runAndWait()

        falarTexto = False
        #time.sleep(3)
    try:
        with mic as fonte:
            r.adjust_for_ambient_noise(fonte)
            print("Fale alguma coisa")
            audio = r.listen(fonte)
            print("Enviando para reconhecimento")
        try:
            text = r.recognize_google(audio, language= "pt-BR")
            print("Você disse: {}".format(text))
            if text == "ligar" or text == "desligar":
                try:
                    pass
                except:
                    print("sem socket")               
            SerialArduino.write((text + '\n').encode())
            print("Dado enviado")
            if(text == "desativar"):
                print("Saindo")

                desativando = "Dinix desativando."

                engine.say(desativando)
                engine.runAndWait()

                engine.stop()
                desligarArduinoThread = True
                SerialArduino.close()
                lerSerialThread.join()
                break
        except:
            print("Não entendi o que você disse\n")
        
        time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        print("Apertou Ctrl+C")
        engine.stop()
        desligarArduinoThread = True
        SerialArduino.close()
        lerSerialThread.join()
        break
    