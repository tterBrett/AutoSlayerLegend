from shop import Shop
from general import *
from bluestacks import BlueStacks
from dotenv import load_dotenv
from daily import Daily
import os

# Load env variables
load_dotenv()

# Constructors
instance = BlueStacks()
daily = Daily()
newShop = Shop()

first_login_of_day_operations = [
    "instance.start_new_instance(os.environ['SLAYER_LEGEND_LAUNCH'])",
    "login()",
    "find_n_click(os.environ['CLAIM_DAILY_REWARDS'], .8)",
    "find_n_click(os.environ['RED_X'], .8)",
    "claim_afk_rewards()",
    "daily.activate_scrolls()"
]

first_login_of_day_shop_only_operations = [
    "newShop.open_shop()",
    "newShop.daily_summon()",
    "newShop.collect_goods()"
]

testing_operations = [
    "newShop.open_shop()",
    "newShop.daily_summon()",
]

active_operations = testing_operations
no_error = True

while no_error and len(active_operations) > 0:
    current_operation = active_operations.pop(0)
    no_error = eval(current_operation)
    print(f"value of no error is: {no_error}")

    if not no_error:
        # Re-try failed operation 3 times before failing
        for x in range(1, 4):
            print(f"attempt {x} in failure.")
            time.sleep(20)
            no_error = eval(current_operation)
            if no_error:
                print("operation succeed")
                break
    time.sleep(20)
