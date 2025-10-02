
import re
import sys
import html

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


def main():
    if len(sys.argv) != 3:
        print("Usage: python md_converter.py <input_file.md> <output_file.html>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]

    try:
        with open(input_file_path, 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        html_content = markdown_to_html(markdown_content)

        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write("<!DOCTYPE html>\n<html lang='en'>\n<head>\n")
            f.write("  <meta charset='UTF-8'>\n  <title>Converted Markdown</title>\n</head>\n<body>\n")
            f.write(html_content)
            f.write("\n</body>\n</html>")

        print(f"✅ Conversion successful! File saved to: {output_file_path}")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
