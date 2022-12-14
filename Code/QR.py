import qrcode

data= "This is a test data"

img=qrcode.make(data)

img.save('C:/Users/KundanKumar/Desktop/Study/Code/qr_code.png')