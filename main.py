from macros import *
import math
import os

gold_bbox = (1629, 93, 1805, 125)
gold_max_bbox = (1626, 175, 1875, 206)
elixir_bbox = (1629, 195, 1805, 229)
elixir_max_bbox = (1626, 278, 1875, 303)
gold_max = None
last_gold = None
current_gold = None
initial_time = time.time()
initial_gold = 0
gold_per_10min = 0
first_loop = True
first_print = True

os.system("cls")
print("BuilderBaseBattler v0.0.1\n")
stop_at = input("Stop at how much gold? Input GOLD_MAX to fill storages.\n")

if stop_at == "GOLD_MAX":
    gold_target = gold_max
else:
    gold_target = int(stop_at)

countdown(5, "Script Starting in")
while True:
    open_game()
    zoom_out()
    collect_elixir_cart()

    if not gold_target:
        dgm, dem = get_max(gold_max_bbox, elixir_max_bbox)
        gold_target = dgm
        print(f"Detected Max: {dgm} Gold, {dem} Elixir")
    if not last_gold:
        last_gold = int(input("Enter the current gold for OCR calibration.\n"))
        initial_gold = last_gold
        countdown(5, "Resuming in")
        print()

    # OCR Error Checking Logic
    if current_gold:
        last_gold = current_gold
    current_gold = resource_amounts(gold_bbox, elixir_bbox)["gold"]
    # print(f"Detected current gold: {current_gold}")
    if math.ceil(math.log10(current_gold)) > math.ceil(math.log10(gold_target)):
        current_gold = int("".join(str(current_gold)[1:]))
    if last_gold and math.ceil(math.log10(current_gold)) < math.ceil(math.log10(last_gold)):
        current_gold = int(str(last_gold)[0]) * 10**(int(math.log10(last_gold))) + current_gold
        if current_gold % 1000000 - last_gold % 1000000:
            current_gold += 1000000
    current_gold = correct_ocr_misdetection(last_gold, current_gold)
    if not first_loop:
        gold_per_second = (current_gold - initial_gold) / (time.time() - initial_time)
        gold_per_10min = str(int(gold_per_second * 600 // 1000)) + "k"
        if gold_per_second > 0:
            time_left = (gold_target - current_gold) / gold_per_second
            time_left = convert_seconds_to_hm(int(time_left))
        else:
            time_left = "∞"
        if not first_print:
            clear_above_n_lines(3)
        print_gold_table(current_gold, gold_target, gold_per_10min, time_left)
        first_print = False
    if current_gold >= gold_target:
        break
    first_loop = False

    match()
    zoom_out()
    deploy_troops()
    close_game()

print("Gold target reached; stopping script.")