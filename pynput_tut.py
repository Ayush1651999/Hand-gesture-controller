from pynput.keyboard import Key, Controller

keyboard = Controller()

# keyboard.type('cd ..')

keyboard.press(Key.cmd)
keyboard.press('l')
keyboard.release(Key.cmd)