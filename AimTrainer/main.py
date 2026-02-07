import pyautogui
import mss

# finds the target and clicks on it
def find_target():
    with mss.mss() as sct:
        # define area to be captured and look for targets
        monitor = {"top": 250, "left": 550, "width": 850, "height": 400}
        screenshot = sct.grab(monitor)

        # looks for target and clicks if the target is found
        if screenshot.pixel(282, 339)[2] != 84:
            for x in range(0, 850, 50):
                for y in range(0, 400, 50):
                    if screenshot.pixel(x, y)[0] != 43:
                        pyautogui.click(x + 550, y + 250)
                        break
                else:
                    continue
                break

# sets pyautogui to click as fast as possible
pyautogui.PAUSE = 0;
pyautogui.MINIMUM_DURATION = 0;

# clicks the start target
pyautogui.click(971, 424)

# clicks all the remaining targets
while True:
    find_target()