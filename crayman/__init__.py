"""
جميع الحقوق محفوظة لدى المطور المصري @cr_dex على تليجرام
All rights reserved to the Egyptian developer @cr_dex on Telegram
  Telegram < t.me/cr_dex > |  channal < @mt_4_4 >
"""
import sys, os, tempfile, subprocess

def _install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

_dependencies = {
    'pystyle': 'pystyle',
    'termcolor': 'termcolor',
    'colorama': 'colorama',
    'autopep8': 'autopep8',
    'rich': 'rich',
    'cfonts': 'python-cfonts'
}

for module_name, pip_name in _dependencies.items():
    try: __import__(module_name)
    except ImportError: _install(pip_name)


from .IMPORT import IMPORT
IMPORT()

TEMP = tempfile.NamedTemporaryFile(delete=True).name
version = ".".join(sys.version.split(" ")[0].split(".")[:-1])

R = '\x1b[31m'
def HELP():
    print(f'''
 CONSOLE(File)  {R}>> Print file's Code contents as Rich library
 CONSOLT(text)  {R}>> Print text Code contents as Rich library
   COLOR(text)  {R}>> print text colored as pystyle
   FRAME(text, auto/screen)  {R}>> print text colored as pystyle in box
    IMPORT()    {R}>> import all most of libraries
     IN_OUT()   {R}>> easy input import and export and versions
      HELP()    {R}>> to show this list help''')

from .COLOR import COLOR
from .CONSOLS import CONSOLE, CONSOLT
from .IN_OUT import IN_OUT
from .AST import AST
from .FRAME import FRAME
__all__ = ['COLOR', 'CONSOLE', 'FRAME', 'CONSOLT', 'IN_OUT', 'IMPORT', 'AST', 'HELP', 'TEMP', 'version']
