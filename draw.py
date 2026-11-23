"""Draw the news-image-20261123 front page (1024x1024 PNG) with PIL.

Fresh builder, written for 23 November 2026's news. Flat vector style:
masthead with the date, one hero story (COP31), a 2x2 grid of four more
stories, and an "also today" ticker. No photos, no copied artwork.
Run:  python3 draw.py  ->  entry.png beside this file.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
NAVY = (20, 33, 61)
NAVY2 = (28, 46, 84)
GOLD = (252, 163, 17)
RED = (193, 18, 31)
INK = (25, 25, 25)
GREY = (90, 90, 90)
CARD = (255, 255, 255)
BORDER = (200, 196, 186)
BLUE = (42, 111, 151)
GREEN = (82, 183, 136)

FONT_DIR = "/home/hatch/workspace/custom-skills/video-animasi-ringan/fonts/"
XB = FONT_DIR + "Montserrat-ExtraBold.ttf"
B = FONT_DIR + "Montserrat-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, f, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_block(d, x, y, lines, f, color, leading=None):
    if leading is None:
        leading = int(f.size * 1.25)
    for ln in lines:
        d.text((x, y), ln, font=f, fill=color)
        y += leading
    return y


def fit_lines(d, text, f, max_w, max_lines):
    """Wrap text; shrink the font until it fits max_lines (min 60% size)."""
    size = f.size
    while size > int(f.size * 0.6):
        lines = wrap(d, text, f, max_w)
        if len(lines) <= max_lines:
            return lines, f
        size -= 2
        f = font(f.path, size)
    return wrap(d, text, f, max_w)[:max_lines], f


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- masthead ----------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.text((W // 2, 26), "THE WORLD TODAY", font=font(XB, 62), fill=(255, 255, 255), anchor="ma")
d.text((W // 2, 100), "MONDAY  23  NOVEMBER  2026", font=font(B, 30), fill=GOLD, anchor="ma")
d.rectangle([0, 148, W, 156], fill=RED)

# ---------- hero: COP31 ----------
hx0, hy0, hx1, hy1 = 28, 168, 996, 470
d.rectangle([hx0, hy0, hx1, hy1], fill=CARD, outline=BORDER, width=2)
# illustration: cracked globe, left side
cx, cy, r = 196, 318, 96
d.rectangle([hx0 + 2, hy0 + 2, 330, hy1 - 2], fill=(232, 240, 244))
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=BLUE, outline=NAVY, width=3)
# continents (simple blobs)
d.ellipse([cx - 62, cy - 58, cx - 8, cy - 6], fill=GREEN)
d.ellipse([cx + 6, cy - 30, cx + 58, cy + 22], fill=GREEN)
d.ellipse([cx - 40, cy + 28, cx + 18, cy + 66], fill=GREEN)
d.ellipse([cx + 28, cy + 40, cx + 66, cy + 74], fill=GREEN)
# crack across the globe
crack = [(cx - 78, cy - 52), (cx - 34, cy - 18), (cx - 52, cy + 8), (cx - 6, cy + 30),
         (cx - 24, cy + 58), (cx + 22, cy + 78), (cx + 12, cy + 96)]
d.line(crack, fill=RED, width=7, joint="curve")
# NO DEAL stamp, slightly rotated
stamp = Image.new("RGBA", (190, 64), (0, 0, 0, 0))
sd = ImageDraw.Draw(stamp)
sd.rounded_rectangle([4, 4, 186, 60], radius=8, outline=RED, width=5)
sd.text((95, 32), "NO DEAL", font=font(XB, 30), fill=RED, anchor="mm")
stamp = stamp.rotate(-9, expand=True, resample=Image.BICUBIC)
img.paste(stamp, (150, 388), stamp)
d = ImageDraw.Draw(img)
# hero text, right side
tx = 360
d.text((tx, hy0 + 22), "CLIMATE  ·  ANTALYA, TURKEY", font=font(B, 21), fill=RED)
d.text((tx, hy0 + 56), "COP31 COLLAPSES", font=font(XB, 56), fill=NAVY)
d.text((tx, hy0 + 118), "WITH NO DEAL", font=font(XB, 56), fill=NAVY)
deck = ("Longest summit in history ends after the EU and others reject a pact "
        "that never mentions fossil fuels. The blame game begins in Australia.")
lines, _ = fit_lines(d, deck, font(B, 24), hx1 - tx - 28, 4)
text_block(d, tx, hy0 + 196, lines, font(B, 24), (60, 60, 60), leading=31)

# ---------- 2x2 grid ----------
cards = [
    # (kicker, headline, deck, accent, icon)
    ("IRAN WAR  ·  BAHRAIN", "Strikes hit Bahrain",
     "Iran hits a civilian site and US bases as Trump demands a \u201creal deal\u201d.",
     RED, "missile"),
    ("UKRAINE  ·  KYIV REGION", "Flats hit, 15 killed",
     "Dymer block collapses; missiles enter Poland as NATO meets in emergency.",
     (0, 90, 140), "building"),
    ("UNITED STATES", "Democrats take House",
     "258 seats \u2014 best since 1992 \u2014 as Trump moves to block oversight.",
     (0, 80, 160), "capitol"),
    ("GAZA", "99% toxic, Oxfam warns",
     "Report finds contamination across nearly all of Gaza after the assault.",
     (120, 90, 0), "warning"),
]
gx, gy = 28, 486
cw, chh, gap = 476, 186, 16
for i, (kicker, head, deck, accent, icon) in enumerate(cards):
    x0 = gx + (i % 2) * (cw + gap)
    y0 = gy + (i // 2) * (chh + gap)
    x1, y1 = x0 + cw, y0 + chh
    d.rectangle([x0, y0, x1, y1], fill=CARD, outline=BORDER, width=2)
    d.rectangle([x0, y0, x1, y0 + 6], fill=accent)
    # icon box
    ix0, iy0, ix1, iy1 = x0 + 14, y0 + 22, x0 + 128, y0 + chh - 14
    d.rectangle([ix0, iy0, ix1, iy1], fill=(238, 238, 234))
    icx, icy = (ix0 + ix1) // 2, (iy0 + iy1) // 2
    if icon == "missile":
        # diagonal missile with flame
        d.polygon([(icx - 34, icy + 30), (icx + 8, icy - 12), (icx + 22, icy - 26),
                   (icx + 30, icy - 12), (icx - 8, icy + 34)], fill=(70, 70, 70))
        d.polygon([(icx + 22, icy - 26), (icx + 38, icy - 40), (icx + 34, icy - 18)],
                  fill=RED)
        d.polygon([(icx - 44, icy + 38), (icx - 30, icy + 44), (icx - 36, icy + 52)],
                  fill=GOLD)
        d.ellipse([icx - 52, icy + 44, icx - 38, icy + 58], fill=(255, 120, 40))
    elif icon == "building":
        # broken apartment block with smoke
        d.polygon([(icx - 42, iy1 - 8), (icx - 42, icy - 34), (icx - 22, icy - 48),
                   (icx - 6, icy - 30), (icx + 12, icy - 44), (icx + 30, icy - 28),
                   (icx + 42, icy - 36), (icx + 42, iy1 - 8)], fill=(110, 120, 135))
        for wx in (-30, -6, 18):
            for wy in (-14, 12):
                d.rectangle([icx + wx, icy + wy, icx + wx + 14, icy + wy + 16], fill=(40, 45, 60))
        d.ellipse([icx + 18, icy - 62, icx + 34, icy - 46], fill=(150, 150, 150))
        d.ellipse([icx + 28, icy - 72, icx + 48, icy - 54], fill=(170, 170, 170))
    elif icon == "capitol":
        # dome on a colonnaded base
        d.rectangle([icx - 44, icy + 8, icx + 44, iy1 - 8], fill=(225, 225, 220))
        for cxp in (-34, -12, 10, 32):
            d.rectangle([icx + cxp, icy + 16, icx + cxp + 8, iy1 - 8], fill=(160, 160, 155))
        d.pieslice([icx - 34, icy - 40, icx + 34, icy + 28], 180, 360, fill=(245, 245, 240),
                   outline=NAVY, width=2)
        d.rectangle([icx - 4, icy - 52, icx + 4, icy - 38], fill=NAVY)
        d.ellipse([icx - 20, icy - 34, icx + 20, icy - 22], fill=(245, 245, 240))
    else:  # warning triangle
        d.polygon([(icx, icy - 48), (icx + 48, icy + 34), (icx - 48, icy + 34)],
                  fill=(255, 196, 0), outline=(20, 20, 20))
        d.polygon([(icx, icy - 48), (icx + 48, icy + 34), (icx - 48, icy + 34)],
                  outline=(20, 20, 20))
        d.text((icx, icy - 2), "!", font=font(XB, 44), fill=(20, 20, 20), anchor="mm")
        d.rectangle([icx - 48, iy1 - 10, icx + 48, iy1 - 8], fill=(120, 90, 0))
    # card text
    tx = x0 + 142
    tw = x1 - tx - 14
    d.text((tx, y0 + 20), kicker, font=font(B, 16), fill=accent)
    hlines, _ = fit_lines(d, head, font(XB, 27), tw, 2)
    y = text_block(d, tx, y0 + 46, hlines, font(XB, 27), NAVY, leading=31)
    dlines, _ = fit_lines(d, deck, font(B, 18), tw, 3)
    text_block(d, tx, y + 4, dlines, font(B, 18), (70, 70, 70), leading=23)

# ---------- ticker ----------
ty0, ty1 = 890, 996
d.rectangle([0, ty0, W, ty1], fill=NAVY)
d.text((28, ty0 + 14), "ALSO TODAY", font=font(XB, 22), fill=GOLD)
tick = ("Nvidia scandal: Huang aide linked to Chinese state security  ·  "
        "Delta outage delays 1,600 flights  ·  Mexico captures \u201cEl Chapo Isidro\u201d")
tlines, _ = fit_lines(d, tick, font(B, 21), W - 56, 3)
text_block(d, 28, ty0 + 44, tlines, font(B, 21), (255, 255, 255), leading=27)

img.save("entry.png", optimize=True)
print("saved entry.png", img.size)
