import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import webbrowser
import wikipedia
import os
import keyword
from tkinter import *

name = 'Eva'
listener = sr.Recognizer()

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 170)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen(texto):
    try:
        with sr.Microphone() as source:
            print(texto)
            voice = listener.listen(source)
            rec = listener.recognize_google(voice, language='es-ES')
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name,'')
                # print("Usted dijo: " + rec)                                                
    except:
        return 'error'
    return rec

#def basic_functions():
 #   rec = listen('Funciones básicas...')

    
def run():
    #Música y Videos en YT
    
    rec = listen('Esperando ordenes...')
    if 'busca en youtube' in rec:
        music = rec.replace('busca en youtube', '')
        talk('Reproduciendo '+ music)
        pywhatkit.playonyt(music)
                    
    #Hora
    elif 'dime la hora' in rec:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk("Son las " + hora)
                    
    #Fecha
    elif 'que es dia hoy' in rec:
        fecha = datetime.datetime.now().strftime('%d/%m/%Y')
        talk("Hoy es " + fecha) 

    #Buscador 
    elif 'busca en internet' in rec:
        order = rec.replace('busca en internet', '')
        talk('Buscando '+ order)
        pywhatkit.search(order)

    #Chistes
    elif 'dime un chiste' in rec:
        talk(pyjokes.get_joke('es'))

    elif 'hola' in rec:
        talk('Hola, en que puedo ayudarte?')  
        run() 

    elif 'busca en wikipedia' in rec:
        palabra = rec.replace('busca en wikipedia', '')
        talk('Buscando en Wikipedia...'+palabra)
        wikipedia.set_lang('es')
        wiki = wikipedia.summary(palabra,1) 
        resultados='Resultado de '+ palabra + ' segun wikipedia ' + wiki  
        talk(resultados)

    elif 'ejecutar comando' in rec:
        order = rec.replace('ejecuta','')
        talk('Abriendo '+ order)
        app = order+'.exe'
        os.system(app)   
   

    #Redireccionamiento de sitios web
    elif 'abre facebook' in rec:
        case = rec.replace('abre facebook', '')
        talk("abiendo feisbuk " + case)
        webbrowser.open('https://facebook.com')

    elif 'abre whatsapp' in rec:
        case = rec.replace('abre whatsapp', '')
        talk("Abriendo guats ap" + case)
        webbrowser.open('https://web.whatsapp.com/')

    elif 'busca en spotify' in rec:
        case = rec.replace('busca en spotify', '')
        talk("buscando en espotifai " + case)
        webbrowser.open('https://open.spotify.com/search/'+case)

    elif 'error' in rec:
        # talk("No te entendi muy bien, vuelve a intentarlo")
        run()
    elif 'adios' in rec:
        talk("adios")
    #Sin programar
    else:
        talk("No te entendi muy bien, vuelve a intentarlo")
        # run()
#Iniciador
if __name__ == "__main__":
    # run()
    root = Tk()
    root.geometry("150x50")
    root.resizable(0,0)
    root.title("Eva")
    root.configure(bg='#2d2d2d')
    root.iconbitmap('logo.ico')
    # root.call('wm','iconphoto',root._w, PhotoImage(file='logo.ico'))
    boton_iniciar = Button(root, text="Iniciar", command=run, bg="#2d2d2d", fg='#ffffff', font=('Arial', 12),activebackground='#2d2d2d', activeforeground='#ffffff',justify=CENTER,width=150,height=50).pack()
    root.mainloop()
