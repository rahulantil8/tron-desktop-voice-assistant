import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)

recognizer = sr.Recognizer()
mic = sr.Microphone()

def speak(text):
    print("[TRON]", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("[TRON] Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("[TRON] Heard:", text)
        return text.lower()
    except Exception as e:
        print("[TRON] Error:", e)
        return None
