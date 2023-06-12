import  qrcode #install pip qrcode
qr = qrcode.QRCode(    #make object qr and define the box size you want
        version=1,
        box_size=10,
        border=5)

data="https://www.youtube.com/channel/UC_BIOy6FLEzWGEvvkczeutg" #add link for which you want to generate qr
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("myqrcode.jpg")
