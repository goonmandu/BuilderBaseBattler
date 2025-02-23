# BuilderBaseBattler
Automatically does Builder Base battles for you in Clash of Clans.

The BlueStacks keymap configuration file for this script is also provided: `bbb.cfg`.

# DISCLAIMER
**This script is against Supercell's Terms of Service**:<br>
[Update to Our Fair Play Policy and Next Steps](https://supercell.com/en/games/clashofclans/blog/misc/update-to-our-fair-play-policy-and-next-steps/)

**Use at your own risk.**

# Usage
## BlueStacks configuration
### Clash of Clans keymap configuration
Provided in `bbb.cfg`.
### Apps list:
Add a Tap shortcut with key `Q` on the Clash of Clans app icon.

![image](https://github.com/user-attachments/assets/4d403128-cc81-4280-8cb6-ceceaef54315)
### Recent apps/multitasking slider (Ctrl Shift 5):
Add a Swipe shortcut with its default keymaps on the center of the BlueStacks window.

![image](https://github.com/user-attachments/assets/d093d441-b6ac-49a4-b081-a105e18474db)

### Bounding Boxes for OCR (optional)
Refer to [Issue #1](https://github.com/goonmandu/BuilderBaseBattler/issues/1#issuecomment-2677164382).

## Command Line
1. `pip3 install -r requirements.txt`
2. `python3 main.py`

When the script asks you whether you want to use automatic stopping:
- If you answer "Y" without setting up the bounding boxes, the script will terminate.
- If you answer "N", the script will indefinitely spam builder base attacks until you stop it manually.

This is what automatic stopping looks like.

![image](https://github.com/user-attachments/assets/b22cdb6d-dc2e-46d9-b5ca-97f3924a753f)
