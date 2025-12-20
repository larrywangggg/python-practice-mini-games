import qrcode

url = "https://x.com"
img_file = "./qrcode/qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)
img = qr.make_image(back_color="silver", fill_color="purple")
img.save(img_file)
