Intended usage: You can import function from these files to add color to your text

xc_ex has availabillity to color specific words

```python
import xc # xterm color
# or from xc import gxt
# or import pycolorhelpers.xc
# or import sys; sys.path.append("path/to/the/directory/with/xc")

# You can color text with a function

def light_blue(text):
    print(xc.gxt(f"{text}", 0, 204, 255))

light_blue("This is light blue!")

# You can store colored text as a variable

purple_text = xc.gxt("This is purple!", 123, 104, 238)
print(purple_text)

# Same with multiline text
multiline_text = xc.gxt("""This text is colored lavender
It has multiple lines
You can add as much as you want""", 224, 181, 255)
print(multiline_text)
```
