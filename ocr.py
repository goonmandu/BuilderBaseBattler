'''
from easyocr import Reader

print("Initializing OCR Engine...")
reader = Reader(['en'])
print("OCR Engine Initialized.")


def ocr(im):
    result = reader.readtext(im, allowlist ='0123456789')
    return result


def how_much(im):
    return int(ocr(im)[0][1])
'''