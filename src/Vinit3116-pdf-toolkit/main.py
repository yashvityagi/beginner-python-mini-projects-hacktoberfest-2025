from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown

console = Console()

console.print("=== PDF MERGE TOOL ===", style="bold cyan")

# Ask user for PDF files input
file_input = console.input("Enter PDF paths separated by commas:")
file_list = [f.strip() for f in file_input.split(',')]

valid_pdfs = []

for file in file_list:
    path = Path(file)
    if not path.is_file():
        console.print(f"❌ Skipping: {file} (File does not exist)", style="bold red")
        continue
    if path.suffix.lower() != ".pdf":
        console.print(f"⚠ Skipping: {file} (Not a PDF)", style="yellow")
        continue
    try:
        reader = PdfReader(str(path), strict=False)
        valid_pdfs.append((path, reader))
        console.print(f"✅ Loaded: {file} ({len(reader.pages)} page(s))", style="green")
    except Exception as e:
        console.print(f"❌ Failed to load {file}: {e}", style="bold red")

if not valid_pdfs:
    console.print("❌ No valid PDFs to merge. Exiting.", style="bold red")
    exit(1)

# Merge PDFs
writer = PdfWriter()
total_pages = 0
for path, reader in valid_pdfs:
    for page in reader.pages:
        writer.add_page(page)
    total_pages += len(reader.pages)

output_file = "merged_output.pdf"
with open(output_file, 'wb') as f:
    writer.write(f)

console.print(f"\n📄 Total pages merged: {total_pages}", style="cyan")
console.print(f"✅ Saved output as: {output_file}", style="bold green")
console.print("Developed by @Vinit3116 👨‍💻", style="bold magenta")