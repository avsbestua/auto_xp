import easyocr, time, keyboard, threading, logging
from PIL import ImageGrab
import pyautogui as pg
from pynput.mouse import Button, Controller
from pynput import keyboard as kb

m = Controller()
time.sleep(1)
reader = easyocr.Reader(['en'])

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def main():
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

            if text >= 16:

                keyboard.press_and_release('m')

                time.sleep(1)

                m.position = 1032, 374
                m.click(Button.left)
                #pg.click(1032, 374)

                time.sleep(1.2)

                m.position = 962, 302
                m.click(Button.left)
                #pg.click(962, 302)

                time.sleep(0.5)

                keyboard.press_and_release('esc')

                time.sleep(0.2)

def on_press(key):
    try:
        logging.info(key.char)
    except AttributeError:
        logging.info(key)

threading.Thread(target=main, daemon=True).start()

listener = kb.Listener(on_press=on_press)
listener.start()