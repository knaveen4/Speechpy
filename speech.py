import speech_recognition as sr
from datetime import datetime
import webbrowser

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        print("You said: " + recognizer.recognize_google(audio))
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def respond_to_command(command):
    if "hello" in command.lower():
        print("Hello! How can I help you?")
    elif "time" in command.lower():
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Current time is:", current_time)
    elif "date" in command.lower():
        current_date = datetime.now().strftime("%Y-%m-%d")
        print("Current date is:", current_date)
    elif "search" in command.lower():
        search_query = command.split("search")[-1].strip()
        search_url = f"https://www.google.com/search?q={search_query}"
        webbrowser.open(search_url)
        print(f"Searching the web for: {search_query}")
    else:
        print("Sorry, I don't understand that command.")

if __name__ == "__main__":
    while True:
        command = recognize_speech()
        if command:
            respond_to_command(command)
