from easyocr import Reader

print("Initializing OCR Engine...")
reader = Reader(['en'])
print("OCR Engine Initialized.")


def ocr(im, allowlist=None):
    if allowlist:
        result = reader.readtext(im, allowlist=allowlist)
    else:
        result = reader.readtext(im)
    return result


def how_much(im, numbers_only=True):
    if numbers_only:
        return int(ocr(im, "0123456789")[0][1])
    else:
        return ocr(im)[0][1]