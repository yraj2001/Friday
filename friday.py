import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 175)
engine.say('hi sir, I am Friday, here for your assistance')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google (voice)
            command = command.lower()
            print(command)
            if 'friday' in command:
                command = command.replace('friday','')
            else:
                command = '010110'

    except:
        command = '010110'
        pass
    return command



def run_friday():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace("play",'')
        talk('playing' + song + 'sir')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('sir, current time is ' + time)
    elif 'wikipedia' in command:
        person = command.replace('wikipedia','')
        info = wikipedia.summary(person,1)
        talk('sir, I found this in wikipedia ' + info)
    elif 'search' in command:
        search = command.replace('search','')
        talk('sir this is what I found')
        pywhatkit.search(search)
    elif 'tell me a joke' in command :
        talk('ok sir, ' + pyjokes.get_joke())
    elif 'cancel shutdown' in command:
        talk('shutdown cancelled sir')
        pywhatkit.cancel_shutdown()
    elif 'shutdown' in command:
        talk('Sir, shutting the system in 20 seconds')
        pywhatkit.shutdown(20)
    elif ('010110' == command):
        a = 1
    else:
        talk('sorry sir, can you repeat ?')



while True :
    run_friday()
