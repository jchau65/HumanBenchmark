import pyautogui
import mss
import time

# gets a screenshot of the area needed
def get_screenshot():
    with mss.mss() as sct:
        monitor = {"top": 325, "left": 850, "width": 251, "height": 251}
        return sct.grab(monitor)
# initial variables
totalCounter = 1
flashedCounter = 0
clickedCounter = 0
clicked = 0
sequence = []
lock = True

while True:
    # gets the screenshot of the area
    screenshot = get_screenshot()

    # to be executed when target is done being shown
    if lock == False:
        # finds the flashed square
        if screenshot.pixel(1, 1)[0] == 255:
            if flashedCounter < totalCounter:
                sequence.append(1)
                flashedCounter += 1
                lock = True
            print(sequence)
            print("Clicked: " + str(clickedCounter))
            print("Flashed: " + str(flashedCounter))
        elif screenshot.pixel(125, 0)[0] == 255:
            if flashedCounter < totalCounter:
                sequence.append(2)
                flashedCounter += 1
                lock = True
            print(sequence)
            print("Clicked: " + str(clickedCounter))
            print("Flashed: " + str(flashedCounter))
        elif screenshot.pixel(250, 0)[0] == 255:
            if flashedCounter < totalCounter:
                sequence.append(3)
                flashedCounter += 1
                lock = True
            print(sequence)
            print("Clicked: " + str(clickedCounter))
            print("Flashed: " + str(flashedCounter))
        elif screenshot.pixel(0, 125)[0] == 255:
            if flashedCounter < totalCounter:
                sequence.append(4)
                flashedCounter += 1
                lock = True
            print(sequence)
            print("Clicked: " + str(clickedCounter))
            print("Flashed: " + str(flashedCounter))
        elif screenshot.pixel(125, 125)[0] == 255:
            if flashedCounter < totalCounter:
                sequence.append(5)
                flashedCounter += 1
                lock = True
            print(sequence)
            print("Clicked: " + str(clickedCounter))
            print("Flashed: " + str(flashedCounter))
        elif screenshot.pixel(250, 125)[0] == 255:
            if flashedCounter < totalCounter:
                sequence.append(6)
                flashedCounter += 1
                lock = True
            print(sequence)
            print("Clicked: " + str(clickedCounter))
            print("Flashed: " + str(flashedCounter))
        elif screenshot.pixel(0, 250)[0] == 255:
            if flashedCounter < totalCounter:
                sequence.append(7)
                flashedCounter += 1
                lock = True
            print(sequence)
            print("Clicked: " + str(clickedCounter))
            print("Flashed: " + str(flashedCounter))
        elif screenshot.pixel(125, 250)[0] == 255:
            if flashedCounter < totalCounter:
                sequence.append(8)
                flashedCounter += 1
                lock = True
            print(sequence)
            print("Clicked: " + str(clickedCounter))
            print("Flashed: " + str(flashedCounter))
        elif screenshot.pixel(250, 250)[0] == 255:
            if flashedCounter < totalCounter:
                sequence.append(9)
                flashedCounter += 1
                lock = True
            print(sequence)
            print("Clicked: " + str(clickedCounter))
            print("Flashed: " + str(flashedCounter))

    # to be executed when the target is not yet done being shown
    else:
        # starts the loop
        if len(sequence) == 0:
            if screenshot.pixel(0, 0)[0] == 37:
                lock = False

        # clicks the sequence when the sequence is done being flashed
        elif flashedCounter == totalCounter and clickedCounter < totalCounter:
            time.sleep(0.5)
            for num in sequence:
                if num == 1:
                    x = 0
                    y = 0
                if num == 2:
                    x = 125
                    y = 0
                if num == 3:
                    x = 250
                    y = 0
                if num == 4:
                    x = 0
                    y = 125
                if num == 5:
                    x = 125
                    y = 125
                if num == 6:
                    x = 250
                    y = 125
                if num == 7:
                    x = 0
                    y = 250
                if num == 8:
                    x = 125
                    y = 250
                if num == 9:
                    x = 250
                    y = 250
                pyautogui.click(850 + x, 325 + y)
                clickedCounter += 1

        # detects when the target is done being shown
        else:
            if sequence[-1] == 1:
                if screenshot.pixel(0, 0)[0] == 37:
                    lock = False
                    if clickedCounter == totalCounter:
                        totalCounter += 1
                        clickedCounter = 0
                        flashedCounter = 0
                        sequence = []
                        lock = False
            elif sequence[-1] == 2:
                if screenshot.pixel(125, 0)[0] == 37:
                    lock = False
                    if clickedCounter == totalCounter:
                        totalCounter += 1
                        clickedCounter = 0
                        flashedCounter = 0
                        sequence = []
                        lock = False
            elif sequence[-1] == 3:
                if screenshot.pixel(250, 0)[0] == 37:
                    lock = False
                    if clickedCounter == totalCounter:
                        totalCounter += 1
                        clickedCounter = 0
                        flashedCounter = 0
                        sequence = []
                        lock = False
            elif sequence[-1] == 4:
                if screenshot.pixel(0, 125)[0] == 37:
                    lock = False
                    if clickedCounter == totalCounter:
                        totalCounter += 1
                        clickedCounter = 0
                        flashedCounter = 0
                        sequence = []
                        lock = False
            elif sequence[-1] == 5:
                if screenshot.pixel(125, 125)[0] == 37:
                    lock = False
                    if clickedCounter == totalCounter:
                        totalCounter += 1
                        clickedCounter = 0
                        flashedCounter = 0
                        sequence = []
                        lock = False
            elif sequence[-1] == 6:
                if screenshot.pixel(250, 125)[0] == 37:
                    lock = False
                    if clickedCounter == totalCounter:
                        totalCounter += 1
                        clickedCounter = 0
                        flashedCounter = 0
                        sequence = []
                        lock = False
            elif sequence[-1] == 7:
                if screenshot.pixel(0, 250)[0] == 37:
                    lock = False
                    if clickedCounter == totalCounter:
                        totalCounter += 1
                        clickedCounter = 0
                        flashedCounter = 0
                        sequence = []
                        lock = False
            elif sequence[-1] == 8:
                if screenshot.pixel(125, 250)[0] == 37:
                    lock = False
                    if clickedCounter == totalCounter:
                        totalCounter += 1
                        clickedCounter = 0
                        flashedCounter = 0
                        sequence = []
                        lock = False
            elif sequence[-1] == 9:
                if screenshot.pixel(250, 250)[0] == 37:
                    lock = False
                    if clickedCounter == totalCounter:
                        totalCounter += 1
                        clickedCounter = 0
                        flashedCounter = 0
                        sequence = []
                        lock = False