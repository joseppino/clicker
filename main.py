import sys
import os
from tkinter import *
from tkinter import ttk
from clicker import sim_mouseclick
from interval import call_repeatedly
from pynput import mouse
from time import time

root = Tk()

# interval in seconds
TIMER_INTERVAL = 2
SCREEN_WIDTH = root.winfo_screenwidth()

# initialise interval function variable
intv = None
active_timer = time()

def trigger_button():
  if btn["text"] == "Start":
    # Start periodic clicking
    btn.config(text="Stop")
    ttk.Style().configure("TButton", background="red")
    global intv
    intv = call_repeatedly(TIMER_INTERVAL, simulate_action, (SCREEN_WIDTH / 2, 0))
  else:
    btn["text"] == "Stop"
    btn.config(text="Start")
    ttk.Style().configure("TButton", background="green")
    intv()

def simulate_action(coords):
  global active_timer
  listener = listen()
  # if user inactive for more than 4.5mins
  if time() - active_timer > 270:
    sim_mouseclick(coords)
    active_timer = time()

def on_click(x, y, button, pressed):
  global active_timer
  active_timer = time()
  if not pressed:
    # Stop listener
    return False

def listen():
  listener = mouse.Listener(
    on_click=on_click)
  listener.start()
  return listener

# define respath function for bundled exe output to still locate ico resource
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root.iconbitmap(resource_path("pointer-hand.ico"))
root.geometry("200x50")
# make window non-resizable on either axis
root.resizable(0,0)
root.title("Clicker")

ttk.Style().configure("TButton", background="green")
btn = ttk.Button(root, text="Start", command=trigger_button)
btn.pack()

# bind return key to trigger the button
root.bind("<Return>", lambda e: btn.invoke())
root.mainloop()