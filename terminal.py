import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning!")
    elif hour >= 12 and hour < 17:
        speak("good afternoon")
    elif hour >= 17 and hour < 20:
        speak("good evening")
    else:
        speak('good night') 

    speak("i am terminator version 0.1 sir. please tell me how may i help you")


def takecommand():      # input by user
  r = sr.Recognizer()
  with sr.Microphone() as source:
    print("listining.....")
    r.pause_threshold = 1
    audio = r.listen(source)
  try:
    print("recognizing........")
    query = r.recognize_google(audio, language='en-in')
    print(f"user said: {query}\n")
  except Exception as e:
    # print(e)
    print("say that again please....")
    return "none"
  return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('test123information.technology@gmail.com', *********)        //////put u r pass 
    server.sendmail('test123information.technology@gmail.com', to, content)
    server.close()

if __name__== "__main__":
    # speak("good morning jay")
    wishme()
    while True:
        query = takecommand().lower()

    if 'wikipedia' in query:
        speak('searching wikipedia')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open facebook' in query:
        webbrowser.open("facebook.com")

    elif 'open whatsapp' in query:
        webbrowser.open("web.whatsapp.com")


    elif 'play music' in query:
        music_dir = 'E:\\jay\\New folder (2)\\New folder\\musiic_vid\\music\\pendrive'
        songs = os.listdir(music_dir)
        print(songs)
        speak("playing ")
        os.startfile(os.path.join(music_dir, songs))
    elif 'pause music' in query:
        music_dir = 'E:\\jay\\New folder (2)\\New folder\\musiic_vid\\music\\pendrive'
        songs = os.listdir(music_dir)
        os.startfile(os.path.stop(songs))

    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, The time is {strTime}")

    elif 'open code' in query:
        codePath = "E:\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif 'email to jay' in query:
        try:
            speak("what should i say ? to jay ")
            content = takecommand()
            to = "sharmajijvs@gmail.com"
            sendEmail(to, content)
            speak("email has been sent !")
        except Exception as e:
            print(e)
            speak("sorry i am not able to send this email right now !")
    # elif  'reload' in query:
    # return query

    # elif 'shutdown' in query:
    # exit(0)
