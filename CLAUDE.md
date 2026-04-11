# FC Global Group Landing

Static marketing landing page for FC Global Group LLC — a U.S.-based Amazon FBA wholesale distribution company.

## Stack

- Vanilla HTML5 / CSS3 / ES6 JavaScript — no frameworks, no build step, no dependencies
- Google Fonts: Outfit (headings) + DM Sans (body), loaded via `<link>` in `index.html`

## Running locally

```bash
python3 -m http.server 8000
# then open http://localhost:8000
```

Or open `index.html` directly in a browser — it works either way.

## File layout

| File | Purpose |
|------|---------|
| `index.html` | All markup and section structure |
| `style.css` | All styles — CSS variables defined at the top in `:root` |
| `script.js` | Scroll reveal (Intersection Observer), parallax, nav shrink, form handling |

## Key conventions

**Colors** — change the palette by editing the CSS custom properties at the top of `style.css`:
- `--obsidian-*` — primary dark backgrounds
- `--gold-*` — accent color throughout
- `--steel` / `--silver` — body text hierarchy
- `--pearl` / `--snow` — light text on dark backgrounds

**Animations** — scroll-reveal is driven by the `.reveal` class (and `.reveal-delay-1` / `.reveal-delay-2` for stagger). Add it to any element to opt in.

**Form** — the contact form simulates a 1500 ms API call (`setTimeout`). There is no real backend; wire up a real endpoint in `script.js` → `handleFormSubmit` when needed.

**Responsive breakpoints** — `1024px` (tablet) and `768px` (mobile) in `style.css`.

## What to avoid

- Do not introduce a bundler, framework, or npm unless the scope of work genuinely requires it.
- Do not add inline styles — use CSS variables and existing utility classes instead.
- The grain overlay (`z-index: 10000`) sits above everything; do not place interactive elements above it.
