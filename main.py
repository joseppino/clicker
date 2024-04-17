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
TIMER_INTERVAL = 15

# initialise interval function variable
intv = None
active_timer = time()
num_autoclicks = 0

def trigger_button():
  if btn["text"] == "Start":
    # Start periodic clicking
    btn.config(text="Stop")
    ttk.Style().configure("TButton", background="red")
    global intv
    intv = call_repeatedly(TIMER_INTERVAL, simulate_action, (root.winfo_screenwidth() / 2, 0))
  else:
    btn["text"] == "Stop"
    btn.config(text="Start")
    ttk.Style().configure("TButton", background="green")
    global num_autoclicks
    num_autoclicks = 0
    label.config(text="Auto-clicks: 0")
    intv()

def simulate_action(coords):
  global active_timer
  global num_autoclicks
  listener = listen()
  # if user inactive for more than 4.5mins
  if time() - active_timer > 270:
    sim_mouseclick(coords)
    num_autoclicks += 1
    label.config(text="Auto-clicks: {0}".format(num_autoclicks))
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
label = ttk.Label(root, text='Auto-clicks: 0')
label.pack()

# bind return key to trigger the button
root.bind("<Return>", lambda e: btn.invoke())
root.mainloop()