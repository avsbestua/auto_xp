import easyocr, time, keyboard
from PIL import ImageGrab
import pyautogui as pg

time.sleep(1)
reader = easyocr.Reader(['en'])

while True:
    img = ImageGrab.grab(bbox=(930, 885, 989, 927))
    img.save("Image.png")
    p_text = reader.readtext("Image.png", detail=0)
    if p_text and len(p_text) == 1:

        try:
            text = ''.join(p_text)
            text = int(text)
        except ValueError:
            continue

        if text >= 15:

            keyboard.press_and_release('m')

            time.sleep(0.8)

            pg.click(1032, 374)

            time.sleep(0.9)

            pg.click(962, 302)

            time.sleep(0.7)

            keyboard.press_and_release('esc')

            time.sleep(0.2)