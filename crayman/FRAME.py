from .COLOR import COLOR
import textwrap
from wcwidth import wcswidth

def FRAME(text, mode="auto"):
    terminal_width = shutil.get_terminal_size().columns
    lines = textwrap.dedent(text).strip().splitlines()
    def visual_len(s):
        w = wcswidth(s)
        return w if w >= 0 else len(s)
    def visual_ljust(s, width):
        padding = width - visual_len(s)
        return s + " " * max(padding, 0)
    max_len = max((visual_len(line) for line in lines), default=0)
    if mode == "screen": inner_width = terminal_width - 4
    else: inner_width = max_len
    print(COLOR(f"┌{'─' * (inner_width + 2)}┐"))
    middle_lines = [f"│ {visual_ljust(line, inner_width)} │" for line in lines]
    print(COLOR("\n".join(middle_lines)))
    print(COLOR(f"└{'─' * (inner_width + 2)}┘"))