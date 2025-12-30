import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import queue

from voice import listen
from commands import process

class TronGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tron Assistant")
        self.root.geometry("700x450")
        self.root.configure(bg="#1e1e1e")

        self.queue = queue.Queue()

        self.text = ScrolledText(
            self.root,
            bg="#111",
            fg="#0f0",
            insertbackground="#0f0",
            font=("Consolas", 11)
        )
        self.text.pack(fill="both", expand=True, padx=10, pady=10)

        self.entry = tk.Entry(
            self.root,
            bg="#222",
            fg="white",
            insertbackground="white",
            font=("Consolas", 12)
        )
        self.entry.pack(fill="x", padx=10, pady=(0,10))
        self.entry.bind("<Return>", self.on_enter)

        self.log("Tron GUI started")

        threading.Thread(target=self.voice_loop, daemon=True).start()
        self.root.after(100, self.process_queue)

    def log(self, msg):
        self.text.insert(tk.END, msg + "\n")
        self.text.see(tk.END)

    def on_enter(self, event):
        cmd = self.entry.get().strip()
        if cmd:
            self.log("> " + cmd)
            process(cmd)
            self.entry.delete(0, tk.END)

    def voice_loop(self):
        while True:
            text = listen()
            if text:
                self.queue.put(text)

    def process_queue(self):
        while not self.queue.empty():
            text = self.queue.get()
            self.log("> " + text)
            process(text)
        self.root.after(100, self.process_queue)

    def run(self):
        self.root.mainloop()
