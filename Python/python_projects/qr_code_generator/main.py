import qrcode
data=input("Enter the Text or URL : ").strip() # to get rid of any white spaces on the url 
file_name=input("Enter the file name you want to save with : ").strip()
qr=qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image=qr.make_image(fill_color="black",back_color="white")
image.save(file_name)
print(f"Your Qr code is succesfully saved as {file_name}")
