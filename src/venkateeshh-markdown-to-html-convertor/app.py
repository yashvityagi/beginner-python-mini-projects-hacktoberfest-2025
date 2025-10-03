#!/usr/bin/env python3
"""md2html.py

Simple Markdown -> HTML converter.

Features:
- Two modes: a) simple built-in Markdown parser (covers headings, bold, italics,
  links, inline code, code blocks, lists, paragraphs) b) full-featured using
  the `markdown` PyPI package (if you prefer richer output).
- Convert a single .md file or all .md files in a directory.
- Optional CSS file to style output or uses a small default style.
- Generates a standalone .html file with a basic template.

Usage examples:

    # convert single file using built-in parser
    python md2html.py README.md

    # convert using the markdown package (pip install markdown)
    python md2html.py README.md --use-lib

    # convert all markdown files in a directory
    python md2html.py docs/ --out-dir site/

    # add custom css
    python md2html.py README.md --css custom.css

"""
import argparse
import os
import re
import sys
from pathlib import Path

DEFAULT_CSS = """
body { font-family: system-ui, -apple-system, Segoe UI, Roboto, 'Helvetica Neue', Arial; max-width: 760px; margin: 3rem auto; line-height: 1.6; padding: 0 1rem; }
pre { background:#f6f8fa; padding:1rem; overflow:auto; }
code { background:#f6f8fa; padding:0.15rem 0.3rem; border-radius:4px; }
h1,h2,h3,h4 { margin-top:1.4rem; }
blockquote { color:#555; border-left:4px solid #ddd; padding-left:1rem; margin:1rem 0; }
ul,ol { margin:0.5rem 0 1rem 1.25rem; }
"""

# -------------------- Simple markdown parser --------------------
# This is intentionally small: it handles common constructs but is NOT a
# full CommonMark parser. Use the markdown package for full fidelity.

_heading_re = re.compile(r'^(#{1,6})\s+(.*)$')
_hr_re = re.compile(r'^(\*{3,}|-{3,}|_{3,})$')
_codeblock_start_re = re.compile(r'^```(.*)$')
_list_item_re = re.compile(r'^(\s*)([-*+]|\d+\.)\s+(.*)$')
_blockquote_re = re.compile(r'^(>+)\s?(.*)$')

def escape_html(s: str) -> str:
    return (s.replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;'))

def inline_transform(s: str) -> str:
    # Strong: **text** or __text__
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'__(.+?)__', r'<strong>\1</strong>', s)
    # Emphasis: *text* or _text_
    s = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
    s = re.sub(r'_(.+?)_', r'<em>\1</em>', s)
    # Inline code `code`
    s = re.sub(r'`([^`]+?)`', lambda m: f"<code>{escape_html(m.group(1))}</code>", s)
    # Links [text](url)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
    return s


def convert_simple_markdown(md_text: str) -> str:
    lines = md_text.splitlines()
    out_lines = []

    in_codeblock = False
    codeblock_lang = ''
    codeblock_lines = []

    list_stack = []  # stack of (indent_level, list_type)

    para_open = False

    def close_paragraph():
        nonlocal para_open
        if para_open:
            out_lines.append('</p>')
            para_open = False

    def close_all_lists(curr_indent=0):
        nonlocal list_stack
        while list_stack and list_stack[-1][0] >= curr_indent:
            _, lt = list_stack.pop()
            out_lines.append(f'</{lt}>')

    i = 0
    while i < len(lines):
        line = lines[i]
        i += 1
        if in_codeblock:
            if _codeblock_start_re.match(line):
                # end code block
                in_codeblock = False
                out_lines.append('<pre><code>')
                out_lines.extend(escape_html(l) for l in codeblock_lines)
                out_lines.append('</code></pre>')
                codeblock_lines = []
                continue
            else:
                codeblock_lines.append(line)
                continue

        m = _codeblock_start_re.match(line)
        if m:
            close_paragraph()
            close_all_lists()
            in_codeblock = True
            codeblock_lang = m.group(1).strip()
            codeblock_lines = []
            continue

        if not line.strip():
            # blank line -> paragraph/list/code separation
            close_paragraph()
            close_all_lists()
            continue

        # horizontal rule
        if _hr_re.match(line.strip()):
            close_paragraph()
            close_all_lists()
            out_lines.append('<hr/>')
            continue

        # heading
        m = _heading_re.match(line)
        if m:
            close_paragraph()
            close_all_lists()
            level = len(m.group(1))
            text = inline_transform(m.group(2).strip())
            out_lines.append(f'<h{level}>{text}</h{level}>')
            continue

        # blockquote
        m = _blockquote_re.match(line)
        if m:
            close_paragraph()
            close_all_lists()
            depth = len(m.group(1))
            text = inline_transform(m.group(2).strip())
            # simple: wrap entire line in blockquote tags (no nesting handling)
            out_lines.append(f'<blockquote>{text}</blockquote>')
            continue

        # list item
        m = _list_item_re.match(line)
        if m:
            indent = len(m.group(1).expandtabs(4))
            marker = m.group(2)
            content = inline_transform(m.group(3).strip())
            list_type = 'ul' if not marker.endswith('.') else 'ol'

            if not list_stack or indent > list_stack[-1][0]:
                # open new list
                list_stack.append((indent, list_type))
                out_lines.append(f'<{list_type}>')
            else:
                # close lists until current indent fits
                while list_stack and indent < list_stack[-1][0]:
                    _, lt = list_stack.pop()
                    out_lines.append(f'</{lt}>')
                # if same indent but different list type, close and open
                if list_stack and list_stack[-1][1] != list_type:
                    _, lt = list_stack.pop()
                    out_lines.append(f'</{lt}>')
                    list_stack.append((indent, list_type))
                    out_lines.append(f'<{list_type}>')

            out_lines.append(f'<li>{content}</li>')
            continue

        # normal paragraph text
        if not para_open:
            para_open = True
            out_lines.append('<p>')
        out_lines.append(inline_transform(line.strip()))

    # finish up
    if in_codeblock:
        # unclosed code block: flush what we have
        out_lines.append('<pre><code>')
        out_lines.extend(escape_html(l) for l in codeblock_lines)
        out_lines.append('</code></pre>')

    close_paragraph()
    close_all_lists(0)

    return "\n".join(out_lines)

# -------------------- HTML template & file helpers --------------------

def make_html_page(title: str, body_html: str, css: str | None = None) -> str:
    if css is None:
        css = DEFAULT_CSS
    return f"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{escape_html(title)}</title>
<style>
{css}
</style>
</head>
<body>
<main>
{body_html}
</main>
</body>
</html>
"""


def write_output(html: str, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(html, encoding='utf-8')
    print(f'Wrote: {out_path}')

# -------------------- Optional markdown lib mode --------------------
try:
    import markdown as _markdown_lib  # type: ignore
except Exception:
    _markdown_lib = None


def convert_with_markdown_lib(md_text: str) -> str:
    if _markdown_lib is None:
        raise RuntimeError('markdown package is not installed. run: pip install markdown')
    return _markdown_lib.markdown(md_text, extensions=['fenced_code', 'tables', 'codehilite'])

# -------------------- CLI --------------------

def process_file(in_path: Path, out_path: Path, use_lib: bool, css_text: str | None):
    md_text = in_path.read_text(encoding='utf-8')
    if use_lib:
        body = convert_with_markdown_lib(md_text)
    else:
        body = convert_simple_markdown(md_text)
    html = make_html_page(title=in_path.stem, body_html=body, css=css_text)
    write_output(html, out_path)


def gather_files(input_path: Path):
    if input_path.is_dir():
        return list(input_path.glob('**/*.md'))
    elif input_path.is_file() and input_path.suffix.lower() == '.md':
        return [input_path]
    else:
        raise FileNotFoundError(f'No markdown files found at: {input_path}')


def main(argv=None):
    p = argparse.ArgumentParser(description='Convert Markdown (.md) files to standalone HTML')
    p.add_argument('input', help='Path to a .md file or a directory containing .md files')
    p.add_argument('--out-dir', help='Output directory (defaults to same folder as input)', default=None)
    p.add_argument('--use-lib', help='Use the "markdown" Python package for conversion', action='store_true')
    p.add_argument('--css', help='Path to custom CSS file to include in HTML', default=None)
    args = p.parse_args(argv)

    in_path = Path(args.input)
    out_dir = Path(args.out_dir) if args.out_dir else None

    css_text = None
    if args.css:
        css_text = Path(args.css).read_text(encoding='utf-8')

    files = gather_files(in_path)
    if not files:
        print('No markdown files found, exiting.')
        return

    for md in files:
        # determine out path
        if out_dir:
            rel = md.relative_to(in_path) if in_path.is_dir() else md.name
            if isinstance(rel, Path):
                out_path = out_dir / rel.parent / (md.stem + '.html')
            else:
                out_path = out_dir / (md.stem + '.html')
        else:
            out_path = md.with_suffix('.html')

        try:
            process_file(md, out_path, use_lib=args.use_lib, css_text=css_text)
        except Exception as e:
            print(f'Error processing {md}: {e}', file=sys.stderr)

if __name__ == '__main__':
    main()
