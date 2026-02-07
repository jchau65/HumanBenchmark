import math
import mss
import pyautogui
import time

# gets number from screenshot using OCR
def get_dimensions(x, y, width, height):
    with mss.mss() as sct:
        # define area on monitor to screenshot
        monitor = {"top": y, "left": x, "width": width, "height": height}
        screenshot = sct.grab(monitor)

        rows = 1
        col = 1
        lock = False

        for x in range(width):
            if screenshot.pixel(x, 1)[0] == 43 and lock == False:
                rows += 1
                lock = True
            elif screenshot.pixel(x, 1)[0] == 255 and lock == True:
                lock = False
            elif screenshot.pixel(x, 1)[0] == 37 and lock == True:
                lock = False

        lock = False

        for y in range(height):
            if screenshot.pixel(1, y)[0] == 43 and lock == False:
                col += 1
                lock = True
            elif screenshot.pixel(1, y)[0] == 255 and lock == True:
                lock = False
            elif screenshot.pixel(1, y)[0] == 37 and lock == True:
                lock = False

        print(str(rows) + ", " + str(col))
        lock = False
        list = []

        for x in range(rows):
            for y in range(col):
                if screenshot.pixel(math.floor((width - 1) / (rows - 1) * x), math.floor((height - 1) / (col - 1) * y))[0] == 255:
                    list.append([math.floor((width - 1) / (rows - 1) * x), math.floor((height - 1) / (col - 1) * y)])

        return list

pyautogui.MINIMUM_DURATION = 0
pyautogui.PAUSE = 0

pyautogui.click(925, 546)
time.sleep(0.75)
while True:
    positions = get_dimensions(790, 280, 365, 365)
    time.sleep(1.5)
    for position in positions:
        pyautogui.click(position[0] + 790, position[1] + 280)
    time.sleep(2)