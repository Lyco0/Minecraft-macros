import pydirectinput
import time
import keyboard

i=0
pydirectinput.keyDown('alt')
pydirectinput.press('tab')
pydirectinput.press('tab')
pydirectinput.keyUp('alt')
pydirectinput.press('e')

while True:
    pydirectinput.keyUp('z')
    pydirectinput.keyDown('z')
    pydirectinput.keyDown('d')
    time.sleep(18.90)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('w')
    time.sleep(1.10)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('a')
    time.sleep(18.90)
    pydirectinput.keyUp('a')
    i+=1
    if i==19:
        pydirectinput.press('/')
        pydirectinput.press('w')
        pydirectinput.press('a')
        pydirectinput.press('r')
        pydirectinput.press('p')
        pydirectinput.press(' ')
        pydirectinput.press('g')
        pydirectinput.press('a')
        pydirectinput.press('r')
        pydirectinput.press('d')
        pydirectinput.press('e')
        pydirectinput.press('n')
        pydirectinput.press('return')
        time.sleep(1)
        i = 0
    else:
        pydirectinput.keyDown('w')
        time.sleep(1.10)
        pydirectinput.keyUp('w')
