import time #This module provides various functions to manipulate time values

import smtplib #defines an SMTP (Simple Mail Transfer Protocol) client session object that can be used to send mail to any Internet machine with an SMTP

import random #The random module gives access to various useful functions and one of them being able to generate random numbers, which is randint()

import os #The OS module in Python provides functions for interacting with the operating system

import pyttsx3 #The OS module in Python provides functions for interacting with the operating system

import speech_recognition as sr #To convert speech to text the one and only class we need is the Recognizer class from the speech_recognition module.

import datetime #supplies classes to work with date and time.
# These classes provide a number of functions to deal with dates, times and time intervals. Date and datetime are an object in Python

import wikipedia #Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia

from selenium import webdriver #The selenium package is used to automate web browser interaction from Python.

import logging #allows writing status messages to a file or any other output streams. 

from selenium.webdriver.remote.remote_connection import LOGGER #Turning off logging in Selenium (from Python)
LOGGER.setLevel(logging.WARNING)


engine = pyttsx3.init('sapi5') # Constructs a new Text To Speech engine instance using sapi5
vocies = engine.getProperty('voices') # to know properties of voice
print(vocies[1].id) # to see which person is talking
engine.setProperty('voices', vocies[0].id) # set the property of voice


def speak(audio): # This Function Takes a Audio Parameter And converts the text into Audio
    engine.say(audio)
    engine.runAndWait()


def wishMe(): # This Function Function wishes the user according Time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Abhinav Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Abhinav Sir!")

    else:
        speak("Good Evening Abhinav Sir!")

    speak("I am Jarvis. Please tell me how may I help you")
    print("Wishing my friend")


def takeCommand(): #this take audio from microphne and converts it into english india using recognize_google apli
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


with open('C:\\Users\\abhin\\password.txt') as f:
    password = f.read()

frommail = 'abhinav.gupta.02.08@gmail.com'


def sendEmail(to, content): # this function sends email using Simple Mail Transfer Protocol library
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(frommail, password)
    server.sendmail(frommail, to, content)
    server.close()


if __name__ == "__main__":
    # wishMe()
    while True:

        query = takeCommand().lower() # Lower case the String said by User

        if 'wikipedia' in query: # if given text string contain wikipedia in it then it will search that on wikipedia
            speak('Searching Wikipedia....')
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            print(results)
            speak("According to Wikipedia,")
            speak(results)

        elif 'open youtube' in query: # if given string contain "open youtube" then it will open Youtube
            speak("Opening Youtube")
            driver = webdriver.Chrome(
                executable_path="C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.youtube.com/")

        elif 'open google' in query: # if given string contain "open google" then it will open google
            speak("Opening Google")
            driver = webdriver.Chrome(
                executable_path="C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.google.com/")

        elif 'open stack overflow' in query: # if given string contain "open stackoverflow" then it will open stackoverflow
            speak("Opening Stakoverflow")
            driver = webdriver.Chrome(
                executable_path="C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.stackoverflow.com/")

        elif 'play music' in query: # if given string contain "play music" then it will play any random music from the given directory
            speak("Playing Random Song from your folder")
            music_dir = "C:\\Users\\abhin\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))

        elif 'the time' in query: # if given string contain "the time" then it will speak and show the time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")

        elif 'the date' in query: # if given string contain "the date" then it will speak and show the date
            strdate = datetime.datetime.now().strftime("%D")
            print(strdate)
            speak(f"Sir today's date is {strdate}")

        elif 'open vs code' in query: # if given string contain "open vs code" then it will do that
            speak("Opening Vs Code")
            vspath = "C:\\Users\\abhin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vspath)

        elif 'open chrome' in query: # if given string contain "open chrome" then it will open chrome
            chromepath = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            os.startfile(chromepath)

        elif 'email to abhinav' in query: # if given string contain "email to abhinav" then it send a mail to the following perso with the the content spoken by the user
            try:
                speak("What Should I send?")
                content = takeCommand()
                to = "abhinavgupta020208@gmail.com"
                print("Sending email")
                speak("Sending email")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry Sir mail couldn't be send. Due to errors:")
                print(e)

        elif 'open gmail' in query: # This will open Gmail using Selenium and WebDriver
            try:
                speak("Opening Gmail in Chrome for Pooja")
                from selenium import webdriver
                driver = webdriver.Chrome(
                    executable_path='C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe')
                driver.get('https://mail.google.com/mail/u/0/#inbox')
                username = driver.find_element_by_xpath(
                    '//*[@id="identifierId"]')
                username.click()
                username.send_keys('2018.pooja.gupta@ves.ac.in')
                next = driver.find_element_by_xpath(
                    '//*[@id ="identifierNext"]')
                next.click()
                time.sleep(3)
                password = driver.find_element_by_xpath(
                    '//*[@id="password"]/div[1]/div/div[1]/input')
                password.click()
                with open('C:\\Users\\abhin\\2018poojapass.txt') as g:
                    password2 = g.read()
                    password.send_keys(password2)
                next = driver.find_element_by_xpath('//*[@id ="passwordNext"]')
                next.click()
            except Exception as e:
                print('Sorry')

        elif 'how are you' in query:
            speak("I an fine Sir. Thank You for asking")

        elif 'your name' in query:
            speak("My name is Jarvis and I can do many tasks.")

        elif 'multiply' in query:
            try:
                speak("Please say the first number")
                number1 = takeCommand()
                speak("Please say the Second number")
                number2 = takeCommand()
                speak(
                    f"{number1} multiplied by {number2} equals to {int(number1)*int(number2)}")
                print(
                    f"{number1} multiplied by {number2} equals to {int(number1)*int(number2)}")
            except Exception as e:
                print(e)
                speak("sorry I couldn't multiply the numbers due to internal errors")

        elif 'add' in query:
            try:
                speak("Please say the first number")
                num1 = takeCommand()
                speak("Please say the Second number")
                num2 = takeCommand()
                speak(
                    f"{num1} plus {number2} equals to {int(num1)+int(num2)}")
                print(
                    f"{num1} plus {number2} equals to {int(num1)+int(num2)}")
            except Exception as e:
                print(e)
                speak("sorry I couldn't Add the numbers due to internal errors")

        elif 'Subtract' in query:
            try:
                speak("Please say the first number")
                numb1 = takeCommand()
                speak("Please say the Second number")
                numb2 = takeCommand()
                speak(
                    f"{numb1} subtracted by {numb2} equals to {int(numb1)-int(numb2)}")
                print(
                    f"{numb1} subtracted by {numb2} equals to {int(numb1)-int(numb2)}")
            except Exception as e:
                print(e)
                speak("sorry I couldn't Subtract the numbers due to internal errors")

        elif 'the table of' in query:
            try:
                speak("Please repeat the number")
                tableof = takeCommand()
                if tableof == None:
                    break
                for i in range(1, 11):
                    a = int(tableof) * i
                    speak(f"{tableof} into {i} equals to {a}")
                    print(f"{tableof} into {i} equals to {a}")
            except Exception as e:
                speak("sorry I couldn't say the table due to internal errors")

        elif 'open whatsapp' in query:
            whatsapppath = "C:\\Users\\abhin\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsapppath)

        elif 'open telegram' in query:
            telegrampath = "C:\\Users\\abhin\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(telegrampath)

        elif 'the square' in query:
            try:
                speak("Please repeat the number")
                squ = takeCommand()
                a = int(squ)
                b = a * a
                speak(f"The square of {squ} is {b}")
            except Exception as e:
                speak("sorry I couldn't say the table due to internal errors")

        elif 'the weather' in query:
            speak("You can see the weather and temperature on the screen")
            driver = webdriver.Chrome(
                executable_path='C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe')
            driver.get(
                'https://weather.com/en-IN/weather/today/l/98f2fa2e5164f762a871e01c8ce7c8f88b1c92c907d8870d7b646a16bbe523db')

        elif 'the temperature' in query:
            speak("You can see the weather and temperature on the screen")
            driver = webdriver.Chrome(
                executable_path='C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe')
            driver.get(
                'https://weather.com/en-IN/weather/today/l/98f2fa2e5164f762a871e01c8ce7c8f88b1c92c907d8870d7b646a16bbe523db')

        elif 'search' in query:
            a = query.replace("search ", "")
            driver = webdriver.Chrome(
                executable_path="C:\\Users\\abhin\\OneDrive\\Desktop\\Project_Jarvis\\chromedriver_win32\\chromedriver.exe")
            driver.get("https://www.google.com/search?q=" + a)
            time.sleep(1)

        elif 'shutdown' in query:
            speak("Now turning off the pc...")
            try:
                os.system("shutdown /s /t 1")
            except Exception as e:
                print(e)
                speak("Couldn't Shutdown the pc due to internal error")

        elif 'restart' in query:
            speak("Now restarting the pc...")
            try:
                os.system("shutdown /r /t 0")
            except Exception as e:
                print(e)
                speak("Couldn't restart the pc due to internal error")

        elif 'close the program' in query:
            break

        else:
            print("Sorry I cant do this right now")
