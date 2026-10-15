# Ettlin Biomechanics

Static site for [ettlinbiomechanics.com](https://www.ettlinbiomechanics.com), hosted on GitHub Pages. Replaces the former Wix build.

- English at `/`, German at `/de/`, Spanish at `/es/`.
- All copy lives in `build.py` (the `LANGS` dictionary). Edit it, then run `python3 build.py` to regenerate the three `index.html` files, and push.
- Styles: `assets/styles.css`. Behaviour (header on scroll, language menu, contact form): `assets/site.js`.
- The contact form has no server. It opens the visitor's email app with a message addressed to ettlinbiomechanics@gmail.com.
