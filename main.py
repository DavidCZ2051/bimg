import tkinter as tk
from tkinter import filedialog
from math import floor
import zlib
from math import sqrt
from PIL import Image

def convert_8_to_24(byte):
    byte = int(byte, 16)
    red = (byte >> 5) * 32
    green = ((byte & 28) >> 2) * 32
    blue = (byte & 3) * 64
    return (red, green, blue)

def convert_24_to_8(red, green, blue):
    byte = (floor((red / 32)) << 5) + (floor((green / 32)) << 2) + floor((blue / 64))
    return byte

def convert_24_to_8_c(red, green, blue):
    byte = (floor((red / 32)) << 5) + (floor((green / 32)) << 2) + floor((blue / 64))
    byte = hex(byte)[2:]
    if len(byte) == 1:
        byte = "0" + byte
    return byte

def from_bimg_to_gif(file_path):
    bimg = open(file_path, "rb")
    bytes = bimg.read().hex()
    bimg.close()

    size = int(len(bytes) / 2)
    resolution = int(sqrt(size))
    byte_array = [bytes[i:i+2] for i in range(0, len(bytes), 2)]

    img = Image.new("RGB", (resolution, resolution), color = "red")

    for x in range(resolution):
        for y in range(resolution):
            img.putpixel((x, y), convert_8_to_24(byte_array[x * resolution + y]))

    img.save("fromBimgToGif.gif", optimize=True)
    img.show()
    
def from_bimgc_to_gif(file_path):
    bimgc = open(file_path, "rb")
    bytes = bimgc.read()
    bimgc.close()

    bytes = zlib.decompress(bytes).decode()

    size = int(len(bytes) / 2)
    """ if size % 2 == 1:
        size += 1 """
    resolution = int(sqrt(size))
    byte_array = [bytes[i:i+2] for i in range(0, len(bytes), 2)]

    img = Image.new("RGB", (resolution, resolution), color = "red")

    for x in range(resolution):
        for y in range(resolution):
            img.putpixel((x, y), convert_8_to_24(byte_array[x * resolution + y]))

    img.save("fromBimgcToGif.gif", optimize=True)
    img.show()

def from_png_to_bimg(file_path):
    img = Image.open(file_path)
    resolution = img.size[0]

    bytes = []

    for x in range(resolution):
        for y in range(resolution):
            pixel = img.getpixel((x, y))
            bytes.append(convert_24_to_8(pixel[0], pixel[1], pixel[2]))

    return bytes

def from_png_to_bimgc(file_path):
    img = Image.open(file_path)
    resolution = img.size[0]

    bytes = ""

    for x in range(resolution):
        for y in range(resolution):
            pixel = img.getpixel((x, y))
            bytes = bytes + (convert_24_to_8_c(pixel[0], pixel[1], pixel[2]))

    bytes = zlib.compress(bytes.encode(), level=9)

    return bytes

def main():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=(("Image file", "*.png"), ("Bimg file", "*.bimg"), ("Compressed Bimg file", "*.bimgc"), ("All files", "*.*")))

    if file_path.endswith(".png"):
        x = input("Press 'n' to convert to normal bimg file\nPress 'c' to convert to compressed bimgc file\nPress 'a' to automatically decide\n")
        if x == "n":
            bytes = from_png_to_bimg(file_path)
            bimg = open("fromPngtoBimg.bimg", "wb")
            bimg.write(bytearray(bytes))
            bimg.close()
            print("Done!")
        elif x == "c":
            bytes = from_png_to_bimgc(file_path)
            bimgc = open("fromPngToBimgc.bimgc", "wb")
            bimgc.write(bytes)
            bimgc.close()
            print("Done!")
        elif x == "a":
            bytes = from_png_to_bimg(file_path)
            bytes_c = from_png_to_bimgc(file_path)
            if (len(bytes_c) < len(bytes)):
                bimgc = open("fromPngToBimgc.bimgc", "wb")
                bimgc.write(bytes_c)
                bimgc.close()
                print("Done! Used compressed bimgc file")
            elif (len(bytes_c) > len(bytes)):
                bimg = open("fromPngtoBimg.bimg", "wb")
                bimg.write(bytearray(bytes))
                bimg.close()
                print("Done! Used normal bimg file")
            else:
                bimg = open("fromPngtoBimg.bimg", "wb")
                bimg.write(bytearray(bytes))
                bimg.close()
                print("Done! Used normal bimg file")
        else:
            print("Invalid input")
            exit()
    elif file_path.endswith(".bimg"):
        from_bimg_to_gif(file_path)
        print("Done!")
    elif file_path.endswith(".bimgc"):
        from_bimgc_to_gif(file_path)
        print("Done!")
    elif file_path == "":
        exit()
    else:
        print("File format not supported!")
        exit()

if __name__ == "__main__":
    main()