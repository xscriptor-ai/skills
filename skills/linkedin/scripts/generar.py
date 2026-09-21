#!/usr/bin/env python3
"""Generate numbered LinkedIn posts + 1080x1350 images.

Content system to position X - Scriptor (or any technical account):
- Spanish copies with a 2-line hook, short paragraphs, arrows, and a closing
  question; 3 niche hashtags; suggested publishing window.
- OLED black images, Space Grotesk / Space Mono / Doto typography, a single red
  accent, and the tiny `X - Scriptor` signature, barely visible.
- The .md number always matches the image number.

Usage:
    python3 scripts/generar.py --out content --count 200
    python3 scripts/generar.py --topic typescript --count 20 --out out-ts
    python3 scripts/generar.py --count 30 --text-only --out drafts

Requirements: python3; rsvg-convert (librsvg2-bin) for images; Space Grotesk,
Space Mono, and Doto fonts installed (rsvg falls back silently if missing).
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from ganchos import HOOKS
from temas import CLOSERS, OPENERS, ORDER, TOPICS, WINDOWS

# ------------------------------------------------------------------ tokens
W, H = 1080, 1350
BLACK = "#000000"
DOTS = "#171717"
HAIR = "#151515"
INK = "#F2F2F2"
DIM = "#6E6E6E"
SUB = "#7A7A7A"
TICK = "#3A3A3A"
FAINT = "#3E3E3E"
ACCENT = "#D71921"
F_HEAD = "Space Grotesk"
F_MONO = "Space Mono"
F_DOTO = "Doto"
BRAND = "X - Scriptor"


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def plain(t):
    """Strip inline markdown: LinkedIn does not render it."""
    return t.replace("`", "").replace("**", "")


def slugify(t):
    t = t.replace("`", "")
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower()
    t = re.sub(r"[^a-z0-9 ]", "", t)
    return "-".join(t.split()[:6])[:52]


def wrap(text, max_chars):
    words, lines, cur = text.split(), [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if len(cand) <= max_chars or not cur:
            cur = cand
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_headline(text, max_w=880, max_lines=5, top=96, bottom=54):
    """Find the largest size that fits width and height without odd breaks."""
    size = top
    while size > bottom:
        per = max(8, int(max_w / (size * 0.60)))
        lines = wrap(text, per)
        if len(lines) <= max_lines and len(lines) * size * 1.14 <= 620:
            return size, lines
        size -= 4
    per = max(8, int(max_w / (bottom * 0.60)))
    return bottom, wrap(text, per)


def motif(k, cx, cy):
    """Hairline background structure (4 rotating variants)."""
    p, col = [], HAIR
    if k == 0:
        for r in range(120, 1500, 70):
            p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="1"/>')
    elif k == 1:
        for i in range(-14, 32):
            x = i * 72
            p.append(f'<line x1="{x}" y1="0" x2="{x + 1350}" y2="1350" stroke="{col}" stroke-width="1"/>')
    elif k == 2:
        for j in range(0, 1400, 54):
            p.append(f'<line x1="0" y1="{j}" x2="{W}" y2="{j}" stroke="{col}" stroke-width="1"/>')
    else:
        for r in range(150, 1400, 90):
            p.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{col}" stroke-width="1" stroke-dasharray="3 9"/>')
    return "\n".join(p)


def build_svg(num, label, head, sub, k):
    size, lines = fit_headline(head)
    lh = size * 1.12
    total = len(lines) * lh
    y0 = 700 - total / 2 + size * 0.82
    cx, cy = (860, 300) if k % 2 == 0 else (220, 1080)
    if k == 3:
        cx, cy = 880, 1120
    headline = "\n".join(
        f'<text x="96" y="{y0 + i * lh:.1f}" font-family="{F_HEAD}" font-size="{size}" '
        f'font-weight="500" letter-spacing="-0.02em" fill="{INK}">{esc(l)}</text>'
        for i, l in enumerate(lines)
    )
    rule_y = y0 - size * 0.82 - 54
    ticks = "\n".join(
        f'<path d="M {x} {y + sy * 18} L {x} {y} L {x + sx * 18} {y}" fill="none" '
        f'stroke="{TICK}" stroke-width="1"/>'
        for x, y, sx, sy in ((44, 44, 1, 1), (W - 44, 44, -1, 1), (44, H - 44, 1, -1), (W - 44, H - 44, -1, -1))
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs><pattern id="dots" width="16" height="16" patternUnits="userSpaceOnUse">
<circle cx="1" cy="1" r="0.9" fill="{DOTS}"/></pattern></defs>
<rect width="{W}" height="{H}" fill="{BLACK}"/>
<rect width="{W}" height="{H}" fill="url(#dots)"/>
{motif(k, cx, cy)}
{ticks}
<line x1="96" y1="{rule_y:.1f}" x2="256" y2="{rule_y:.1f}" stroke="{ACCENT}" stroke-width="1.6"/>
<circle cx="264" cy="{rule_y:.1f}" r="3" fill="{ACCENT}"/>
<text x="96" y="86" font-family="{F_MONO}" font-size="22" letter-spacing="0.18em" fill="{DIM}">{esc(label)}</text>
<text x="{W - 96}" y="92" font-family="{F_DOTO}" font-size="46" fill="#383838" text-anchor="end">{num:03d}</text>
{headline}
<text x="96" y="{y0 + total + 46:.1f}" font-family="{F_MONO}" font-size="22" letter-spacing="0.16em" fill="{SUB}">{esc(sub.upper())}</text>
<text x="{W - 96}" y="{H - 58}" font-family="{F_MONO}" font-size="19" letter-spacing="0.08em" fill="{FAINT}" text-anchor="end">{esc(BRAND)}</text>
</svg>'''


def compose_post(hook, items, opener, closer, mode):
    items = [plain(x) for x in items]
    if mode == 0:
        body = "\n\n".join(f"→ {x}" for x in items)
    elif mode == 1:
        body = "\n\n".join(f"{i + 1}) {x}" for i, x in enumerate(items))
    elif mode == 2:
        body = "\n\n".join(items)
    else:
        body = "\n\n".join(f"• {x}" for x in items)
    return f"{hook}\n\n{opener}\n\n{body}\n\n{closer}"


def build_sequence(topics, count):
    """Interleave topics round-robin: no two consecutive posts share a topic."""
    out, rnd = [], 0
    while len(out) < count:
        for topic in topics:
            hs = HOOKS.get(topic, [])
            if rnd < len(hs):
                out.append((topic, hs[rnd]))
        rnd += 1
        if rnd > 100:
            break
    return out[:count]


def main():
    ap = argparse.ArgumentParser(description="Generate numbered LinkedIn posts + images.")
    ap.add_argument("--out", default="content", help="output folder (default: content)")
    ap.add_argument("--count", type=int, default=200, help="number of posts to generate")
    ap.add_argument("--topic", action="append", default=None, help="limit to one or more topics (repeatable)")
    ap.add_argument("--start", type=int, default=1, help="starting number (to continue a series)")
    ap.add_argument("--text-only", action="store_true", help="only generate the .md files")
    args = ap.parse_args()

    topics = args.topic or ORDER
    for t in topics:
        if t not in TOPICS:
            sys.exit(f"unknown topic: {t}. Available: {', '.join(ORDER)}")
    sequence = build_sequence(topics, args.count)
    if not sequence:
        sys.exit("no hooks for those topics")

    posts_dir = os.path.join(args.out, "posts")
    img_dir = os.path.join(args.out, "img")
    tmp_dir = "/tmp/opencode-linkedin"
    os.makedirs(posts_dir, exist_ok=True)
    os.makedirs(tmp_dir, exist_ok=True)
    if not args.text_only:
        os.makedirs(img_dir, exist_ok=True)
        if shutil.which("rsvg-convert") is None:
            sys.exit("missing rsvg-convert (librsvg2-bin) to generate images")

    index = ["# Post index", "", "| Nº | Topic | Hook | Image |", "|---|---|---|---|"]
    for pos, (topic, hook) in enumerate(sequence):
        n = args.start + pos
        info = TOPICS[topic]
        items = info["items"]
        m = len(items)
        sel = [items[(n * 3 + k * 5) % m] for k in range(4)]
        closer = CLOSERS[n % len(CLOSERS)]
        opener = OPENERS[n % len(OPENERS)]
        text = compose_post(hook, sel, opener, closer, n % 4)
        sub = info["subs"][n % len(info["subs"])]
        window = WINDOWS[n % len(WINDOWS)]
        hashtags = " ".join(info["hashtags"])
        name = f"{n:03d}-{slugify(hook)}"

        if not args.text_only:
            svg = build_svg(n, info["label"], hook, sub, n % 4)
            svg_path = os.path.join(tmp_dir, name + ".svg")
            with open(svg_path, "w") as f:
                f.write(svg)
            subprocess.run(
                ["rsvg-convert", "-w", str(W), "-h", str(H), svg_path,
                 "-o", os.path.join(img_dir, name + ".png")],
                check=True,
            )

        alt = f"Número {n:03d}. Imagen minimalista en negro con tipografía blanca: «{hook}». Tema: {info['label'].title()}."
        md = [
            f"# {n:03d} · {hook}",
            "",
            f"- **Topic:** {info['label'].title()}",
            f"- **Image:** `img/{name}.png`",
            f"- **Image ALT:** {alt}",
            f"- **Suggested window:** {window}",
            f"- **Hashtags:** {hashtags}",
            "",
            "---",
            "",
            text,
            "",
            hashtags,
            "",
        ]
        with open(os.path.join(posts_dir, name + ".md"), "w") as f:
            f.write("\n".join(md))
        index.append(f"| {n:03d} | {info['label'].title()} | {hook} | `img/{name}.png` |")

    with open(os.path.join(args.out, "indice.md"), "w") as f:
        f.write("\n".join(index) + "\n")
    print(f"{len(sequence)} posts -> {args.out}/posts" + ("" if args.text_only else f" and {args.out}/img"))


if __name__ == "__main__":
    main()
