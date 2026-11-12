"""Draw the Workshop preview using Pillow and locally installed fonts."""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

SCALE = 3
image = Image.new("RGB", (512 * SCALE, 512 * SCALE), "#191a1b")
draw = ImageDraw.Draw(image)

def xy(values):
    return tuple(round(value * SCALE) for value in values)

def line(points, color, width=1):
    draw.line([xy(point) for point in points], fill=color, width=width * SCALE, joint="curve")

def font(size, bold=False):
    return ImageFont.truetype("C:/Windows/Fonts/msyhbd.ttc" if bold else "C:/Windows/Fonts/msyh.ttc", size * SCALE)

def centered(position, text, size, color, bold=False):
    draw.text(xy(position), text, font=font(size, bold), fill=color, anchor="mm")

draw.rounded_rectangle(xy((20, 20, 492, 492)), radius=12 * SCALE, outline="#72624d", width=2 * SCALE)
draw.ellipse(xy((153, 72, 359, 278)), fill="#232526", outline="#b89b69", width=4 * SCALE)
draw.ellipse(xy((164, 83, 348, 267)), outline="#514739", width=2 * SCALE)
for i in range(12):
    angle = math.pi * i / 6
    x, y = 256 + math.sin(angle) * 86, 175 - math.cos(angle) * 86
    draw.ellipse(xy((x-2, y-2, x+2, y+2)), fill="#b89b69")
line([(256, 175), (241, 124)], "#d8c6a4", 4)
line([(256, 175), (297, 196)], "#d8c6a4", 4)
draw.ellipse(xy((251, 170, 261, 180)), fill="#d8c6a4")
centered((256, 43), "旺达年龄条", 26, "#f2e8d8", True)
centered((256, 298), "45", 35, "#f6f1e8", True)
colors = ["#bf1f1f", "#e6401f", "#f26e1f", "#eda624", "#c4bd2e", "#80b338", "#3ba647"]
draw.rounded_rectangle(xy((48, 326, 464, 358)), radius=4 * SCALE, fill="#08090a", outline="#ac9572", width=2 * SCALE)
for i, color in enumerate(colors):
    left = 53 + i * 406 / len(colors)
    right = 53 + (i + 1) * 406 / len(colors)
    draw.rectangle(xy((left, 331, right, 353)), fill=color)
draw.rounded_rectangle(xy((279, 319, 286, 365)), radius=2 * SCALE, fill="#f7f3e9", outline="#292929", width=SCALE)
centered((66, 384), "年老", 17, "#e8dacc")
centered((446, 384), "年轻", 17, "#e8dacc")
line([(55, 409), (457, 409)], "#5d5142", 1)
centered((256, 444), "WANDA AGE BAR", 18, "#cbbfa9", True)
image = image.resize((512, 512), Image.Resampling.LANCZOS)
image.save(Path(__file__).resolve().parents[1] / "preview.jpg", "JPEG", quality=92, optimize=True)
