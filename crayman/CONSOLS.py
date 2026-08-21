"""
جميع الحقوق محفوظة لدى المطور المصري @cr_dex على تليجرام
All rights reserved to the Egyptian developer @cr_dex on Telegram
  Telegram < t.me/cr_dex > |  channal < @mt_4_4 >
"""
import os
from rich.console import Console
from rich.syntax import Syntax
from rich.panel import Panel

O = '\x1b[38;5;216m'
CL = '\x1b[0m'

def CONSOLE(Out):
    if os.path.isfile(Out):
        console = Console()
        content = open(Out, 'r', encoding='utf-8').read()
        syntax = Syntax(content, "python", theme="monokai", line_numbers=True)
        panel = Panel(syntax, style="cyan", expand=True)
        console.print(panel)
    else: print(f"{O}{Out} not found{CL}")

def CONSOLT(*args):
    if args:
        console = Console()
        text = ''.join(map(str, args))
        syntax = Syntax(text, "python", theme="monokai", line_numbers=True)
        panel = Panel(syntax, style="cyan", expand=True)
        console.print(panel)
    else: print(f'{O}No text code{CL}')
