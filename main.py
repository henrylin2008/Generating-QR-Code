# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import qrcode


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
def encode_qr_code(data):
    data = "Please visit the site: https://google.com"
    img = qrcode.make(data)     # Encode the link
    print(type(img))
    img.save("image1.jpg")

# How QR Code display
# qr = qrcode.QRCode(
#     version=1,  # matrix size of the QR code
#     error_correction=qrcode.constants.ERROR_CORRECT_L,  # analyze the error connection attribute
#     box_size=10,  # pixel size of each box
#     border=4,   # border thickness
# )

def decoding_qr_code(qr):
    decoder = cv2.QRCodeDetector()
    file = "image1.jpg"
    image = cv2.imread(file)
    link, data_points, straight_qrcode = decoder.detectAndDecode(image)
    print(link)


if __name__ == '__main__':
    encode_qr_code(data="https://google.com")
    decoding_qr_code(qr="image1.jpg")
