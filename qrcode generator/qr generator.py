import qrcode
import image

qr = qrcode.QRCode(
    version = 15,   #15 means version of qr code . Higher the number bigger the code image
    box_size = 5,  # size of the box where qr code would be displayed
    border = 5        # It si white part of the image---- border in all four sides with white color
    
)

# path of the youtube channel

data = "https://www.linkedin.com/in/ankita-gajbhiye-785b7747/"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("test_small1.png")
                    
