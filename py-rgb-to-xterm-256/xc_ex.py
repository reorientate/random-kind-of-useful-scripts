#!/usr/bin/env python3
import re
def _bounded(word: str) -> str:
    esc = re.escape(word)
    left = r'\b' if word[0].isalnum() or word[0] == '_' else ''
    right = r'\b' if word[-1].isalnum() or word[-1] == '_' else ''
    return f"{left}{esc}{right}"

def gxt(text: str, r: int, g: int, b: int, words: list[str] = None) -> str:
    # formula to approximate 256 color
    r_idx = int(r / 255 * 5)
    g_idx = int(g / 255 * 5)
    b_idx = int(b / 255 * 5)
    color_code = 16 + 36 * r_idx + 6 * g_idx + b_idx
    color = f"\033[38;5;{color_code}m"
    reset = "\033[0m"

    if words: # You can color a specific word
        ordered = sorted(words, key=len, reverse=True)
        pattern = '|'.join(_bounded(w) for w in ordered)
        return re.sub(pattern, lambda m: f"{color}{m.group(0)}{reset}", text)

    return f"{color}{text}{reset}"

if "__name__" == "__main__":
	print(gxt_ex.gxt("████████████████████ This is dark pink", 198, 71, 148, ["████████████████████", "dark pink"]))
	print(gxt_ex.gxt("████████████████████ This is pink", 251, 168, 250, ["████████████████████", "pink"]))
	print(gxt_ex.gxt("████████████████████ This is white", 225, 255, 255, ["████████████████████", "white"]))
	print(gxt_ex.gxt("████████████████████ This is blue", 75, 196, 244, ["████████████████████", "blue"]))
	print(gxt_ex.gxt("████████████████████ This is white", 225, 255, 255, ["████████████████████", "white"]))
	print(gxt_ex.gxt("████████████████████ This is pink", 251, 168, 250, ["████████████████████", "pink"]))
	print(gxt_ex.gxt("████████████████████ This is dark pink", 198, 71, 148, ["████████████████████", "dark pink"]))
