import os
import pyttsx3 #pip3 install pyttsx3
import datetime
import speech_recognition as s #pip3 install speechrecognition
import webbrowser 
import wikipedia#pip3 install wikipedia

engine=pyttsx3.init("espeak")#set the speak module to espeak

voice=engine.getProperty('voices')

engine.setProperty("voice",voice[10])#set the laguage of espeak to english
engine.setProperty("voice","english+f3")

engine.setProperty("rate",150)#set the speed of the voice

engine.runAndWait()#wait for the device to finish speaking

hrs=int(datetime.datetime.now().hour)
minu = int(datetime.datetime.now().minute)


def greetings():
    
    if hrs>5 and hrs<12:
        say("good morning")
    
    elif hrs>12 and hrs<18:
        say("good afternoon")

    elif hrs>18 and hrs<22:
        say("good evening")
    
    else:
        say("good night")


def time():
    date=datetime.datetime.now().day
    month=datetime.datetime.now().month
    say("The time is "+str(hrs)+"hours and "+str(minu)+"minute")
    if month ==1:
        currmonth="january"

    elif month==2:
        currmonth="february"

    elif month==3:
        currmonth="march"

    elif month==4:
        currmonth="april"

    elif month==5:
        currmonth="may"

    elif month==6:
        currmonth="june"

    elif month==7:
        currmonth="july"

    elif month==8:
        currmonth="agust"

    elif month==9:
        currmonth="september"

    elif month==10:
        currmonth="october"

    elif month==11:
        currmonth="november"

    elif month==12:
        currmonth="december"
    say("and it is "+str(date)+"th of"+currmonth)


def say(var):
    engine.say(var)
    engine.runAndWait()

def cmd():
    listener = s.Recognizer()
    with s.Microphone() as source:
        print("listening......")
        listener.energy_threshold=1000
        listener.pause_threshold=0.9
        audio = listener.listen(source)
    try:
        print("working on it please wait ")
        query =listener.recognize_google(audio,language="en-in")
        print("user said : ",query)

    except Exception as e:
        print(e)
        print("say that again please")
        return "none"

    return query


if __name__ == "__main__":
    
    greetings()
    #os.system("pip3 install pyaudio")
    
    while True:
        query=cmd().lower()

        if 'code' in query:
            say("opening visual studio")
            os.system("code")

        elif 'wikipedia' in query:
            say("searching wikipedia")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=1)
            say("according to wikipedia ")
            print(result)
            say(result)

        elif 'editor' in query:
            say("opening codeblocks")
            os.system("codeblocks")

        elif "about you" in query:
            say("I am the code which will be used for automating your day to day task with the help of python")
        
        elif "browser" in query:
            say("opening firefox")
            os.system("firefox")

        elif "youtube" in query:
            say("opening youtube")
            webbrowser.open("https://www.youtube.com/")
   
        elif  "quit" in query:
            say("thank you for utilizing me ")
            break
        
        elif  "time" in query:
            time()

        elif  "hello" in query:
            say("Hello jack i am jarvis you car mate ")


        else:
            say("hey i am not programmed to reply to that")
            