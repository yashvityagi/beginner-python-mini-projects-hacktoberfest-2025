# 🚀 Markdown to HTML Converter

This project is a custom-built Python script that converts Markdown files into well structured HTML. It was created for **Hacktoberfest 2025** with a focus on providing a lightweight, dependency free implementation of a Markdown parser.

The script handles several useful features beyond basic conversion, including support for ordered lists and semantic figure tags for images.

## ✨ Features

This converter supports the following Markdown syntax:

- **Headings (`<h1>` to `<h6>`)**: Converts lines starting with `#` to the appropriate heading level.
- **Bold**: Converts `**bold text**` to `<strong>bold text</strong>`.
- **Italic**: Converts `_italic text_` to `<em>italic text</em>`.
  - Note: This implementation specifically uses underscores (`_`) for italics.
- **Ordered Lists**: Converts numbered lists (e.g., `1. First item`) into an `<ol>` block.
- **Links**: Converts `[link text](url)` to `<a href="url">link text</a>`.
- **Images**: Converts `![alt text](src "optional title")` to an `<img>` tag, including support for an optional title attribute.
- **Code Blocks**: Wraps fenced code blocks (```) in `<pre><code class="language-xyz">...</code></pre>` tags for syntax highlighting.
- **Figure Wrapper**: Automatically wraps standalone images in a semantic `<figure>` tag.

## 🛠️ How to Run the Project

This project requires only Python 3. No external libraries need to be installed.

1.  **Single File Conversion**
    ```powershell
    python md_converter.py .\sample.md -o .\output.html
    ```

    - If `-o` is omitted, the output will be written next to the input as `.html`.
    - You can set a custom HTML title:
      ```powershell
      python md_converter.py .\sample.md -o .\output.html -t "My Doc"
      ```

2.  **Directory Conversion**
    Convert all `.md` files in a directory to `.html` files:
    ```powershell
    python md_converter.py .\docs -o .\public\docs
    ```

    Recurse into subdirectories:
    ```powershell
    python md_converter.py .\docs -o .\public\docs -r
    ```

3.  **Help**
    ```powershell
    python md_converter.py -h
    ```

4.  **View the Output**
    Open the generated `.html` files in any web browser.

## 📝 Example Usage

### Sample Input (`sample.md`)

````markdown
# My Project Documentation

This is a test of the _advanced features_ of the converter.

## Main Goals

1. Ensure code blocks are handled correctly.
2. Support ordered lists for step-by-step guides.
3. Make images semantically better with **figure tags**.

```python
# A simple function
def hello(name):
    print(f"Hello, {name}!")
```

This is an important diagram for our architecture.
![Digital System Diagram](https://media.geeksforgeeks.org/wp-content/uploads/20250228171646291248/Conceptual-Architecture-Diagram.webp "Architecture Diagram")

For more information, please visit the [official Python documentation](https://docs.python.org/3/).
````

### Generated Output (`output.html`)

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Converted Markdown</title>
  </head>
  <body>
    <h1>My Project Documentation</h1>

    <p>This is a test of the <em>advanced features</em> of the converter.</p>

    <h2>Main Goals</h2>

    <ol>
      <li>Ensure code blocks are handled correctly.</li>
      <li>Support ordered lists for step-by-step guides.</li>
      <li>
        Make images semantically better with <strong>figure tags</strong>.
      </li>
    </ol>

    <pre><code class="language-python"># A simple function
def hello(name):
    print(f&quot;Hello, {name}!&quot;)</code></pre>

    <p>
      This is an important diagram for our architecture.<br /><img
        src="https://media.geeksforgeeks.org/wp-content/uploads/20250228171646291248/Conceptual-Architecture-Diagram.webp"
        alt="Digital System Diagram"
        title="Architecture Diagram" />
    </p>

    <p>
      For more information, please visit the
      <a href="https://docs.python.org/3/">official Python documentation</a>.
    </p>
  </body>
</html>
```
