"""Draw the Workshop preview with Pillow, without generated images."""
import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

S = 3
rng = random.Random(1820)
image = Image.new("RGB", (512 * S, 512 * S), "#d9ceb1")
draw = ImageDraw.Draw(image)

def coords(values):
    return tuple(round(v * S) for v in values)

def stroke(points, color, width=1):
    draw.line([coords(p) for p in points], fill=color, width=width * S, joint="curve")

def text(x, y, value, size, color, font="georgia.ttf", anchor=None):
    face = ImageFont.truetype("C:/Windows/Fonts/" + font, size * S)
    draw.text(coords((x, y)), value, font=face, fill=color, anchor=anchor)

# A few irregular marks give the paper a printed, tactile finish.
for _ in range(2100):
    x, y = rng.randrange(512 * S), rng.randrange(512 * S)
    shade = rng.choice(("#c9bfa5", "#e3d9bf", "#d3c6ab"))
    draw.point((x, y), fill=shade)

text(46, 42, "WANDA'S", 18, "#5c5146", "georgiai.ttf")
text(44, 67, "A matter", 48, "#2c2928", "georgiab.ttf")
text(44, 122, "of time.", 48, "#2c2928", "georgiab.ttf")
stroke([(45, 190), (160, 190)], "#9b4d3f", 3)

# Pocket watch, intentionally drawn with doubled, imperfect ink outlines.
draw.ellipse(coords((263, 141, 442, 320)), fill="#a58a5e", outline="#282826", width=4*S)
draw.ellipse(coords((270, 147, 435, 312)), fill="#e5d9bc", outline="#282826", width=3*S)
draw.arc(coords((257, 137, 447, 325)), 35, 325, fill="#5d4d38", width=S)
draw.ellipse(coords((327, 120, 374, 160)), outline="#282826", width=4*S)
draw.rectangle(coords((341, 139, 360, 151)), fill="#9f845c", outline="#282826", width=2*S)
for i in range(12):
    a = math.pi * i / 6
    r1, r2 = (67, 73) if i % 3 else (62, 73)
    stroke([(352 + math.sin(a)*r1, 230 - math.cos(a)*r1),
            (352 + math.sin(a)*r2, 230 - math.cos(a)*r2)], "#39342d", 2)
stroke([(352, 230), (341, 184)], "#2e2b28", 4)
stroke([(352, 230), (385, 246)], "#2e2b28", 3)
draw.ellipse(coords((347, 225, 357, 235)), fill="#9b4d3f", outline="#282826", width=S)

text(47, 267, "A LITTLE MORE", 12, "#6d5f4e", "arialbd.ttf")
text(47, 287, "TIME TO SEE", 12, "#6d5f4e", "arialbd.ttf")
text(47, 307, "WHERE YOU ARE.", 12, "#6d5f4e", "arialbd.ttf")
stroke([(45, 367), (467, 367)], "#52493d", 2)
colors = ["#9b4d3f", "#bd6b40", "#d49a48", "#c6ae61", "#8d9d63", "#58876b"]
for i, color in enumerate(colors):
    a = 46 + i * 420 / len(colors)
    b = 46 + (i + 1) * 420 / len(colors)
    draw.rectangle(coords((a, 373, b, 382)), fill=color)
stroke([(45, 389), (467, 389)], "#52493d", 1)
stroke([(286, 359), (286, 397)], "#2c2928", 3)
draw.polygon([coords((281, 355)), coords((291, 355)), coords((286, 362))], fill="#2c2928")
text(46, 411, "AGE BAR", 25, "#2c2928", "georgiab.ttf")
text(46, 449, "A CLIENT-SIDE WANDA MOD", 11, "#716454", "arialbd.ttf")

image.resize((512, 512), Image.Resampling.LANCZOS).save(
    Path(__file__).resolve().parents[1] / "preview.jpg", "JPEG", quality=92, optimize=True)
