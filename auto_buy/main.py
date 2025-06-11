import pyautogui as pg
from pynput.keyboard import Controller, Key
import pytesseract

k = Controller()
image = "zhydak.png"
#pytesseract.pytesseract.tesseract_cmd = r'D:\download\teseract\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

red = pytesseract.image_to_string(image, 'rus+ukr')
for line in red.splitlines():
    if "Цена" in line:
        kuski = line.split("$")

        price = int(kuski[-1].strip().replace(',', ''))
        print(price)

