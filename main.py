from macros import *
import math

gold_bbox = (1629, 93, 1805, 125)
gold_max_bbox = (1626, 175, 1875, 206)
elixir_bbox = (1629, 195, 1805, 229)
elixir_max_bbox = (1626, 274, 1875, 305)
gold_max = None
last_gold = None

stop_at = input("Stop at how much gold? Input GOLD_MAX to fill storages.\n")

if stop_at == "GOLD_MAX":
    gold_target = gold_max
else:
    gold_target = int(stop_at)

warn(5)
while True:
    open_game()
    zoom_out()
    collect_elixir_cart()

    if not gold_target:
        gold_target = get_max(gold_max_bbox, elixir_max_bbox)[0]
    if not last_gold:
        last_gold = int(input("Enter the current gold for OCR calibration.\n"))
        warn(5)
    current_gold = resource_amounts(gold_bbox, elixir_bbox)["gold"]
    if math.ceil(math.log10(current_gold)) > math.ceil(math.log10(gold_target)):
        current_gold = int("".join(str(current_gold)[1:]))
    if last_gold and math.ceil(math.log10(current_gold)) < math.ceil(math.log10(last_gold)):
        current_gold = int(str(last_gold)[0]) * 10**(int(math.log10(last_gold))) + current_gold
        if current_gold % 1000000 - last_gold % 1000000:
            current_gold += 1000000
    current_gold = correct_ocr_misdetection(last_gold, current_gold)
    print(f"Current: {current_gold}, Target: {gold_target}")
    if current_gold >= gold_target:
        break

    match()
    zoom_out()
    deploy_troops()
    close_game()

print("Gold target reached; stopping script.")