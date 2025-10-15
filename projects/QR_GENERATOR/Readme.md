📦 QR Code Generator — Python

A lightweight and efficient QR Code Generator built with Python.
This project allows you to easily convert any text or URL into a QR code image in just a few lines of code.

🚀 Features

🔹 Generate QR codes instantly

🔹 Save QR codes as high-quality .png images

🔹 Supports URLs, plain text, and any string input

🔹 Lightweight and beginner-friendly project

🧰 Tech Stack

Language: Python 3

Library: qrcode[pil]

⚙️ Installation

Clone the repository

git clone https://github.com/yourusername/qr-code-generator.git
cd qr-code-generator


Install dependencies

pip install qrcode[pil]

🧠 Usage

Run the Python script to generate your QR code:

python qr_generator.py

Example Code
import qrcode

data = "https://example.com"
img = qrcode.make(data)
img.save("qrcode.png")
print("QR code generated and saved as qrcode.png")


After running the script, a file named qrcode.png will be created in the same directory.
You can open it using any image viewer or scan it directly with your mobile device.

🖼️ Example Output
Input Data	Generated QR Code
https://goggle.com


🧩 Customization


You can modify the data variable in the script:

data = "Hello, Srishti!"


You can also change colors, error correction, and size using:

import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://example.com")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("custom_qr.png")

📄 License

This project is licensed under the MIT License — feel free to use and modify it for personal or professional projects.

💬 Author

Srishti Kumari
🎓 B.Tech CSE (DATA SCIENCE) — Haldia Institute of Technology