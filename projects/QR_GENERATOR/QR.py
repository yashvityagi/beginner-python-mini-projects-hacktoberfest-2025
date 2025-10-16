import qrcode

data = "https://www.google.com/?zx=1760554724521&no_sw_cr=1"
img = qrcode.make(data)
img.save("qrcode.png")
print("QR code generated and saved as qrcode.png")
