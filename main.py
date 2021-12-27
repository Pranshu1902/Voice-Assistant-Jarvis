# Jarvis (Virtual Assistant) by Pranshu

import os
import pyttsx3  
import webbrowser
import datetime
from datetime import date
import pyautogui
import time
import speech_recognition as sr
import cv2
import pytesseract
import re


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# initialize Text-to-speech engine  
engine = pyttsx3.init()  


#voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[2].id)


# convert this text to speech  
text = "Welcome, I am Jarvis your Voice Assistant"  
engine.say(text)  
# play the speech  
engine.runAndWait()  


def speak(text):
    """Speak the text input as paramete"""
    engine.say(text)
    engine.runAndWait()


def findDay(num):
    if num==0:
        return "Monday"
    elif num==1:
        return "Tuesday"
    elif num==2:
        return "Wednesday"
    elif num==3:
        return "Thursday"
    elif num==4:
        return "Friday"
    elif num==5:
        return "Saturday"
    else:
        return "Sunday"
    


def takeCommand():
    """Understand what user says"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))

# voice input, for sharing with gui
command = ""


def jarvis(audio, task):
    if audio=="yes":
        t = takeCommand()
        global command
        command = t
    else:
        t = task

    t = t.lower()



    if t=="initialise" or t=="initialize":
        # opens gmail (personal and work email) and whatsapp
        
        if pyautogui.locateOnScreen('google2.png', confidence=0.6):
            x,y,w,h = pyautogui.locateOnScreen('google2.png')
        elif pyautogui.locateOnScreen('google.png'):
            x,y,w,h = pyautogui.locateOnScreen('google.png')
        pyautogui.click(x+w//2, y+h//2)

        time.sleep(3)

        webbrowser.get("chrome").open("gmail.com")
        webbrowser.get("chrome").open("web.whatsapp.com")

        time.sleep(2)
        # work email
        pyautogui.hotkey("ctrl", "shift", "m")
        time.sleep(2)
        pyautogui.hotkey("enter")
            
        time.sleep(2)
        pyautogui.typewrite("gmail.com")
        pyautogui.hotkey("enter")
        
    elif t=="open gmail":
        webbrowser.get("chrome").open("gmail.com")
        
    elif t=="open leetcode":
        webbrowser.get("chrome").open("leetcode.com")
        
    elif t=="open whatsapp":
        webbrowser.get("chrome").open("web.whatsapp.com")
        x,y,w,h = pyautogui.locateOnScreen('whatsapp_app.png')
        pyautogui.click(x+w//2, y+h//2)

        
    elif t=="open youtube":
        webbrowser.get("chrome").open("youtube.com")
        
    elif t=="music":
        webbrowser.get("chrome").open("https://www.youtube.com/watch?v=a59gmGkq_pw&list=RDa59gmGkq_pw&start_radio=1")
        
    elif t=="hope":
        webbrowser.get("chrome").open("https://www.youtube.com/watch?v=8nb6zgHSvww&list=LL&index=1")
        
    elif t=="class":
        # atomatically joins the class based on the timetable

        x,y,w,h = pyautogui.locateOnScreen('teams.png', confidence=0.8)
        pyautogui.click(x+w//2, y+h//2)
            
        time.sleep(5)

        # maximize
        if pyautogui.locateOnScreen('mini.png'):
            x,y,w,h = pyautogui.locateOnScreen('mini.png')
            pyautogui.click(x+w//2, y+h//2)
            
        time.sleep(2)
        # selecting teams tab
        pyautogui.click(x=46, y=277)

        time.sleep(2)
        # selecting the team based on timetable
        stop=False

        now = datetime.datetime.today()
        day = findDay(now.weekday())
        a = datetime.datetime.today()
            
        if day=="Monday":
            if datetime.time(7,50) <= a.time() < datetime.time(8,50):
                # BCHY
                pyautogui.click(x=1209, y=391)
            elif datetime.time(10,30) <= a.time() < datetime.time(11,30):
                # BSTS
                pyautogui.click(x=337, y=769)
            elif datetime.time(13,50) <= a.time() < datetime.time(15,40):
                # BCSE
                pyautogui.click(x=345, y=391)
            else:
                stop=True
                x,y,w,h = pyautogui.locateOnScreen("cross.png")
                pyautogui.click(x+w//2, y+h//2)
                print("No class right now")
                speak("No class right now")
            
        elif day=="Tuesday":
            if datetime.time(7,50) <= a.time() < datetime.time(8,50):
                # BSTS
                pyautogui.click(x=337, y=769)
            elif datetime.time(9,40) <= a.time() < datetime.time(10,40):
                # BMAT
                pyautogui.click(x=784, y=376)
            elif datetime.time(13,50) <= a.time() < datetime.time(15,40):
                # BMAT Lab
                pyautogui.click(x=784, y=769)
            else:
                stop=True
                x,y,w,h = pyautogui.locateOnScreen("cross.png")
                pyautogui.click(x+w//2, y+h//2)
                print("No class right now")
                speak("No class right now")
            
        elif day=="Wednesday":
            if datetime.time(7,50) <= a.time() < datetime.time(8,50):
                # BEEE
                pyautogui.click(x=1663, y=372)
            elif datetime.time(8,45) <= a.time() < datetime.time(9,45):
                # BCHY
                pyautogui.click(x=1209, y=391)
            elif datetime.time(10,35) <= a.time() < datetime.time(11,30):
                # BCSE
                pyautogui.click(x=345, y=391)
            elif datetime.time(13,50) <= a.time() < datetime.time(15,40):
                # BEE Lab
                pyautogui.click(x=1664, y=738)
            else:
                stop=True
                x,y,w,h = pyautogui.locateOnScreen("cross.png")
                pyautogui.click(x+w//2, y+h//2)
                print("No class right now")
                speak("No class right now")
            
        elif day=="Thursday":
            if datetime.time(8,40) <= a.time() < datetime.time(9,40):
                # BSTS
                pyautogui.click(x=337, y=769)
            elif datetime.time(10,35) <= a.time() < datetime.time(11,30):
                # BMAT
                pyautogui.click(x=784, y=376)
            elif datetime.time(13,50) <= a.time() < datetime.time(15,40):
                # BCSE Lab
                pyautogui.click(x=345, y=391)
            else:
                stop=True
                x,y,w,h = pyautogui.locateOnScreen("cross.png")
                pyautogui.click(x+w//2, y+h//2)
                print("No class right now")
                speak("No class right now")
            
        elif day=="Friday":
            if datetime.time(7,50) <= a.time() < datetime.time(8,50):
                # BMAT
                pyautogui.click(x=784, y=376)
            elif datetime.time(8,45) <= a.time() < datetime.time(9,40):
                # BEEE
                pyautogui.click(x=1663, y=372)
            elif datetime.time(9,40) <= a.time() < datetime.time(10,40):
                # BCHY
                pyautogui.click(x=1209, y=391)
            elif datetime.time(15,40) <= a.time() < datetime.time(17,30):
                # BCHY Lab
                pyautogui.click(x=1221, y=756)
            else:
                stop=True
                x,y,w,h = pyautogui.locateOnScreen("cross.png")
                pyautogui.click(x+w//2, y+h//2)
                print("No class right now")
                speak("No class right now")
            
        else:
            stop=True
            print("No class right now")
            x,y,w,h = pyautogui.locateOnScreen("cross.png")
            pyautogui.click(x+w//2, y+h//2)

        if stop==False:
            time.sleep(3)

            while pyautogui.locateOnScreen('join1.png')==None:
                pass
            # first join button
            x,y,w,h = pyautogui.locateOnScreen('join1.png')
            pyautogui.click(x+w//2, y+h//2)

            time.sleep(5)

            # muting the mic if it is on unmute
            if pyautogui.locateOnScreen('mic.png'):
                x,y,w,h = pyautogui.locateOnScreen('mic.png')
                pyautogui.click(x+w//2, y+h//2)
            
            time.sleep(3)
            # final join button
            x,y,w,h = pyautogui.locateOnScreen('join2.png', confidence=0.8)
            pyautogui.click(x+w//2, y+h//2)

    elif t=="timetable":
        now = datetime.datetime.today()
        speak(date.today())
        day = findDay(now.weekday())
        speak("Today is "+day)
        #speak(timetable(day, datetime.time(8,10)))

    elif "google" in t:
        a = t.split()
        st = ""
        for i in range(1,len(a)-1):
            st+=a[i]
            st+="+"
        st += a[-1]
        webbrowser.get("chrome").open("https://www.google.com/search?q="+st)
        
    elif t=="whatsapp autoreply":
        webbrowser.get("chrome").open("web.whatsapp.com")
        time.sleep(10)
        x,y,w,h = pyautogui.locateOnScreen('whatsapp.png', confidence=0.7)
        pyautogui.click(x,y)
        time.sleep(2)
        pyautogui.typewrite("autoreply")
        pyautogui.hotkey("enter")
    
    elif t=="check gmail":
        webbrowser.get("chrome").open("gmail.com")

        time.sleep(6)
        x,y,w,h = pyautogui.locateOnScreen('inbox (2).png', confidence=0.6)

        img = pyautogui.screenshot(region=(x, y, 2*w, 2*h))

        text = pytesseract.image_to_string(img)

        num = re.search("[0-9]", text)
        print(text[num.span()[0]])
        speak(text[num.span()[0]]  + " unread emails")
        
    else:
        speak("Sorry, I didnt catch that")



