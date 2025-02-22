from PIL import ImageGrab
from ocr import how_much
import numpy as np
import time
import keyboard as kb


def resource_amounts(gold_bbox, elixir_bbox):
    gold_pic = np.array(ImageGrab.grab(bbox=gold_bbox))
    elixir_pic = np.array(ImageGrab.grab(bbox=elixir_bbox))
    return {"gold": how_much(gold_pic),
            "elixir": how_much(elixir_pic)}


def get_max(gold_max_bbox, elixir_max_bbox):
    kb.press_and_release("m")
    time.sleep(0.5)
    gold_pic = np.array(ImageGrab.grab(bbox=gold_max_bbox))
    kb.press_and_release("m")
    time.sleep(0.5)

    kb.press_and_release("n")
    time.sleep(0.5)
    elixir_pic = np.array(ImageGrab.grab(bbox=elixir_max_bbox))
    kb.press_and_release("n")
    time.sleep(0.5)

    det_gold_max_string = how_much(gold_pic, False)
    det_elixir_max_string = how_much(elixir_pic, False)
    gold_max = "".join(c for c in det_gold_max_string if c.isdigit())
    elixir_max = "".join(c for c in det_elixir_max_string if c.isdigit())

    return int(gold_max), int(elixir_max)


def match(log=False):
    kb.press_and_release("space")
    time.sleep(0.5)
    kb.press_and_release("q")
    time.sleep(6.5)


def zoom_out(log=False):
    kb.press("down")
    time.sleep(1)
    kb.release("down")
    time.sleep(0.5)


def deploy_troops(log=False):
    for i in range(1, 11):
        kb.press_and_release(f"{i % 10}")
        time.sleep(0.2)
        kb.press_and_release(f"f{i}")
        time.sleep(0.2)
    kb.press_and_release("-")
    time.sleep(0.2)
    kb.press_and_release("=")
    time.sleep(1.2)


def close_game(log=False):
    kb.press_and_release("ctrl+shift+5")
    time.sleep(1.2)
    kb.press("up")
    time.sleep(0.5)
    kb.release("up")
    time.sleep(1.2)


def open_game(log=False):
    kb.press_and_release("q")
    time.sleep(7)


def collect_elixir_cart(log=False):
    kb.press_and_release("p")
    time.sleep(0.5)
    kb.press_and_release("9")
    time.sleep(0.5)
    kb.press_and_release("l")
    time.sleep(1.5)


def warn(sec):
    print(f"Executing in {sec}", end=" ")
    time.sleep(1)
    for i in range(sec-1, 0, -1):
        print(i, end=" ")
        time.sleep(1)
    print()


def correct_ocr_misdetection(old_number: int, new_number: int) -> int:
    if old_number is not None and new_number - old_number > 30000:
        old_upper = (old_number // 100000) * 100000  # Extract upper digits (hundred thousands and above)
        new_lower = new_number % 100000  # Extract lower five digits

        # Check if a carry occurred in the hundred thousands digit:
        if new_number % 100000 < old_number % 100000:
            # Correct by increasing the upper part by 100,000
            corrected_upper = old_upper + 100000
        else:
            # Keep the old upper part
            corrected_upper = old_upper

        return corrected_upper + new_lower
    else:
        return new_number
