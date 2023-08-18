import os
import pyautogui
import time
from dotenv import load_dotenv


def login(image_name: str, num_attempts: int) -> None:
    if num_attempts < 6:
        tap_to_start_loc = pyautogui.locateOnScreen(f'{image_name}', region=(175, 815, 210, 50), confidence=0.8)
        if tap_to_start_loc is not None:
            print("Logging in")
            buttonLocation = pyautogui.center(tap_to_start_loc)
            pyautogui.click(buttonLocation[0], buttonLocation[1])
        else:
            print("I am unable to see it, trying again")
            time.sleep(0.5)
            login(image_name, num_attempts+1)
    else:
        print("was unable to find the 'TAP TO START' text")


def collect_daily_reward() -> None:
    return True


def open_character():
    return True


load_dotenv()
login(os.environ['LOGIN_IMAGE'], 0)