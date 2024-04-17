from pynput.mouse import Button, Controller

def sim_mouseclick(coords):
  mouse = Controller()

  mouse.position = (coords[0], coords[1])

  mouse.press(Button.left)
  mouse.release(Button.left)