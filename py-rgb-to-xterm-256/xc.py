def xc(text: str, r: int, g: int, b: int) -> str:
    """
    Converts RGB to an xterm-256color ANSI sequence 
    and returns it as a string.
    """
    # Quick formula to approximate 256 color
    r_idx = int(r / 255 * 5)
    g_idx = int(g / 255 * 5)
    b_idx = int(b / 255 * 5)
    color_code = 16 + 36 * r_idx + 6 * g_idx + b_idx
    
    return f"\033[38;5;{color_code}m{text}\033[0m"

if __name__ == "__main__":
	print(gxt.gxt("████████████████████ This is dark pink", 198, 71, 148))
	print(gxt.gxt("████████████████████ This is pink", 251, 168, 250))
	print(gxt.gxt("████████████████████ This is white", 225, 255, 255))
	print(gxt.gxt("████████████████████ This is blue", 75, 196, 244))
	print(gxt.gxt("████████████████████ This is white", 225, 255, 255))
	print(gxt.gxt("████████████████████ This is pink", 251, 168, 250))
	print(gxt.gxt("████████████████████ This is dark pink", 198, 71, 148))
