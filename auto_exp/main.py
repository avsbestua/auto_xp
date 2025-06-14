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

            time.sleep(0.8)

            ms.position = (1032, 374)
            ms.click(Button.left)

            time.sleep(0.8)

            ms.position = (962, 302)
            ms.click(Button.left)

            time.sleep(0.7)

            kb.press(Key.esc)
            kb.release(Key.esc)

            time.sleep(0.2)