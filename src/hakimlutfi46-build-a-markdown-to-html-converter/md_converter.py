
import re
import sys
import html
import os
import argparse
from pathlib import Path

def markdown_to_html(markdown_text):
    
    blocks = markdown_text.strip().split('\n\n')
    html_output = []

    for block in blocks:
        
        if block.strip().startswith('```'):
            lines = block.split('\n')
            lang = lines[0][3:].strip()  
            
            if lines[-1].strip() == '```':
                code_lines = lines[1:-1]
            else:
                code_lines = lines[1:]
            
            code = '\n'.join(code_lines)
            escaped_code = html.escape(code)
            html_output.append(
                f'<pre><code class="language-{lang}">{escaped_code}</code></pre>'
            )
            continue  
    
        block = re.sub(
            r'!\[(.*?)\]\((.*?)(?:\s+"(.*?)")?\)',
            lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}"'+ (f' title="{m.group(3)}"' if m.group(3) else '') + '>',block)
        block = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', block)
        block = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', block)
        block = re.sub(r'_(?!_)(.*?)_(?!_)', r'<em>\1</em>', block)

        
        if re.match(r'^#{1,6}\s', block):
            level = len(block.split(' ')[0])
            text = ' '.join(block.split(' ')[1:])
            html_output.append(f'<h{level}>{text}</h{level}>')
        
        elif re.match(r'^\d+\.\s', block):
            items = block.split('\n')
            list_items = [f'<li>{re.sub(r"^\d+\.\s", "", item)}</li>' for item in items]
            html_output.append('<ol>\n' + '\n'.join(list_items) + '\n</ol>')
        
        elif re.match(r'^<img .*?>$', block.strip()):
            
            html_output.append(f'<figure>{block}</figure>')
        
        else:
            html_output.append(f'<p>{block.replace("\n", "<br>")}</p>')

    return '\n\n'.join(html_output)


def _write_html_file(output_file_path, html_body, title="Converted Markdown"):
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n")
        f.write(f"  <meta charset='UTF-8'>\n  <title>{html.escape(title)}</title>\n</head>\n<body>\n")
        f.write(html_body)
        f.write("\n</body>\n</html>")


def convert_file(input_file_path: Path, output_file_path: Path, title: str = None) -> None:
    with open(input_file_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    html_content = markdown_to_html(markdown_content)
    page_title = title or input_file_path.stem
    output_file_path.parent.mkdir(parents=True, exist_ok=True)
    _write_html_file(output_file_path, html_content, page_title)


def convert_directory(input_dir: Path, output_dir: Path, recursive: bool = False) -> int:
    pattern = "**/*.md" if recursive else "*.md"
    count = 0
    for md_path in input_dir.glob(pattern):
        if md_path.is_dir():
            continue
        relative = md_path.relative_to(input_dir)
        out_html = (output_dir / relative).with_suffix('.html')
        convert_file(md_path, out_html)
        count += 1
    return count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert Markdown (.md) to HTML. Supports single file or entire directory.")
    parser.add_argument("input", help="Input .md file or a directory containing .md files")
    parser.add_argument("-o", "--output", help="Output file (for single file input) or output directory (for directory input)")
    parser.add_argument("-r", "--recursive", action="store_true", help="Recurse into subdirectories when input is a directory")
    parser.add_argument("-t", "--title", help="HTML <title> for single file conversion (defaults to filename)")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input path '{input_path}' not found.")
        sys.exit(1)

    if input_path.is_file():
        if input_path.suffix.lower() != ".md":
            print("Error: Input file must have a .md extension.")
            sys.exit(1)
        if args.output:
            output_file = Path(args.output)
            if output_file.is_dir():
                output_file = output_file / (input_path.stem + ".html")
        else:
            output_file = input_path.with_suffix('.html')

        convert_file(input_path, output_file, title=args.title)
        print(f"✅ Conversion successful! File saved to: {output_file}")
        return

    # Directory input
    output_dir = Path(args.output) if args.output else (input_path / "html_output")
    converted = convert_directory(input_path, output_dir, recursive=args.recursive)
    if converted == 0:
        print("No .md files found to convert.")
    else:
        print(f"✅ Converted {converted} file(s). Output directory: {output_dir}")

if __name__ == "__main__":
    main()
