"""
جميع الحقوق محفوظة لدى المطور المصري @cr_dex على تليجرام
All rights reserved to the Egyptian developer @cr_dex on Telegram
  Telegram < t.me/cr_dex > |  channal < @mt_4_4 >
"""
import ast, os

def AST(f, w=True):
    if not os.path.isfile(f):
        print(f"Error: '{f}' not found.")
        return
    try:
        code = open(f, 'r', encoding='utf-8').read()
        unparsed = ast.unparse(ast.parse(code))
        open(f, 'w', encoding='utf-8').write(unparsed)
        if w: print(f'done {f}')
    except SyntaxError as e: print(f"Syntax Error in '{f}': Line {e.lineno}\n    {e.msg}")
    except Exception as e: print(f"Error: {e}")
