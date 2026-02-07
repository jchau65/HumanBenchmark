from PIL import Image, ImageOps, ImageEnhance
import pyautogui
import pytesseract as ocr
import mss

# path to tesseract executable
ocr.pytesseract.tesseract_cmd = r'C:\Users\jacki\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# gets text from screenshot using OCR
def get_text():
    with mss.mss() as sct:
        # define area on monitor to screenshot
        monitor = {"top": 375, "left": 475, "width": 1000, "height":85}
        screenshot = sct.grab(monitor)

        # convert mss image to raw data
        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")

        #resize image to be smaller for OCR to work because it's dumb sometimes
        resize_amount = 1
        new_size = (int(img.width * resize_amount), int(img.height * resize_amount))
        new_img = img.resize(new_size, Image.LANCZOS)

        # convert image to greyscale
        new_img = ImageOps.grayscale(new_img)

        # enhance the image
        new_img = ImageEnhance.Contrast(new_img).enhance(2.0)

        # convert to binary and invert
        new_img = new_img.point(lambda p:255 if p > 150 else 0)
        new_img = ImageOps.invert(new_img)

        # configure tesseract
        config = '--psm 6'

        # print out OCR results
        return ocr.image_to_string(new_img).strip().replace("\n", "")

# finds the text within an array using a basicas linear search
def find(array, texttofind):
    for txt in array:
        if txt == texttofind:
            return True
    return False

storage = []
while True:
    text = get_text()

    # if text is not found in storage, click "SEEN"
    if find(storage, text):
        pyautogui.click(900, 500)

    # if text is found in storage, click "NEW"
    else:
        storage.append(text)
        pyautogui.click(1000, 500)

