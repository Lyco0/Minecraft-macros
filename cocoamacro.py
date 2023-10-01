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
    pydirectinput.keyDown('z')
    time.sleep(1)
    pydirectinput.keyDown('w')
    time.sleep(16.74)
    pydirectinput.keyUp('w')
    pydirectinput.keyDown('d')
    time.sleep(1)
    pydirectinput.keyUp('d')
    pydirectinput.keyDown('s')
    time.sleep(16.80)
    pydirectinput.keyUp('s')
    
    i+=1
    if i==31:
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
        pydirectinput.keyDown('d')
        time.sleep(1)
        pydirectinput.keyUp('d')

