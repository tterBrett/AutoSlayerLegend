import os
import pyautogui
from dotenv import load_dotenv
import datetime
from general import find_n_click


class Daily:

    def __init__(self):
        load_dotenv()
        dir_path = os.path.dirname(__file__)

        self.summons_count = 0
        self.goods_count = 0
        self.scrolls = 0

        self.afk_screenshots_path = os.path.join(dir_path, "images/afk_rewards")
        self.afk_screenshot_region = [50, 260, 450, 480]

    def activate_scrolls(self) -> bool:
        """
        Summary: Screenshots afk rewards and saves image to track exp/hr and gold/hr
        :return: boolean determining if the scrolls were activated fast enough
        """
        if find_n_click(os.environ['SCROLL_INTERFACE_ICON'], .90):
            daily_scrolls = [
                os.environ['GOLD_SCROLL_ICON'], os.environ['EXP_SCROLL_ICON'],
                os.environ['ENHANCE_CUBE_SCROLL_ICON'], os.environ['EQUIPMENT_SCROLL_ICON']
            ]

            scrolls_found = []
            for scroll in daily_scrolls:
                # Same operation listed twice to activate daily limit of 2
                scrolls_found.append(find_n_click(scroll, .95))
                scrolls_found.append(find_n_click(scroll, .95))
                self.scrolls += 1

            if False in scrolls_found:
                print(f"404 - Failed to active all scrolls {scrolls_found}")
                return False
            else:
                print("200 - all scrolls have been activated")
                find_n_click(os.environ['RED_X'], .8)
                return True
