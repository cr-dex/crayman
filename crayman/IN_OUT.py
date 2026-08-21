"""
جميع الحقوق محفوظة لدى المطور المصري @cr_dex على تليجرام
All rights reserved to the Egyptian developer @cr_dex on Telegram
  Telegram < t.me/cr_dex > |  channal < @mt_4_4 >
"""
import argparse, os, tempfile, sys
from .COLOR import COLOR
from .IMPORT import IMPORT

R = '\x1b[31m'
Y = '\033[93m'
O = '\x1b[38;5;216m'
G = '\x1b[38;5;220m'
CY = '\x1b[36m'

IMPORT()

TEMP = tempfile.NamedTemporaryFile(delete=True).name
version = ".".join(sys.version.split(" ")[0].split(".")[:-1])

def IN_OUT(VERSION=version):
    parser = argparse.ArgumentParser(description=f"{G}Project that manage all themes, colors, inputs, output, versions, mode[free variable] and ast code[clean]    {CY}[ powered by @cr_dex on telegram ]")
    parser.add_argument('filename', type=str, help=f'{Y} path of the file that you want be as input{CY}', metavar=f"{O}File input {G}", nargs='?')
    parser.add_argument('-o', type=str, help='output to save [ == for save to input ]', metavar="output")
    parser.add_argument('-m', type=str, help='mode of any thing as your prefer', metavar="mode")
    parser.add_argument('-v', type=str, help='version of the python’s file', metavar="version")
    args = parser.parse_args()
    input_file = args.filename
    output_file = args.o or TEMP if args.o != '==' else input_file
    file_version = args.v or VERSION
    mode = args.m or None
    if input_file and not os.path.isfile(str(input_file)): exit(COLOR('Error: File Not Found'))
    return input_file, output_file, file_version, mode