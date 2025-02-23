from PIL import ImageGrab
from ocr import how_much
import numpy as np
import time
import keyboard as kb
import sys


def resource_amounts(gold_bbox, elixir_bbox):
    gold_pic = np.array(ImageGrab.grab(bbox=gold_bbox))
    elixir_pic = np.array(ImageGrab.grab(bbox=elixir_bbox))
    return {"gold": how_much(gold_pic),
            "elixir": how_much(elixir_pic)}


def get_max(gold_max_bbox, elixir_max_bbox):
    kb.press_and_release("m")
    time.sleep(0.5)
    gold_pic = np.array(ImageGrab.grab(bbox=gold_max_bbox))
    time.sleep(0.5)
    kb.press_and_release("m")
    time.sleep(0.5)

    kb.press_and_release("n")
    time.sleep(0.5)
    elixir_pic = np.array(ImageGrab.grab(bbox=elixir_max_bbox))
    time.sleep(0.5)
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
    time.sleep(2)


def countdown(sec, prefix):
    print(f"{prefix} {sec}", end=" ")
    time.sleep(1)
    for i in range(sec-1, 0, -1):
        print(i, end=" ")
        time.sleep(1)
    print()


def correct_ocr_misdetection(old_number: int, new_number: int) -> int:
    if old_number \
            and (new_number - old_number > 30000 or new_number - old_number < -30000):
        old_upper = (old_number // 100000) * 100000  # Extract upper digits (hundred thousands and above)
        new_lower = new_number % 100000  # Extract lower five digits

        # Check if a carry occurred in the hundred thousands digit:
        if new_number % 100000 < old_number % 100000:
            # Correct by increasing the upper part by 100,000
            corrected_upper = old_upper + 100000
        else:
            # Keep the old upper part
            corrected_upper = old_upper
        corrected_number = corrected_upper + new_lower
        if corrected_number - old_number > 100000:
            return corrected_number - 100000
        else:
            return corrected_number
    else:
        return new_number


def print_gold_table(current_gold, gold_target, gold_per_10min, time_left):
    # Define the header and separator
    headers = ["Gold", "Target", "Per10m", "TimeLeft"]
    widths = [10, 10, 10, 10]  # Define consistent widths for all columns

    # Unicode box-drawing characters
    top_left = "┌"
    top_right = "┐"
    bottom_left = "└"
    bottom_right = "┘"
    horizontal = "─"
    vertical = "│"
    top_joint = "┬"
    middle_joint = "┼"
    bottom_joint = "┴"
    side_joint = "├"
    side_joint_right = "┤"

    # Embed headers directly into the frame
    header_row = top_left + top_joint.join(
        f"{header:^{width}}".replace(" ", horizontal)
        for header, width in zip(headers, widths)
    ) + top_right

    # Format data row
    data_row = vertical + vertical.join(
        f"{str(value):^{width}}"
        for value, width in zip([current_gold, gold_target, gold_per_10min, time_left], widths)
    ) + vertical

    # Bottom row
    bottom_row = bottom_left + bottom_joint.join(f"{horizontal * width}" for width in widths) + bottom_right

    # Print the formatted table with embedded headers
    print(header_row)
    print(data_row)
    print(bottom_row)


def convert_seconds_to_hm(seconds):
    """Convert seconds to a string in '{hours}h {minutes}m' format.

    Any leftover seconds cause an extra minute to be added. The minutes are
    adjusted to account for any overflow into an additional hour.

    Leading zero hours are omitted.

    Examples:
      3661 -> "1h 2m"   (3661 seconds is 1 hour, 1 minute, and 1 second, rounding up minutes to 2)
      3600 -> "1h 0m"   (exactly one hour)
      59   -> "1m"      (59 seconds rounds up to 1 minute)
      0    -> "0m"      (zero seconds)
    """
    hours = seconds // 3600
    remainder = seconds % 3600
    minutes = remainder // 60
    extra_seconds = remainder % 60

    # If there are any remaining seconds, round up by adding one minute.
    if extra_seconds > 0:
        minutes += 1

    # Adjust if minutes roll over to an additional hour.
    if minutes == 60:
        hours += 1
        minutes = 0

    # Build output string, omitting leading zero hours.
    if hours:
        return f"{hours}h {minutes}m"
    else:
        return f"{minutes}m"


def clear_above_n_lines(lines):
    for _ in range(lines):
        sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


if __name__ == "__main__":
    ImageGrab.grab(bbox=(1626, 278, 1875, 303)).show()