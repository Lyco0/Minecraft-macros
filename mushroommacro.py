import pydirectinput
import time

i=0

pydirectinput.keyDown('alt')
pydirectinput.press('tab')
pydirectinput.press('tab')
pydirectinput.keyUp('alt')
pydirectinput.press('e')

while True:
    pydirectinput.keyUp('z')
    time.sleep(0.5)
    pydirectinput.keyDown('z')
    time.sleep(1)
    pydirectinput.keyDown('w')
    pydirectinput.keyDown('a')
    time.sleep(35.55)
    pydirectinput.keyUp('a')
    time.sleep(1.85)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(40.60)
    pydirectinput.keyUp('d')
    i+=1
    if i==8:
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
        pydirectinput.press('m')


