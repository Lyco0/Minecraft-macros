import pydirectinput
import time
import math
import pyautogui

def move_mouse(degree):
    screen_width, screen_height = pyautogui.size()

    target_x = int(screen_width * (degree / 360))

    pyautogui.moveTo(target_x, pyautogui.position().y, duration = 0.5)


pydirectinput.keyDown('alt')
pydirectinput.press('tab')
pydirectinput.press('tab')
pydirectinput.keyUp('alt')
pydirectinput.press('e')
move_mouse(8.7)
