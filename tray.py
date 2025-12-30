import threading
import pystray
from pystray import MenuItem as item
from PIL import Image

from voice import listen
from commands import process

listening = True

def voice_loop():
    while listening:
        text = listen()
        if text:
            process(text)

def start_listening(icon, item):
    global listening
    if not listening:
        listening = True
        threading.Thread(target=voice_loop, daemon=True).start()

def stop_listening(icon, item):
    global listening
    listening = False

def exit_app(icon, item):
    icon.stop()
    exit(0)

def run_tray():
    image = Image.open("assets/tron.png")
    menu = (
        item("Start Listening", start_listening),
        item("Stop Listening", stop_listening),
        item("Exit", exit_app)
    )
    icon = pystray.Icon("Tron", image, "Tron Assistant", menu)
    threading.Thread(target=voice_loop, daemon=True).start()
    icon.run()
