from time import sleep
import pyautogui
import mss
import pytesseract as ocr
import math
import cv2
import numpy as np

resize = 0.75
medianBlur = 1
morphOpen = 2

# path to tesseract executable
ocr.pytesseract.tesseract_cmd = r'C:\Users\jacki\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# gets number from screenshot using OCR
def get_number(x, y, width, height):
    with mss.mss() as sct:
        # define area on monitor to screenshot
        monitor = {"top": y, "left": x, "width": width, "height": height}
        screenshot = sct.grab(monitor)

        # convert image into a readable format for cv2
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        # resize image for OCR inputs
        image = cv2.resize(img, None, fx=resize, fy=resize, interpolation=cv2.INTER_CUBIC)

        # convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # run a threshold on the image and convert it to binary
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

        # apply a median blur for smoothening the digit
        # thresh = cv2.medianBlur(thresh, medianBlur)

        # rebinarize and threshold the image
        thresh = cv2.threshold(thresh, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

        # invert image
        thresh = cv2.bitwise_not(thresh)

        # close open holes
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (morphOpen, morphOpen))
        clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
        clean = cv2.dilate(clean, kernel, iterations=1)

        # invert image again
        clean = cv2.bitwise_not(clean)

        # rebinarize and threshold the image
        _, smooth = cv2.threshold(clean, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # OCR config to make it read a single line of text and also so it only reads digits
        config = '--psm 7 -c tessedit_char_whitelist=0123456789'

        # print out OCR results
        return ocr.image_to_string(smooth, config=config)

# gets the color foe a pixel at the designated spot
def get_pixel(x, y):
    with mss.mss() as sct:
        # define 1x1 screenshot as pixel
        monitor = {"top": y, "left": x, "width": 1, "height": 1}
        img = sct.grab(monitor)
        return img.pixel(0, 0)

if get_pixel(907, 573)[2] == 84:
    pyautogui.click(907, 573)

# storage for all the locations of the squares on screen
xcoords = []
ycoords = []

# calculates all the locations of the squares on screen
for x in range(8):
    xcoords.append(math.floor(619 + (x * (629/7))))
for y in range(5):
    ycoords.append(math.floor(208 + (y * (358/4))))

# storage for the positions of the squares and their numbers
positions = []

# number that the program is going to click next
num = 1

while True:
    # reads all the numbers and finds their positions on the screen
    for x in xcoords:
        for y in ycoords:
            # gets the number located at the square
            number = get_number(x, y, 80, 80)

            if str(number) != "":
                # adds the number in the correct order
                if len(positions) == 0:
                    positions.append([int(number), x, y])
                else:
                    inserted = False
                    index = 0
                    for position in positions:
                        if position[0] > int(number):
                            positions.insert(index, [int(number), x, y])
                            inserted = True
                            break
                        else:
                            index += 1
                    if not inserted:
                        positions.append([int(number), x, y])

    # debugging
    print(positions)

    # checks to see if all squares are found in order, if not throw an error
    for position in positions:
        if position[0] == num:
            num += 1
        else:
            raise Exception("Number " + str(num) + " not found")

    # clicks all the positions
    for position in positions:
        pyautogui.click(position[1] + 40, position[2] + 40)

    # resets the positions and number
    positions = []
    num = 1

    # waits until the game is ready before moving on to the next stage
    while True:
        if get_pixel(912, 553)[2] != 84:
            sleep(0.1)
        else:
            pyautogui.click(912, 553)
            break