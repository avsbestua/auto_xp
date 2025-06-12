import keyboard
import pyautogui as pg
from pynput.keyboard import Controller, Key
import pytesseract, time
from PIL import ImageGrab

def price(image):
    red = pytesseract.image_to_string(image, 'rus+ukr')

    for line in red.splitlines():
        if "Цена" in line:

            kuski = line.split()

            price = int(kuski[-1].strip().replace(',', ''))

            return price

ah_update = lambda: pg.click(959,579)

k = Controller()
pg.FAILSAFE = True
target_price = 1500000
#pytesseract.pytesseract.tesseract_cmd = r'D:\download\teseract\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(3)

k.press(']')
k.release(']')

while True:
    try:
        location = pg.locateOnScreen("yayko.png", region=(636, 139, 1287, 517), confidence=0.85)
    except:
        ah_update()
        continue

    yayko_pos = pg.center(location)
    print("find")
    pg.moveTo(yayko_pos)
    x,y = pg.position()

    x2 = x + 600
    y2 = y + 350

    bbox = (x, y-120, x2, y2)

    img = ImageGrab.grab(bbox=bbox)

    price = price(img)
    print(price)

    if price <= target_price:
        #k.press(Key.shift)
        keyboard.press('shift')
        pg.click(yayko_pos)
        break


