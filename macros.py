# from PIL import Image, ImageGrab
# from ocr import how_much
# import numpy as np
import time
import keyboard as kb

'''
def print_resources(max_gold, max_elixir):
    gold_pic = np.array(ImageGrab.grab(bbox=(1629, 93, 1805, 125)))
    elixir_pic = np.array(ImageGrab.grab(bbox=(1629, 195, 1805, 229)))

    gold = how_much(gold_pic)
    elixir = how_much(elixir_pic)

    print(f"Gold:   {gold} / {max_gold} ", end="")
    if gold > max_gold * 0.9:
        print(f"Gold storage is almost full!", end="")
    print()
    print(f"Elixir: {elixir} / {max_elixir} ", end="")
    if elixir > max_elixir * 0.9:
        print(f"Elixir storage is almost full!")
    print("\n")
'''


def match(log=False):
    kb.press_and_release("space")
    time.sleep(0.5)
    kb.press_and_release("q")
    time.sleep(8)


def setup(log=False):
    kb.press("down")
    time.sleep(2)
    kb.release("down")
    time.sleep(1)


def spam(log=False):
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
    time.sleep(2)
    kb.press("up")
    time.sleep(0.5)
    kb.release("up")
    time.sleep(2)


def open_game(log=False):
    kb.press_and_release("q")
    time.sleep(10)


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
