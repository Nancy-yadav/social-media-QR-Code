import qrcode
import qrcode.constants
img= "https://www.youtube.com/@ScholarAarti"
qr =qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10,border=4,)
qr.add_data(img)
qr.make(fit=True)
img = qr.make_image(fill_color="black",back_color="White")
img.save("qr_code.png")