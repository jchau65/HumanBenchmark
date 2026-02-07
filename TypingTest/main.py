import cv2
import mss
import numpy as np
import pyautogui
import pytesseract as ocr
import time

# preprocessing variables
resize = 4
morphOpen = 2
medianBlur = 3

# path to tesseract executable
ocr.pytesseract.tesseract_cmd = r'C:\Users\jacki\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# gets text from screenshot using OCR
def get_text(x, y, width, height):
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
        config = '--psm 6 -c tessedit_char_blacklist=|'

        # print out OCR results
        return ocr.image_to_string(smooth, config=config).strip()

# sets pyautogui to click as fast as possible
pyautogui.PAUSE = 0
pyautogui.MINIMUM_DURATION = 0

# moves the mouse to the correct window
pyautogui.moveTo(493, 413)

# gets the text
text = get_text(493, 403, 950, 200)

# removes double spaces and newlines from the text
editedText = " ".join(text.split())

# clicks to focus the typing box
pyautogui.click()

# waits 0.5 seconds because pyautogui is stupid
time.sleep(0.5)

# types
pyautogui.write(editedText)