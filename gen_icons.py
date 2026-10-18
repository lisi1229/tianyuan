# -*- coding: utf-8 -*-
"""生成 PWA 图标：墨底金字的「天」"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

FONT = "/usr/share/fonts/noto/NotoSerifCJK-Regular.ttc"
IDX = 2
OUT = "/var/minis/workspace/tiangyuan/"


def make(size):
    S = size
    img = Image.new("RGB", (S, S), (13, 12, 10))
    d = ImageDraw.Draw(img)
    # 细金边
    m = int(S * 0.055)
    d.rounded_rectangle([m, m, S - m, S - m], radius=int(S * 0.20),
                        outline=(184, 148, 74), width=max(1, S // 128))
    # 字
    f = ImageFont.truetype(FONT, int(S * 0.56), index=IDX)
    tb = d.textbbox((0, 0), "天", font=f)
    w, h = tb[2] - tb[0], tb[3] - tb[1]
    pos = ((S - w) / 2 - tb[0], (S - h) / 2 - tb[1] - S * 0.01)
    # 微光晕
    glow = Image.new("RGB", (S, S), (0, 0, 0))
    ImageDraw.Draw(glow).text(pos, "天", font=f, fill=(120, 96, 50))
    glow = glow.filter(ImageFilter.GaussianBlur(S // 26))
    img = Image.fromarray(np.clip(np.array(img, float) + np.array(glow, float) * 0.9, 0, 255).astype("uint8"))
    d = ImageDraw.Draw(img)
    d.text(pos, "天", font=f, fill=(216, 186, 118))
    img.save(OUT + f"icon-{S}.png")
    print("icon", S)


for s in (192, 512):
    make(s)
