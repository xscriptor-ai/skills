# Skill: linkedin

opencode skill to produce LinkedIn content end to end: Spanish copies with a
hook, hashtags, and an optimized structure, plus 1080x1350 images on OLED black
with the tiny `X - Scriptor` signature.

It ships a pack of **200 publications** (12 topics: xscriptor, TypeScript, web,
accessibility, usability, programming, JavaScript, VS Code, extensions, dev
ecosystem, Linux distros, and career) and all the strategy knowledge gathered in
`references/`.

## Installing in opencode

Global (recommended):

```bash
cp -r linkedin ~/.config/opencode/skills/
# restart opencode
```

Project:

```bash
mkdir -p .opencode/skills
cp -r linkedin .opencode/skills/
# or register this folder in opencode.json:
# { "skills": { "paths": ["path/to/skills"] } }
# restart opencode
```

## Usage

```bash
python3 scripts/generar.py --out content --count 200
python3 scripts/generar.py --topic typescript --count 20 --out out-ts
python3 scripts/generar.py --out content --count 50 --start 201
python3 scripts/generar.py --out drafts --count 30 --text-only
```

## Structure

```
linkedin/
├── SKILL.md                   # skill instructions (frontmatter + workflow)
├── README.md                  # this file
├── scripts/
│   ├── generar.py             # post + image generator (CLI)
│   ├── temas.py               # topics, hashtags, ideas, CTAs, windows
│   └── ganchos.py             # the 200 hooks
└── references/
    ├── linkedin-strategy.md   # what the algorithm rewards (with numbers)
    ├── copy-structure.md      # hooks, the 4 structures, hashtags
    ├── visual-system.md       # image tokens and composition
    └── publishing.md          # cadence, windows, golden hour, metrics
```

## Notes

- The skill files are in English; the generated post copies are in Spanish, since
  that is the publishing language of the account.
- The images use OLED black, hairline strokes, and a single red accent. The only
  visible brand is `X - Scriptor`, small and subtle; no other brand appears.

## Requirements

- Python 3 (standard library only).
- `rsvg-convert` (`librsvg2-bin`) to rasterize the images.
- Space Grotesk, Space Mono, and Doto fonts installed on the system.
