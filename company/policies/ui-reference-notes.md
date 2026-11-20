# UI Reference Notes

These notes are design references, not instructions to copy another product's source or artwork.

## Sources

- ThreeUI: https://threeui.com — Three.js components, WebGL backgrounds, interactive shaders, hero sections, motion design, and source-backed variants.
- Taste Skill: https://tasteskill.dev — an explicit anti-AI-slop workflow: choose a visual direction, build a palette and typography system, use real imagery deliberately, and inspect at 1440px, 768px, and 390px.
- GSAP: https://gsap.com — professional motion design with deliberate easing, timelines, choreographed sequences, and accessible UI interactions.
- 21st.dev: https://21st.dev — crafted React/TypeScript/Tailwind/shadcn components, live previews, design tokens, and copy-owned source rather than opaque runtime lock-in.

## Rules to apply

1. Start with a visual brief: audience, product personality, visual motif, palette, typography, density, interaction model, and non-goals.
2. Choose one clear art direction per page. Do not combine random gradients, glass cards, emoji, unrelated shadows, and generic purple hero sections.
3. Use design tokens for color, type scale, spacing, radii, borders, shadows, motion duration, and z-index. Prefer a small palette with one accent and semantic status colors.
4. Build a hierarchy before components: one focal action, a readable headline, useful supporting copy, and a real product preview or working interaction instead of filler cards.
5. Use 3D only when it explains or strengthens the product. Keep a non-WebGL fallback, lazy-load heavy assets, respect reduced-motion, and maintain usable keyboard/focus states.
6. Make motion purposeful. Use enter, hover, scroll, and state transitions with consistent easing; do not animate every element or use infinite motion as decoration.
7. Use components as owned source. Inspect the license and adapt the component to the project's tokens and accessibility requirements; never blindly paste a dependency or copied page.
8. Validate in a real browser at desktop, tablet, and mobile widths. Check layout balance, blank gaps, overflow, contrast, focus, reduced-motion, console errors, and network failures.
9. Before handing off, run the project's formatter, typecheck, linter, tests, and production build when available. Report commands and evidence.
