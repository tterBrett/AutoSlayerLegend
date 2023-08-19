import os
import pyautogui
import time
from dotenv import load_dotenv
import datetime
import numpy as np


def find_n_click(image_name: str, max_num_attempts: int) -> bool:
    """
    Summary: Attempts to find a given image on the screen and clicks center of image if found
    :param image_name: file path to image being searched on screen
    :param max_num_attempts: number search attempts allowed
    :return: boolean determining if search was successful
    """
    tap_to_start_loc = pyautogui.locateOnScreen(f'{image_name}', confidence=0.85)
    current_attempts = 0
    if current_attempts < max_num_attempts:
        if tap_to_start_loc is not None:
            print(f"200 - Found image {image_name} on attempt {current_attempts}")
            button_location = pyautogui.center(tap_to_start_loc)
            pyautogui.click(button_location[0], button_location[1])
            return True
        else:
            time.sleep(0.25)
            print(f"404 - Unable to see image {image_name}. Num attempts: {current_attempts}")
            find_n_click(image_name, current_attempts + 1)
            return False
    else:
        return False


def save_afk_rewards() -> bool:
    """
    Summary: Screenshots afk rewards and saves image to track exp/hr and gold/hr
    :return: boolean determining if screenshot and save was successful
    """
    timestamp = datetime.datetime.now()
    timestamp = timestamp.strftime("%m-%d-%Y_%X").replace(":", ".")
    image = pyautogui.screenshot(region=(50, 260, 450, 480))
    image.save(f"images/afk_rewards/{timestamp}.PNG")
    return True


def activate_scrolls() -> bool:
    """
    Summary: Screenshots afk rewards and saves image to track exp/hr and gold/hr
    :return: boolean determining if the scrolls were activated fast enough
    """
    if find_n_click(os.environ['SCROLL_INTERFACE_ICON'], 3):
        daily_scrolls = [
            os.environ['GOLD_SCROLL_ICON'], os.environ['EXP_SCROLL_ICON'],
            os.environ['ENHANCE_CUBE_SCROLL_ICON'], os.environ['EQUIPMENT_SCROLL_ICON']
        ]

        scrolls_found = []
        for scroll in daily_scrolls:
            # Same operation listed twice to activate daily limit of 2
            scrolls_found.append(find_n_click(scroll, 1))
            scrolls_found.append(find_n_click(scroll, 1))

        if False in scrolls_found:
            print(f"404 - Failed to active all scrolls {scrolls_found}")
            return False
        else:
            print("200 - all scrolls have been activated")
            return True


load_dotenv()

operation_results = []
find_n_click(os.environ['LOGIN_IMAGE'], 5)
find_n_click(os.environ['CLAIM_DAILY_REWARDS'], 3)
find_n_click(os.environ['RED_X'], 3)
find_n_click(os.environ['CLAIM_AFK_LOOT'], 1)
find_n_click(os.environ['CONFIRM_BUTTON'], 1)

results = activate_scrolls()


operation_results.append(results)
print(operation_results)
