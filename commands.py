import webbrowser
from voice import speak
from apps import open_app
from ai import ask_ai

WAKE_WORDS = ["hey tron", "tron"]
listening = False

def process(cmd):
    global listening
    cmd = cmd.lower().strip()

    # 🟢 Wake word
    if any(w in cmd for w in WAKE_WORDS):
        listening = True
        speak("Yes, I am listening")
        return

    # 🟡 Ignore until wake word
    if not listening:
        return

    # 🔵 Open apps
    if cmd.startswith("open "):
        app = cmd.replace("open ", "")
        if open_app(app):
            speak(f"Opening {app}")
        else:
            speak("Application not found")
        listening = False
        return

    # 🤖 AI FIRST (for questions)
    if any(q in cmd for q in ["what", "who", "explain", "define", "how"]):
        ask_ai(cmd)
        listening = False
        return

    # 🌐 Google fallback (LAST)
    speak("Searching on Google")
    webbrowser.open("https://www.google.com/search?q=" + cmd)
    listening = False
