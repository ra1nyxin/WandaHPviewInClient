"""Draw a text-free Workshop preview using Pillow."""
from pathlib import Path
from PIL import Image, ImageDraw

scale = 3
image = Image.new("RGB", (512 * scale, 512 * scale), "#232629")
draw = ImageDraw.Draw(image)

def box(values):
    return tuple(round(value * scale) for value in values)

def polygon(points, fill):
    draw.polygon([box(point) for point in points], fill=fill)

# The heart is filled as a single shape so its outline remains clear at thumbnail size.
heart = Image.new("L", image.size, 0)
mask = ImageDraw.Draw(heart)
mask.ellipse(box((56, 189, 120, 253)), fill=255)
mask.ellipse(box((108, 189, 172, 253)), fill=255)
mask.polygon([box(p) for p in ((57, 229), (171, 229), (114, 292))], fill=255)
image.paste("#c93737", mask=heart)
draw = ImageDraw.Draw(image)

polygon([(196, 235), (228, 235), (228, 222), (253, 246), (228, 270), (228, 257), (196, 257)], "#e7e4dc")

draw.rounded_rectangle(box((268, 224, 470, 269)), radius=5 * scale, fill="#101112", outline="#e7e4dc", width=2 * scale)
colors = ["#bf1f1f", "#e6401f", "#f26e1f", "#eda624", "#c4bd2e", "#80b338", "#3ba647"]
for i, color in enumerate(colors):
    left = 274 + i * 190 / len(colors)
    right = 274 + (i + 1) * 190 / len(colors)
    draw.rectangle(box((left, 230, right, 263)), fill=color)
draw.rectangle(box((382, 218, 388, 275)), fill="#f7f4eb", outline="#171717", width=scale)

image.resize((512, 512), Image.Resampling.LANCZOS).save(
    Path(__file__).resolve().parents[1] / "preview.jpg", "JPEG", quality=92, optimize=True)
