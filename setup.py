import os
import win32gui as wgui
import win32con
import time
from dotenv import load_dotenv


load_dotenv()


def start_new_instance(start_loc: str) -> int:
    """
    Summary
        Check if BlueStacks App Player is currently running on device. If not, launch desktop shortcut
        and re-runs check to see if App Player is running. Once true, returns window_id
    :return:
        int: window_id for App Player
    """
    if wgui.FindWindow(None, "BlueStacks App Player"):
        print("Application is running")
        window_id_out = wgui.FindWindow(None, "BlueStacks App Player")
        return window_id_out

    else:
        print(f"Application is launching")
        os.startfile(f'{start_loc}')
        time.sleep(10)
        window_id_out = start_new_instance(start_loc)

        wgui.SetForegroundWindow(window_id_out)
        move_instance(window_id_out)
        kill_bluestacks_x()

        return window_id_out


def kill_bluestacks_x() -> None:
    """
    Summary
        Finds the other instance of BlueStacks and ends the process
        TODO: does not work on first execution. Click to activate BlueStacks X instance before delete
    :return:
    """
    if wgui.FindWindow(None, "BlueStacks X"):
        kill_window = wgui.FindWindow(None, "BlueStacks X")
        print(f"Killing BlueStacks X with id {kill_window}")
        wgui.PostMessage(kill_window, win32con.WM_CLOSE, 0, 0)


def move_instance(window_id_in: int) -> None:
    """
    Summary
        Places App Player in desired window location.
        Currently places fixed location as application can't even handle one instance yet
    Problems
        Taking BlueStacks App Player to new screen prevents MoveWindow()'s x,y coordinate change
        TODO: do some math on screen dimensions to place instance accordingly
    :returns
        None
    """

    wgui.MoveWindow(window_id_in, 0, 0, 590, 1030, False)


# Getting game launched
window_id = start_new_instance(os.environ['SLAYER_LEGEND_LAUNCH'])
kill_bluestacks_x()
