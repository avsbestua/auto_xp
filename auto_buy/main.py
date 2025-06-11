import pyautogui as pg
from pynput.keyboard import Controller, Key
import pytesseract, time
from PIL import ImageGrab

def price(image):
    red = pytesseract.image_to_string(image, 'rus+ukr')

    for line in red.splitlines():
        if "Цена" in line:
            kuski = line.split("$")

            kuski = line.split("Цена")

            price = int(kuski[-1].strip().replace(',', ''))

            return price

ah_update = lambda: pg.click(959,579)

k = Controller()
pg.FAILSAFE = True
target_price = 1500000
pytesseract.pytesseract.tesseract_cmd = r'D:\download\teseract\tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

time.sleep(3)

k.press(']')
k.release(']')

while True:
    try:
        location = pg.locateOnScreen("yayko.png", region=(636, 139, 1287, 517), confidence=0.85)
        yayko_pos = pg.center(location)
        pg.moveTo(yayko_pos)
        x,y = pg.position()

        y1 = y + 80
        x1 = x

        x2 = x + 654
        y2 = y - 80

        bbox = (x1, y1, x2, y2)

        img = ImageGrab.grab(bbox=bbox)
        img.save("ah.png")

        if price("ah.png") <= target_price:
            k.press(Key.shift)
            pg.click(yayko_pos)
            break

    except: ah_update()
