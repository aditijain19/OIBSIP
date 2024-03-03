import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Can you please repeat?")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def greet():
    current_time = datetime.datetime.now().hour
    if 0 <= current_time < 12:
        speak("Good morning! How can I assist you today?")
    elif 12 <= current_time < 18:
        speak("Good afternoon! How can I assist you today?")
    else:
        speak("Good evening! How can I assist you today?")

def search_wikipedia(query):
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia...")
    speak(results)

def open_website(url):
    webbrowser.open(url)

def play_music():
    music_dir = "C:\\Music"  # Change this to your music directory
    songs = os.listdir(music_dir)
    if len(songs) == 0:
        speak("No music files found in the directory.")
        return
    speak("Playing music...")
    os.startfile(os.path.join(music_dir, songs[0]))  # Open the first song in the directory

def main():
    greet()
    while True:
        query = listen()
        if "exit" in query:
            speak("Goodbye!")
            break
        elif "hello" in query:
            speak("Hello there! How can I assist you?")
        elif "what is" in query:
            search_wikipedia(query)
        elif "open" in query:
            if "youtube" in query:
                open_website("https://www.youtube.com")
            elif "google" in query:
                open_website("https://www.google.com")
            else:
                speak("Sorry, I can't open that website.")
        elif "play music" in query:
            play_music()
        else:
            speak("Sorry, I didn't understand. Can you please repeat?")

if __name__ == "__main__":
    main()
