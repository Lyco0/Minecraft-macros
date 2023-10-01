import pydirectinput
import time
import keyboard

pydirectinput.keyDown('alt')
pydirectinput.press('tab')
pydirectinput.press('tab')
pydirectinput.keyUp('alt')
pydirectinput.press('e')


while True:
    pydirectinput.keyDown('d')
    time.sleep(1)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('a')
    time.sleep(1)
    pydirectinput.keyUp('a')

