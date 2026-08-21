"""
جميع الحقوق محفوظة لدى المطور المصري @cr_dex على تليجرام
All rights reserved to the Egyptian developer @cr_dex on Telegram
  Telegram < t.me/cr_dex > |  channal < @mt_4_4 >
"""
import random
from pystyle import Colors, Colorate

def COLOR(*args):
    colors_list = [Colors.red_to_green, Colors.green_to_red, Colors.yellow_to_red, Colors.red_to_yellow, Colors.purple_to_red, Colors.red_to_purple, Colors.yellow_to_green, Colors.green_to_yellow, Colors.green_to_cyan, Colors.cyan_to_green]
    text = ''.join(map(str, args))
    return Colorate.Horizontal(random.choice(colors_list), text)
