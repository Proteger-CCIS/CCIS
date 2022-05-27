import cv2
import numpy as np
from PIL import Image

#it convert data in binary formate

print(r""" _______     _______    _________    _______ 
(  ____ \   (  ____ \   \__   __/   (  ____ \
| (    \/   | (    \/      ) (      | (    \/
| |         | |            | |      | (_____ 
| |         | |            | |      (_____  )
| |         | |            | |            ) |
| (____/\ _ | (____/\ _ ___) (___ _ /\____) |
(_______/(_)(_______/(_)\_______/(_)\_______)""")
print("\n****************************************************************")
print(r"""+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|I|M|A|G|E| |S|T|E|G|A|N|O|G|R|A|P|H|E|R|
+-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+""")
print("\n* Developed by Team Proteger *")


def data2binary(data):
    if type(data) == str:
        p = ''.join([format(ord(i), '08b')for i in data])
    elif type(data) == bytes or type(data) == np.ndarray:
        p = [format(i, '08b')for i in data]
    return p


# hide data in given img

def hidedata(img, data):
    data += "$$"                                   #'$$'--> secrete key
    d_index = 0
    b_data = data2binary(data)
    len_data = len(b_data)

 #iterate pixels from image and update pixel values

    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            if d_index < len_data:
                pix[0] = int(r[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[1] = int(g[:-1] + b_data[d_index])
                d_index += 1
            if d_index < len_data:
                pix[2] = int(b[:-1] + b_data[d_index])
                d_index += 1
            if d_index >= len_data:
                break
    return img


def encode():
    img_name = input("\nEnter image name followed by file format:")
    image = cv2.imread(img_name)
    img = Image.open(img_name, 'r')
    w, h = img.size
    data = input("\nEnter message to hide:")
    if len(data) == 0:
        raise ValueError("Empty data")
    enc_img = input("\nEnter encoded image name followed by file format:")
    enc_data = hidedata(image, data)
    cv2.imwrite(enc_img, enc_data)
    img1 = Image.open(enc_img, 'r')
    img1 = img1.resize((w, h),Image.ANTIALIAS)
    # optimize with 65% quality
    if w != h:
        img1.save(enc_img, optimize=True, quality=65)
    else:
        img1.save(enc_img)

# decoding

def find_data(img):
    bin_data = ""
    for value in img:
        for pix in value:
            r, g, b = data2binary(pix)
            bin_data += r[-1]
            bin_data += g[-1]
            bin_data += b[-1]

    all_bytes = [bin_data[i: i + 8] for i in range(0, len(bin_data), 8)]

    readable_data = ""
    for x in all_bytes:
        readable_data += chr(int(x, 2))
        if readable_data[-2:] == "$$":
            break
    return readable_data[:-2]


def decode():
    img_name = input("\nEnter Image name : ")
    image = cv2.imread(img_name)
    img=Image.open(img_name,'r')
    msg = find_data(image)
    return msg


def stegnography():
    x = 1
    while x != 0:
       print('''\nChoose option to perform :
       1.encode
       2.decode''')
       u_in = int(input("\n Enter your choice:"))
       if u_in == 1:
           encode()
       else:
           ans = decode()
           print("\n your message:"+ans)
       x = int(input("\nTo continue enter 1 ELSE to exit enter 0:"))


stegnography()