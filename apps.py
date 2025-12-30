import os
import subprocess

APP_MAP = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vs code": r"C:\Users\Dell\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "notepad": "notepad.exe"
}

def open_app(name):
    name = name.lower()
    if name in APP_MAP:
        try:
            os.startfile(APP_MAP[name])
            return True
        except:
            subprocess.Popen(APP_MAP[name])
            return True
    return False
