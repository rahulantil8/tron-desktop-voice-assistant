# listener.py
from voice import listen
from commands import process
import threading

def start_listener():
    def loop():
        while True:
            text = listen()
            if text:
                process(text)

    threading.Thread(target=loop, daemon=True).start()
