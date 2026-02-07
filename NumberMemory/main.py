from PIL import Image, ImageOps, ImageEnhance
import pyautogui
import pytesseract as ocr
import mss
import time

# path to tesseract executable
ocr.pytesseract.tesseract_cmd = r'C:\Users\jacki\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# gets number from screenshot using OCR
def get_text():
    with mss.mss() as sct:
        # define area on monitor to screenshot
        monitor = {"top": 200, "left": 460, "width": 1040, "height":470}
        screenshot = sct.grab(monitor)

        # convert mss image to raw data
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")

        #resize image to be smaller for OCR to work because it's dumb sometimes
        new_size = (int(img.width * 0.5), int(img.height * 0.5))
        new_img = img.resize(new_size, Image.LANCZOS)

        # convert image to greyscale
        new_img = ImageOps.grayscale(new_img)

        # enhance the image
        new_img = ImageEnhance.Contrast(new_img).enhance(2.0)

        # convert to binary and invert
        new_img = new_img.point(lambda p:255 if p > 150 else 0)
        new_img = ImageOps.invert(new_img)

        # configure tesseract for only numbers
        config = '--psm 6 -c tessedit_char_whitelist=0123456789'

        # print out OCR results
        return ocr.image_to_string(new_img, config=config).strip().replace("\n", "")

# gets the color fo a pixel at the designated spot
def get_pixel(x, y):
    with mss.mss() as sct:
        # define 1x1 screenshot as pixel
        monitor = {"top": y, "left": x, "width": 1, "height": 1}
        img = sct.grab(monitor)
        return img.pixel(0, 0)

while True:
    # clicks the yellow button to start or to move on to the next level
    pyautogui.click(931, 573)
    time.sleep(0.5)

    # gets the number shown on screen
    num = get_text()
    print(num) # debug

    # stops the program while the text box to type the number in has not been shown
    while get_pixel(500, 400)[0] != 34:
        time.sleep(0.1)

    # types the number into the text box
    pyautogui.write(num)
    time.sleep(0.1)

    # clicks submit
    pyautogui.click(922, 507)
    time.sleep(0.5)

    # stops the program until the next level button has appeared and is able to be clicked
    while get_pixel(931, 573)[0] != 43:
        time.sleep(0.1)
