import pyttsx3, datetime, os, cv2, random, wikipedia,subprocess, webbrowser, smtplib, sys, time, requests, pyautogui, os.path,pyjokes,GoogleNews
import speech_recognition as sr
from requests import get
from selenium import  webdriver
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from newsapi import NewsApiClient
import pygetwindow as gw

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[len(voices) - 2] .id)
engine.setProperty('rate', 210)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=10,phrase_time_limit=10)

    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en -in')
        print(f"user said:{query}")

    except Exception as e:
        # speak("say that again please")
        return "none"
    return query
    
def username(s1):
    try:
        speak(f"what i should to call you Sir{s1}")
        s = takecommand()
        s= s.replace("call me",'')
        speak(f"hello {s1}")
        speak(s)
        with open("data of user.text","a") as e:
            st = datetime.datetime.now()
            st1 = datetime.toda()
            e.write(f"{s} use me on {st1}at{st} / n")
            e.close()
            speak(f"how can i help you{s1}")
            
    except Exception as e:
        speak(f"{s1} i dont unnderstand , What did u say , PLease sat it again Sir")
        username(s1)

def me():
    s = "YES Sir! "
    speak(s)
    speak("how can i help you !")

def increase_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    current_volume = volume.GetMasterVolumeLevelScalar()
    volume.SetMasterVolumeLevelScalar(min(1.0, current_volume + 0.1), None)

def open_calculator():
    subprocess.Popen('calc.exe')  # Open the calculator
    time.sleep(1)  # Allowing time for the calculator to open

def open_camera():
    speak("Opening the camera. Please wait for a moment.")
    # Open the camera using opencv-python
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        # Save the captured frame to the specified location
        output_path = "C:/AiOutput"
        os.makedirs(output_path, exist_ok=True)
        file_path = os.path.join(output_path, "captured_photo.jpg")
        cv2.imwrite(file_path, frame)
        speak(f"Photo captured and saved to {file_path}.")
    else:
        speak("Failed to capture the photo. Please try again.")
    cap.release()
    cv2.destroyAllWindows()

def get_latest_news():
    # Initialize the NewsApiClient with your API key
    newsapi = NewsApiClient(api_key='6c8718c72fa14e4a8a73ccd36588c0f9')

    # Fetch the top headlines
    top_headlines = newsapi.get_top_headlines(language='en')

    if top_headlines['status'] == 'ok':
        articles = top_headlines['articles']

        if articles:
            speak("Today's Top News Headlines:")
            for index, article in enumerate(articles, start=1):
                speak(f"{index}. {article['title']}")
        else:
            print("No articles found.")
    else:
        print("Failed to fetch news.")
        
global i1
global sex
def into():
    while (1):
        try:
            s1 = takecommand().lower()
            s1 = s1.replace('im','')
            if 'prince kumar'in s1 or "prince" in s1:
                sex = 'sir'
            else:
                speak("please identify your self ")
                s1  = takecommand().lower()
                if 'male' in s1 or 'boy'in s1:
                    speak("please identify your name")
                    if "prince kumar" in s1 or "prince" in s1:
                        wishme()

                elif "female " in s1 or "girl" in s1:
                    sex = "MADAMM."
                else:
                    into()
                    i1 =+1
                
            if "prince" not in s1:
                username(sex)
                # print(sex)
                wishme(sex)
                break
            else:
                # print(sex)
                wishme(sex)
                break
        except Exception as e:
            i1 =+1
            into()

def stoplisting():
    speak("for how much seconds you want to stop the program Sir?")
    if "10second"in query:
        try:
            a = int(takecommand())
            speak("going to sleep Sir")
            speak(a)
            time.sleep(a)
        except Exception as e:
            speak(" I could not understand What did you sat ")
            stoplisting()

def get_weather(api_key, city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={'Jamshedpur'}&appid={'56464fe451976bc5af28936ab4e2d5c0'}&units=metric"

    response = requests.get(complete_url)
    if response.status_code == 200:
        weather_data = response.json()

        if weather_data["cod"] == 200:
            weather_description = weather_data['weather'][0]['description']
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            wind_speed = weather_data['wind']['speed']

            print(f"Weather: {weather_description}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print("City not found.")
    else:
        print("Failed to fetch weather data.")
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = '56464fe451976bc5af28936ab4e2d5c0'
    city = 'Jamshedpur'  # Replace with your city name
    get_weather(api_key, city)

def walkupme():
    strftime = datetime.datetime.now().strftime("%I:%S:%p")
    speak(f"it is {strftime} you have yo wakeup Sir.")

def minimize_active_window():
    speak("Minimizing the windows...")
    # Get the currently active window
    active_window = gw.getActiveWindow()
    if active_window:
        active_window.minimize()

def slide_window_up():
    screenWidth, screenHeight = pyautogui.size()
    slide_distance = int(screenHeight / 2)  # Adjust the slide distance as needed
    pyautogui.moveTo(screenWidth // 2, screenHeight // 2 + slide_distance, duration=0.5)
    pyautogui.dragTo(screenWidth // 2, screenHeight // 2 - slide_distance, duration=0.5, button='left')


def run(self):
    speak("wakeup avi")
    while True:
        self.query = self.takecommand()
        if "wake up " in self.query or "are you there " in self.query or"hello" in self.query:
            self.takecommand()

def wishme():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M:%S:%p")
    current_time = time.strftime(("'%Y-%m-%d %A'"))
    if hour >= 0 and hour <= 12:
        speak(f"Good Morning, {current_time}")

    elif hour >=12 and hour >=18:
        speak(f"Good Afternoon, {current_time}")

    else:
        speak(f"Good Evening, {current_time}")

    speak("Hello sir, I am evi. please tell me how may i help you")

if __name__ == "__main__":
    #into()
    wishme()
    
    while True:

        query = takecommand().lower()
        
        if 'hi evi' in query or 'hello evi' in query:
            speak('how can i assist you?')

        elif "sleep" in query:
            stoplisting()
 
        elif "open command" in query: 
            os.system("start cmd")

        elif "minimize the windows" in query or "slide down the windows" in query or "minimize everything" in query:
            minimize_active_window()

        # elif "slide up windows" in query or "slide up window" or "pick up the windows":
        #     slide_window_up()

        elif "volume up" in query or "increase volume" in query:
            increase_volume()

        elif "open camera " in query:
            speak(f"opening camera")
            open_camera()

        elif "wikipedia" in query:
            speak("Searching wikipedia....?")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2) 
            speak("according to wikipedia")
            engine.setProperty('rate', 190)
            speak(results)
            print(results)

        elif "hello" in query:
            me()

        elif "who are you"in query:
            speak("i am evi Sir")

        elif "who made you" in query or "who created you " in query :
            speak("i have been created by prince ")

        elif "click" in query:
            pyautogui.click()

        elif "tell me news" in query or "tell me today news" in query or "say news"in query:
            get_latest_news()

        elif " tell me today's weather" in query:
                get_weather()

        elif "open calculator" in  query:
            speak("opening calculater")
            open_calculator()

        elif 'help me' in query:
            speak(f"ofcurse Sir ! How can i help you Sir")
            speak("There are 3 thing that i can do for you sir i can search for it on google, youtube or wikipedia")  
            speak(f"where i should to serach ")
            s = takecommand()
            s = takecommand().lower()
            if s == 'google':
                speak(f"opening  google!")
                webbrowser.open("www.bing.com/search?q=" + s + "=9d02b0a92caa4bc895c28ea9269d27e6&FORM=ANAB01&PC=ASTS")
            
            if s == "youtube" or "search on youtube":
                speak(f"opening youtube sir")
                speak("what should I Search in Youtube sir?")
                s = takecommand()
                webbrowser.open("www.youtube.com/results?search_query="+ s)

            if s == "wikipedia":
                speak("what should I Search in Wikipedia sir?")
                speak

            if s == "exit":
                speak("ok sir..")
                exit()

        elif "who is prince" in query:
                speak(
                    f"yes{sex} i know him becuase of him im able to talk to you he is a very nice person would you like to know more about mister ")
                s = takecommand().lower()
                if s == "yes":
                    me()
                else:
                    speak(f"ok !{sex} thank you for give me time sir")

        elif 'i want to search' in query or 'write'in query or "search" in query:
                speak("ok sir please say what you want to write or search sir")
                s=takecommand()
                pyautogui.write(s)
                time.sleep(3)
                pyautogui.press('enter')
                speak("srearching sir.")

        elif "open youtube" in query:
            speak("about what should i Search on youtube Sir?.")
            s =  takecommand()
            webbrowser.open("www.youtube.com/results?search_query="+ s)

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif " set timer" in query or "set stopwatch" in query:
            speak("for how many minutes?")
            timing = takecommand()
            timing = timing.replace('minutes','')
            timing = timing.replace('minutes','')
            timing = timing.replace('for','')
            timing = float(timing)
            timing = timing * 60
            speak(f"i will remind you in {timing} seconds")
            time.sleep(timing)
            speak('your time has been finished sir?')

        elif "no thanks" in query:
            speak("tanks for using me sir,have a good day sir.")
            sys.exit()

        elif "close notepad" in query:
            speak("okay sir, closing notpad")
            os.system("taskkill /f /im notpad.exe")

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

        elif" restart the system" in query:
            os.system("shutdown /r /t 1")

        elif "sleep the system" in query:
            os.system("rundll32.exe powerprof.idl,SetSuspended 0,1,0")

        elif "what's your name" in query or "what is your name" in query:
            speak("My name is evi. Nice to meet you Sir")

        elif "can we a friend's" in query:
            speak("off course Sir!")

        elif"tell me current time and date " in query:
            speak("sure Sir! {tt} ,{current_time}")

        elif"evi" in query:
            speak("hello i am there Sir!.")

        elif"say somethings " in query or "say somethings evi" in query:
            speak("what are doing sir!")
            s = takecommand().lower()
            speak("okay SIr. let's do some fun")

        elif "switch the windows" in query or "switch the tab"in query:
            speak("okay sir")
            pyautogui.hotkey('alt','tab')

        elif "stop the music" in query or 'stop' in query:
            speak('okay')
            pyautogui.press('Space')

        elif "play the music" in query or 'play' in query:
            speak("okay")
            pyautogui.press('space')

        elif "what is the time " in query:
            now_time = datetime.datetime.now()
            speak(f"okk Sir!  current time is{now_time}")

        elif "how are you" in query or "kasise ho " in query:
            speak("i am good . tell me about u sir")

        elif "Good evi" in query:
            speak('Thanks you sir..')

        elif "exit" in query:
            if "yes":
                speak("ok Sir have a nice day!")
                exit()
            else:
                break   
       

if __name__ == "__main__":
    wishme()
