import qrcode
url = "https://photo-gallery-vtao.onrender.com"
img = qrcode.make(url)
img.save("qr_code.png")
