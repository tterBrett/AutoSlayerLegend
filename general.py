import pyautogui
import time
from datetime import datetime
import os


def find_n_click(image_name: str, conf: float) -> bool:
    """
    Summary: Attempts to find a given image on the screen and clicks center of image if found
    :param image_name: file path to image being searched on screen
    :param conf: percentage of confidence to find the image
    :return: boolean determining if search was successful
    """
    tap_to_start_loc = pyautogui.locateOnScreen(f'{image_name}', confidence=conf)
    if tap_to_start_loc is not None:
        print(f"200 - Found image")
        button_location = pyautogui.center(tap_to_start_loc)
        pyautogui.click(button_location[0], button_location[1])
        return True
    else:
        print(f"404 - Unable to see image")
        return False


def capture_and_save(screenshot_region, file_name) -> bool:
    """
    Takes screenshot given area on screen, saves it as given file in specified path.
    Should NOT include timestamp or file type
    :param screenshot_region: area on screen that is being captured
    :param file_name: path and name of file to be saved
    :return: T/F if image is present after save occurs
    """

    timestamp = datetime.now()
    timestamp = timestamp.strftime("%m-%d-%Y_%X").replace(":", ".")
    file_name += f"{timestamp}.png"

    image = pyautogui.screenshot(
        region=(
            screenshot_region[0], screenshot_region[1],
            screenshot_region[2], screenshot_region[3]
        )
    )
    image.save(f"{file_name}")
    did_save = os.path.exists(file_name)

    if did_save:
        print(f"200 - screenshot was saved")
    else:
        print(f"404 - screenshot was not saved")

    return did_save


def login() -> bool:
    result = find_n_click(os.environ['LOGIN_IMAGE'], .9)
    return result


def claim_afk_rewards() -> None:
    find_n_click(os.environ['CLAIM_AFK_LOOT'], .8)
    time.sleep(1)
    dir_path = os.path.dirname(__file__)
    afk_screenshots_path = os.path.join(dir_path, "images/afk_rewards")
    afk_screenshot_region = [50, 260, 450, 480]
    capture_and_save(afk_screenshot_region, afk_screenshots_path)
    result = find_n_click(os.environ['CONFIRM_BUTTON'], .9)
    return result
