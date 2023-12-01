from tkinter import *
from threading import Thread
from time import sleep

timers = {
    1: {"time": 0, "running": False, "label": None, "start_button": None, "stop_button": None},
    2: {"time": 0, "running": False, "label": None, "start_button": None, "stop_button": None},
    3: {"time": 0, "running": False, "label": None, "start_button": None, "stop_button": None},
}

def start_timer(n):
    timer = timers[n]
    timer["start_button"].config(state="disabled")
    timer["running"] = True
    while timer["running"]:
        timer["time"] += 1
        sleep(0.001)
        s = timer["time"] // 1000
        ms = timer["time"] % 1000
        m = s // 60
        s = s % 60
        timer["label"].config(text=f"{m:02}:{s:02}.{ms:03}")

def stop_timer(n):
    timer = timers[n]
    timer["running"] = False
    timer["start_button"].config(state="normal")

def run_timer(n):
    Thread(target=start_timer, args=(n,), daemon=True).start()

root = Tk()

for n in timers:
    timer = timers[n]
    timer["start_button"] = Button(root, text="start", command=lambda n=n: run_timer(n))
    timer["stop_button"] = Button(root, text="stop", command=lambda n=n: stop_timer(n))
    timer["label"] = Label(root, text="00:00.00")
    
    timer["start_button"].grid(row=n, column=1)
    timer["stop_button"].grid(row=n, column=2)
    timer["label"].grid(row=n, column=3)

mainloop()