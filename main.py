from time import sleep
from tkinter import *
from tkinter import ttk
from clicker import sim_mouseclick
from mouseTracker import listen
from RepeatedTimer import RepeatedTimer

def trigger_button():
  print("Pressed")
  if btn["text"] == "Start":
    # Start periodic clicking
    btn.config(text="Stop")
    listen()
    rt = RepeatedTimer(2, sim_mouseclick)
  else:
    btn["text"] == "Stop"
    btn.config(text="Start")
    rt.stop()

root = Tk()
root.geometry("200x50")
root.resizable(0,0)
root.title("Clicker")

btn_text = StringVar()
btn = ttk.Button(root, text="Start", command=trigger_button)
btn.pack()

root.bind("<Return>", lambda e: btn.invoke())
root.mainloop()