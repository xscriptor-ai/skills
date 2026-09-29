# xglassmorphism Skill

Real glassmorphism system for TypeScript + CSS web applications, with Tauri 2.x
packaging where native window effects apply.

This skill is intended for AI-assisted design, implementation, review, and
debugging of translucent blurred UI: sticky headers, cards, modals, popovers,
sheets, toasts, command palettes, and desktop windows with vibrancy.

## What it covers

- the optics of real glass: blur, tint, saturation, edges, noise, depth
- the five-layer surface model and intensity decision tables
- `backdrop-filter` mechanics: backdrop roots, clipping, masks, fallbacks
- design tokens, light/dark theming, and the TypeScript token contract
- typed components for React 19, Vue 3, Svelte 5, vanilla TS, and Web Components
- accessibility: WCAG contrast over worst-case backdrops, reduced
  transparency/contrast/motion, forced colors, focus visibility
- performance budgets, engine bug catalog, and the 2026 support matrix
- fullstack integration: SSR, theme persistence API, admin preview, visual
  regression, CI, deployment
- Tauri 2.x: native vibrancy vs CSS glass, `windowEffects`, drag regions,
  packaging, App Store constraints

## Structure

```text
web-fullstack/
  design/
    xglassmorphism/
      SKILL.md
      README.md
      references/
        01-physics-of-glass.md
        02-css-implementation.md
        03-design-tokens-and-theming.md
        04-typescript-components.md
        05-accessibility-and-legibility.md
        06-performance-and-browser-support.md
        07-fullstack-architecture.md
        08-tauri-packaging.md
```

## Main entry point

- `SKILL.md`

## Reference files

- `references/01-physics-of-glass.md`
- `references/02-css-implementation.md`
- `references/03-design-tokens-and-theming.md`
- `references/04-typescript-components.md`
- `references/05-accessibility-and-legibility.md`
- `references/06-performance-and-browser-support.md`
- `references/07-fullstack-architecture.md`
- `references/08-tauri-packaging.md`

## Related

- [web-fullstack index](../README.md)
- [xscriptor-ai/skills](https://github.com/xscriptor-ai/skills)
- [xscriptor-ai/agents](https://github.com/xscriptor-ai/agents)
