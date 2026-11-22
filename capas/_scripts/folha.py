"""Folha de contato: junta imagens lado a lado com rótulo.
Uso: python -I folha.py SAIDA.jpg LARGURA_MINIATURA COLUNAS IMG1 IMG2 ...
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

out, tw, cols = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
paths = sys.argv[4:]
ims = []
for p in paths:
    im = Image.open(p).convert("RGB")
    th = int(im.height * tw / im.width)
    ims.append((os.path.basename(p), im.resize((tw, th), Image.LANCZOS)))
rows = (len(ims) + cols - 1) // cols
th = max(i.height for _, i in ims)
pad, lab = 12, 34
sheet = Image.new("RGB", (cols * (tw + pad) + pad, rows * (th + lab + pad) + pad), (20, 20, 20))
d = ImageDraw.Draw(sheet)
try:
    f = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
except Exception:
    f = ImageFont.load_default()
for k, (name, im) in enumerate(ims):
    r, c = divmod(k, cols)
    x, y = pad + c * (tw + pad), pad + r * (th + lab + pad)
    d.text((x, y + 4), name, fill=(235, 235, 235), font=f)
    sheet.paste(im, (x, y + lab))
sheet.save(out, quality=84)
print("ok", out, sheet.size)
