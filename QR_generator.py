import qrcode

message=input("Enter your name or a short message:")

img=qrcode.make(message)
img.save("my_message_qrcode.png")

print("Message QR code saved successfully!")

website=input("Enter your favorite website URL:")

img=qrcode.make(website)
img.save("my_website_qrcode.png")

print("Website QR code saved successfully!")