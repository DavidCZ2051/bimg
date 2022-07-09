from math import floor
from PIL import Image
import zlib

force = "" # "compression", "normal", ""

img = Image.open("img.png")
resolution = img.size[0]

# normal

def convert_24_to_8(red, green, blue):
    byte = (floor((red / 32)) << 5) + (floor((green / 32)) << 2) + floor((blue / 64))
    return byte

bytes = []

for x in range(resolution):
    for y in range(resolution):
        pixel = img.getpixel((x, y))
        bytes.append(convert_24_to_8(pixel[0], pixel[1], pixel[2]))

# compresion

def convert_24_to_8(red, green, blue):
    byte = (floor((red / 32)) << 5) + (floor((green / 32)) << 2) + floor((blue / 64))
    byte = hex(byte)[2:]
    if len(byte) == 1:
        byte = "0" + byte
    return byte

bytes2 = ""

for x in range(resolution):
    for y in range(resolution):
        pixel = img.getpixel((x, y))
        bytes2 = bytes2 + (convert_24_to_8(pixel[0], pixel[1], pixel[2]))

bytes2 = zlib.compress(bytes2.encode())

# building

def normal():
    print("Creating file using normal method...")
    bimg = open("bimgFromImg.bimg", "wb")
    bimg.write(bytearray(bytes))
    bimg.close()
    print("Done!")

def compressed():
    print("Creating file using compression method...")
    bimg = open("bimgcFromImg.bimgc", "wb")
    bimg.write(bytes2)
    bimg.close()
    print("Done!")

if force == "":
    if (len(bytes2) < len(bytes)):
        compressed()
    elif (len(bytes2) > len(bytes)):
        normal()
    else:
        normal()
elif force == "compression":
    compressed()
elif force == "normal":
    normal()