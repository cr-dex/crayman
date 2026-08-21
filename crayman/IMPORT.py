"""
جميع الحقوق محفوظة لدى المطور المصري @cr_dex على تليجرام
All rights reserved to the Egyptian developer @cr_dex on Telegram
  Telegram < t.me/cr_dex > |  channal < @mt_4_4 >
"""
import builtins
import importlib

def IMPORT():
    standard_modules = [
        're', 'io', 'os', 'dis', 'sys', 'random', 'time', 'tempfile',
        'subprocess', 'webbrowser', 'marshal', 'base64', 'zlib', 'lzma',
        'codecs', 'shutil', 'logging', 'traceback', 'pystyle',
        'termcolor', 'pathlib', 'autopep8', 'ast', 'builtins'
    ]

    for mod_name in standard_modules:
        try: setattr(builtins, mod_name, importlib.import_module(mod_name))
        except ImportError: pass

    specific_bindings = {
        'Path': ('pathlib', 'Path'),
        'Union': ('typing', 'Union'),
        'Optional': ('typing', 'Optional'),
        'CodeType': ('types', 'CodeType'),
        'render': ('cfonts', 'render'),
        'Fore': ('colorama', 'Fore'),
        'init': ('colorama', 'init'),
        'Colors': ('pystyle', 'Colors'),
        'Colorate': ('pystyle', 'Colorate'),
        'Center': ('pystyle', 'Center'),
        'Write': ('pystyle', 'Write'),
        'findall': ('re', 'findall'),
        'Popen': ('subprocess', 'Popen'),
        'PIPE': ('subprocess', 'PIPE'),
        'Process': ('multiprocessing', 'Process'),
        'ZipFile': ('zipfile', 'ZipFile'),
        'printt': ('rich', 'print')
    }

    for builtin_attr, (mod_name, attr_name) in specific_bindings.items():
        try:
            module = importlib.import_module(mod_name)
            setattr(builtins, builtin_attr, getattr(module, attr_name))
        except (ImportError, AttributeError): pass
