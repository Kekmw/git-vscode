import pynput

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()


def on_click(x, y, button, pressed):
    keyboard.press('z')
    keyboard.release('z')


with pynput.mouse.Listener(on_click=on_click) as listener:
    listener.join()
