from pynput.mouse import Button, Controller

def sim_mouseclick():
  mouse = Controller()

  print("The current pointer position is {0}".format(
    mouse.position))

  mouse.position = (0, 750)
  print('Now we have moved it to {0}'.format(
      mouse.position))

  mouse.press(Button.left)
  mouse.release(Button.left)

def listen():
  listener = mouse.Listener(
    on_move