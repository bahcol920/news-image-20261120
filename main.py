#!/usr/bin/env python3
# Deterministic offline generator, see README.md.
# Run: pip install Pillow && python3 main.py
import os, sys
W = H = 1024
OUT = sys.argv[1] if len(sys.argv) > 1 else "output"
HEADLINES = [
 ("SUMMIT", "Trump-Xi-Putin 1st trilateral summit, Shenzhen", "peace declaration: nuclear war must never be fought"),
 ("JUSTICE", "ICJ rules Myanmar committed genocide vs Rohingya", "first time the UN court holds a state responsible, 9-6 vote"),
 ("INNOVATION", "Anthropic IPO debut: $81B raised, $2T peak", "largest pure AI listing ever, closes near $1.3T"),
 ("GAMING", "GTA VI released: 99 on Metacritic ties record", "highest rated game ever, level with Ocarina of Time"),
 ("DRONES", "Turkiye Kizilelma stealth fighter enters service", "first 3 jets delivered to armed forces"),
 ("UKRAINE", "Europe ready for talks, Kyiv hit by missiles overnight", "EU $45B aid push, Kremlin vows painful reply over Crimea Bridge"),
 ("ENERGY", "Strait of Hormuz shock: biggest oil trade disruption", "IEA: energy world will never be the same, Brent $92+"),
 ("CLIMATE", "Cyclone Akvan hits India coast, COP31 deadline", "120k evacuated in Odisha, Africa seeks more climate funds"),
]
def main():
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new("RGB", (W, H), (18, 22, 32)); d = ImageDraw.Draw(img)
    def font(size, bold=False):
        p = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        return ImageFont.truetype(p, size) if os.path.exists(p) else ImageFont.load_default()
    f_title, f_sub = font(62, True), font(27)
    f_kicker, f_head, f_body = font(19, True), font(28, True), font(23)
    d.rectangle([0, 0, W, 148], fill=(30, 58, 95)); d.rectangle([0, 148, W, 154], fill=(230, 180, 60))
    d.text((48, 34), "20 NOVEMBER 2026", font=f_title, fill=(255, 255, 255))
    d.text((48, 106), "THE WORLD IN 8 HEADLINES", font=f_sub, fill=(200, 215, 235))
    y = 180
    colors = [(240,110,110),(110,190,220),(230,180,60),(150,220,140),(190,150,240),(240,170,90),(250,110,160),(120,200,200)]
    for i, (kicker, head, body) in enumerate(HEADLINES):
        c = colors[i % len(colors)]
        d.rounded_rectangle([36, y, W-36, y+86], radius=14, fill=(38, 46, 64), outline=c, width=2)
        d.rectangle([36, y, 48, y+86], fill=c)
        d.text((64, y+9), kicker, font=f_kicker, fill=c)
        d.text((64, y+32), head, font=f_head, fill=(255, 255, 255))
        d.text((64, y+60), body, font=f_body, fill=(190, 200, 215))
        y += 98
    d.text((36, H-42), "snapped 20 Nov 2026  ·  sources: AA, Xinhua, BBC, Kyodo", font=f_body, fill=(150, 160, 175))
    os.makedirs(OUT, exist_ok=True)
    out_path = os.path.join(OUT, "entry.png")
    img.save(out_path, format="PNG", optimize=False, compress_level=6, pnginfo=None)
    print(f"wrote {out_path} ({os.path.getsize(out_path)} bytes, {W}x{H})")
if __name__ == "__main__":
    main()
