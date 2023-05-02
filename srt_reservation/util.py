import argparse
import sys
import subprocess
import pyautogui
import random

screenWidth, screenHeight = pyautogui.size()


def parse_cli_args():

    parser = argparse.ArgumentParser(description='')

    parser.add_argument("--user", help="Username", type=str, metavar="1234567890")
    parser.add_argument("--psw", help="Password", type=str, metavar="abc1234")
    parser.add_argument("--dpt", help="Departure Station", type=str, metavar="동탄")
    parser.add_argument("--arr", help="Arrival Station", type=str, metavar="동대구")
    parser.add_argument("--dt", help="Departure Date", type=str, metavar="20220118")
    parser.add_argument("--tm", help="Departure Time", type=str, metavar="08, 10, 12, ...")

    parser.add_argument("--num", help="no of trains to check", type=int, metavar="2", default=2)
    parser.add_argument("--reserve", help="Reserve or not", type=bool, metavar="2", default=False)
    
    # sms
    parser.add_argument('--sms', action=argparse.BooleanOptionalAction)
    
    # screen saver disable
    parser.add_argument('--scr', action=argparse.BooleanOptionalAction, default=True)

    args = parser.parse_args()

    return args

def play_notification_sound(sound_file = None):
    if sys.platform == "win32": # Windows
        import winsound
        if sound_file == None:
            duration = 1000  # milliseconds
            frequency = 440  # Hz
            winsound.Beep(frequency, duration)
        else:
            print(sound_file)
            winsound.PlaySound(sound_file, winsound.SND_FILENAME)
    else: # Mac
        if sound_file == None:
            sound_file = "/System/Library/Sounds/Ping.aiff"
        subprocess.call(["afplay", sound_file])
        
def mouse_move():
    ran_width = random.randint(1, screenWidth)
    ran_height = random.randint(1, screenHeight)

    #마우스를 2초동안 ran_width, ran_height 위치로 옮김
    pyautogui.moveTo(ran_width, ran_height, 0.5)
    #pyautogui.moveTo(50, 100, duration = 1) # move the mouse
