import pyautogui
import mss
import time

# minimizes reaction time
pyautogui.PAUSE = 0

# gets pixel color at x, y
def get_pixel_color(x,y):
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": 1, "height": 1}
        screenshot = sct.grab(monitor)
        return screenshot.pixel(0, 0)

while True:
    pixel_color = get_pixel_color(500, 500)

    # clicks on the screen when pixel color changes to green and then clicks the screen again to start the next test
    if pixel_color[0] == 75:
        pyautogui.click(500, 500)
        time.sleep(1)
        pyautogui.click(500, 500)
