from win32.win32api import GetCursorPos, SetCursorPos
from time import sleep

while True:
    x, y = GetCursorPos()
    SetCursorPos((x+10, y+10))
    sleep(0.1)