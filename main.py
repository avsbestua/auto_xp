import easyocr, time
from PIL import ImageGrab
from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Controller as MouseController, Button


kb = KeyboardController()
ms = MouseController()
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

            kb.press('m')
            kb.release('m')

            time.sleep(0.2)

            ms.position = (890, 380)
            ms.click(Button.left)

            time.sleep(0.2)

            ms.position = (960, 310)
            ms.click(Button.left)