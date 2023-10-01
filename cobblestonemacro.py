import pydirectinput
import time
import keyboard

pydirectinput.keyDown('alt')
pydirectinput.press('tab')
pydirectinput.press('tab')
pydirectinput.keyUp('alt')
pydirectinput.press('e')
pydirectinput.keyDown('z')

while True:
    pydirectinput.keyDown('w')    
