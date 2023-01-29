import pyautogui as pg
import time
import webbrowser
# while True:
#     time.sleep(4)
#     pyautogui.typewrite('Hello! Motherfu**ing :D')
#     time.sleep(2)
#     pyautogui.press('enter')

# time.sleep(2)
# print(pg.position())
# pg.moveTo(562, 755, 2)
# pg.leftClick()

url = "https://www.facebook.com/messages/t/100017290625742"
webbrowser.get().open(url)
print(pg.position())
# pg.moveTo(970, 1079, 2)
# pg.moveTo(1026, 1052, 2)
# pg.leftClick(1026, 1052, 1)
# pg.keyDown('ctrl')
# pg.press('t')
# pg.keyUp('ctrl')
#     pg.moveTo(661, 479)
#     pg.leftClick()
#     pg.typewrite("hello bạn")
#     pg.press('enter')
time.sleep(10)

for i in range(6):
    pg.keyDown('alt')
    for j in range(i):
        pg.press('tab')
    pg.press('enter')
    pg.keyUp('alt')
    pg.moveTo(959, 1026)
    pg.leftClick()
    pg.typewrite("hello bạn")
    pg.press('enter')
    #pg.hotkey('alt', 'tab', 'enter')
