from dotenv import load_dotenv
import os
from daily import find_n_click
import pyautogui
import datetime
import time

class Shop:
    """
    includes all operations that happen in the Shop tab
    """

    def __init__(self):
        """

        """
        load_dotenv()
        self.daily_summons_count = 0
        self.daily_goods_count = 0
        # break the file path out to a helper function
        absolute_path = os.path.dirname(__file__)

        self.shop = os.path.join(absolute_path, "images\inv_tabs\shop\shop.png")
        self.goods_sub_tab = os.path.join(absolute_path, "images\inv_tabs\shop\goods\goods.png")
        self.claim_ads = os.path.join(absolute_path, "images\inv_tabs\shop\goods\claim_ads.png")
        self.shop_active = os.path.join(absolute_path, "images\inv_tabs\shop\shop_active.png")
        self.summon_button = os.path.join(absolute_path, "images\inv_tabs/shop\summon_button_v3.png")
        self.summon_weapon_button = os.path.join(absolute_path, "images\inv_tabs\shop\summon_weapon_button.png")
        self.summon_accessories_button = os.path.join(absolute_path, "images\inv_tabs\shop\summon_accessories_button.png")
        self.confirm_summon_button = os.path.join(absolute_path, "images\inv_tabs\shop\confirm_button.png")
        self.shop_icon = os.environ['SHOP_ICON']

    def open_shop(self) -> bool:
        shop_opened = find_n_click(self.shop_icon, 2)

        if shop_opened:
            return True
        else:
            return False

    def daily_summon(self) -> bool:
        """
        Opens the Shop tab at the bottom
        :return:
        """
        tap_to_start_loc = list(
            pyautogui.locateAllOnScreen(f'{self.summon_button}', region=(0, 0, 590, 1030), confidence=0.75)
        )
        # TODO: adjust confidence to return only 3 tap_to_start_loc's
        # 0-2 = Equipment
        # 3-4 = Accessories
        # 5 = Skill Card
        summon_cards = {
            "equipment": {
                "button_image": self.summon_weapon_button,
                "index": 2
            },
            "accessories": {
                "button_image": self.summon_accessories_button,
                "index": 3
            },
            "skills": {
                "index": 5
            }
        }

        for x in summon_cards.keys():
            button_location = pyautogui.center(tap_to_start_loc[summon_cards[x]['index']])
            pyautogui.click(button_location[0], button_location[1])
            if x == "skills":
                find_n_click(summon_cards[x]['button_image'], 2)
                time.sleep(5)
                self.save_summon_rewards(x)
                find_n_click(self.confirm_summon_button, 2)
            else:
                # Saving summon, add sleep to screenshot
                time.sleep(5)
                self.save_summon_rewards(x)
                find_n_click(self.confirm_summon_button, 2)
                find_n_click(self.shop_active, 2)

        return True


    def collect_goods(self) -> bool:
        """
        Collects daily diamonds and emeralds from the shop -> goods tab. Limit per day = 10
        :return:
        """
        # Select the goods sub tab
        goods_tab = pyautogui.locateOnScreen(f'{self.goods_sub_tab}',  region=(0, 0, 590, 1030), confidence=0.80)
        pyautogui.click(goods_tab[0], goods_tab[1])

        tap_to_start_loc = list(
            pyautogui.locateAllOnScreen(f'{self.claim_ads}', region=(0, 0, 590, 1030), confidence=0.95)
        )

        for x in range(0, 10):
            time.sleep(.25)
            dizmonds = pyautogui.center(tap_to_start_loc[0])
            emeralds = pyautogui.center(tap_to_start_loc[1])
            pyautogui.click(dizmonds[0], dizmonds[1])
            pyautogui.click(emeralds[0], emeralds[1])
            self.daily_goods_count = self.daily_goods_count + 1

        return True

    def save_summon_rewards(self, pull_type) -> bool:
        """
        Takes screenshot of summon results and saves to folder
        TODO: break screenshot function out to helper file
        :return:
        """

        timestamp = datetime.datetime.now()
        timestamp = timestamp.strftime("%m-%d-%Y_%X").replace(":", ".")
        image = pyautogui.screenshot(region=(10, 90, 550, 930))
        image.save(f"./images/inv_tabs/shop/pulls/{pull_type}/{timestamp}.PNG")
