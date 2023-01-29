import pyautogui as pg
import time
import random


def on_click(image, x1=0, y1=0, x2=0, y2=0):
    try:
        if (x1+y1+x2+y2 == 0):
            loc = pg.locateOnScreen('./img/'+image)
        else:
            xx1 = random.randint(x1, x2)
            yy1 = random.randint(y1, y2)
            xx2 = random.randint(xx1, x2)
            yy2 = random.randint(yy1, y2)
            loc = pg.locateOnScreen(
                './img/'+image, region=(xx1, yy1, xx2, yy2))
        button1 = pg.center(loc)
        pg.moveTo(button1.x, button1.y)
        pg.click()
        return 1
    except:
        return 0


def run_main():
    try:
        sl = int(input('Nhập số lần bạn muốn click: '))
    except:
        sl = 10
    print('Waiting...')
    time.sleep(2)
    print("Running...")
    on_click('lose.png')
    on_click('start.png')

    loc = pg.locateOnScreen('./img/top.png')
    if (loc is None):
        print('ERROR BOARD')
        return
    i = 0
    er = 0
    while i < sl:
        if (on_click("square1.png", loc[0], loc[1], loc[0]+loc[2], loc[1]+loc[3]) == 1):
            i += 1
            er = 0
        else:
            er += 1
            if (er > 10):
                print("ERROR square")
                break
        if (on_click('lose.png') == 1):
            i = 0


if __name__ == '__main__':
    run_main()
