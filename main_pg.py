import easyocr, time, keyboard, threading, logging, win32api, win32con
from PIL import ImageGrab
from pynput.mouse import Button, Controller, Listener
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

                win32api.SetCursorPos((1032, 374))

                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.05)  # коротка пауза
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

                #pg.click(1032, 374)

                time.sleep(1.2)

                win32api.SetCursorPos((962, 302))

                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.05)  # коротка пауза
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

                #pg.click(962, 302)

                time.sleep(0.5)

                keyboard.press_and_release('esc')

                time.sleep(0.2)

def on_press(key):
    try:
        logging.info(key.char)
    except AttributeError:
        logging.info(key)

def on_click(x, y, button, pressed):
    logging.info(f"Pressed {button}")

threading.Thread(target=main, daemon=True).start()

listener = kb.Listener(on_press=on_press)
listener.start()

mouse_listener = Listener(on_click=on_click)
mouse_listener.start()

listener.join()