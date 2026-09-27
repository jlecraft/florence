# Repository Guidelines

## Project Structure & Module Organization

`build.py` is the source for the home data and page markup. It generates `index.html`, the self-contained `Florence-Homes.html`, and `florence-homes.zip`. `style.css` defines the layout; `assets/01.jpg` through `assets/08.jpg` match the eight homes in preference order. `house_list.txt` records the original listing links and notes. There is no separate test directory or application framework.

## Build, Test, and Development Commands

- `python3 build.py` regenerates all three deliverables after editing home data, markup, or CSS.
- `python3 -m py_compile build.py` checks Python syntax.
- `python3 -m http.server 8000` serves the directory locally; open `http://localhost:8000/` to review the page. Stop the server with Ctrl+C.

Use Python 3's standard library for the build. No package installation is required.

## Coding Style & Naming Conventions

Use four-space indentation for new Python code and descriptive, lowercase variable names. Keep listing facts in `build.py`, so rebuilding cannot discard an HTML-only edit. Escape inserted text with `html.escape` and retain `rel="noopener noreferrer"` on links that open a new tab. Keep image filenames in two-digit preference order (`01.jpg`, `02.jpg`, and so on). Add CSS rules to `style.css`, including narrow-screen behavior when a change affects card width.

## Testing Guidelines

There is no automated test suite or coverage target. After rebuilding, inspect `index.html` and `Florence-Homes.html` at desktop and mobile widths. Confirm eight home cards, eight comparison rows, working image links, and readable detail labels. Check that the ZIP contains the current `index.html`, `style.css`, and all eight images. Add focused automated checks only when a change introduces behavior that is hard to verify visually.

## Commit & Pull Request Guidelines

This directory has no Git history, so no existing commit convention can be inferred. If version control is added, use short, imperative subjects such as `Link listing photos to property pages`. Pull requests should describe the visible change, identify any listing sources used for factual updates, state how the page was checked, and include screenshots for layout changes. Rebuild generated files before submitting.
