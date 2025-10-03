# Markdown to HTML Converter

A simple Python-based tool to convert Markdown (`.md`) files into standalone HTML files.

This project includes:
- A **built-in lightweight Markdown parser** (supports headings, lists, code blocks, links, bold/italic, blockquotes, etc.).
- An option to use the **`markdown` PyPI package** for full CommonMark + extensions.
- Support for converting **a single file** or **all `.md` files in a directory**.
- Optional **custom CSS** or a built-in default style.

---

## Features
- Convert `.md` files to `.html` with ease.
- Lightweight built-in parser.
- Support for fenced code blocks (```), headings, lists, blockquotes.
- Inline formatting: **bold**, *italic*, `inline code`, [links](#).
- Full CommonMark + tables & extensions with `--use-lib` (requires `pip install markdown`).
- Automatically generates a standalone HTML page with styles.

---

## Installation

Clone this repo and navigate into it:
```bash
git clone https://github.com/yourusername/md2html.git
cd md2html
```

(Optional) install the `markdown` package for extended features:
```bash
pip install markdown
```

---

## Usage

### Convert a single file:
```bash
python md2html.py README.md
```

### Convert with full Markdown library support:
```bash
python md2html.py README.md --use-lib
```

### Convert all `.md` files in a directory:
```bash
python md2html.py docs/ --out-dir site/
```

### Use custom CSS:
```bash
python md2html.py README.md --css styles.css
```

---

## Example
Given an input file `example.md`:
```markdown
# Hello World

This is **Markdown** converted to HTML.

- Item 1
- Item 2

```

Run:
```bash
python md2html.py example.md
```

Output file `example.html`:
```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>example</title>
  <style> ... default CSS ... </style>
</head>
<body>
  <main>
    <h1>Hello World</h1>
    <p>This is <strong>Markdown</strong> converted to HTML.</p>
    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
  </main>
</body>
</html>
```

---

## Options
- `--out-dir <dir>` → specify an output directory.
- `--use-lib` → use the `markdown` package instead of the built-in parser.
- `--css <file>` → add a custom CSS file.

---

## License
MIT License © 2025
