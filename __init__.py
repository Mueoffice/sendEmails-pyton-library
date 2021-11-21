import smtplib as smtp
import pyttsx3 as pt
import speech_recognition as sr

def handMail(from_, pass_, to_, content):
    if(type(from_ == str) and type(pass_ == str) and type(to_ == str) and type(content == str)):
        server = smtp.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        # Enable low security in gmail
        server.login(from_, pass_)
        server.sendmail(to_, content)
        server.close()
    else:
        raise ValueError('All the parameters must be a string')

#voiceMail or intelligentMail

#Note: VoiceMail requires Microphone input.

engine = pt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty("rate", 142)
def takeMessage():
    #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
            print("Listening...\n")
            r.pause_threshold = 3
            audio = r.listen(source)

    try:
            print("Recognizing...\n")
            msg = r.recognize_google(audio, language='en-in')
            print(f"Message: {msg}\n")

    except Exception as e:
            print("Something! went wrong...\n")
            return "None"
    return msg

def speak(audio):
    engine.say(audio)
    engine.setProperty("rate", 144)
    engine.runAndWait()

def intelligentMail(from_, to_, pass_):
    if(type(from_ == str) and type(to_ == str) and type(pass_ == str)):
        speak("speak your content.")
        content = takeMessage()
        server = smtp.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(from_, pass_)
        server.sendmail(to_, content)
        server.close()
    else:
        raise ValueError("pass_ param must be a string.")

