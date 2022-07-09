from math import sqrt
from PIL import Image
import zlib

try: # normal
    bimg = open("img.bimg", "rb")
    bytes = bimg.read().hex()
    bimg.close()

    size = int(len(bytes) / 2)
    resolution = int(sqrt(size))
    byte_array = [bytes[i:i+2] for i in range(0, len(bytes), 2)]

    def convert_8_to_24(byte):
        byte = int(byte, 16)
        red = (byte >> 5) * 32
        green = ((byte & 28) >> 2) * 32
        blue = (byte & 3) * 64
        return (red, green, blue)

    img = Image.new("RGB", (resolution, resolution), color = "red")

    for x in range(resolution):
        for y in range(resolution):
            img.putpixel((x, y), convert_8_to_24(byte_array[x * resolution + y]))

    # building

    print("Creating file using normal method...")

    img.save("imgFromBimg.gif", optimize=True)
    img.show()

except: # compression
    bimg = open("img.bimgc", "rb")
    bytes2 = bimg.read()
    bimg.close()

    bytes2 = zlib.decompress(bytes2).decode()

    size = int(len(bytes2) / 2)
    """ if size % 2 == 1:
        size += 1 """
    resolution = int(sqrt(size))
    byte_array2 = [bytes2[i:i+2] for i in range(0, len(bytes2), 2)]

    def convert_8_to_24(byte):
        byte = int(byte, 16)
        red = (byte >> 5) * 32
        green = ((byte & 28) >> 2) * 32
        blue = (byte & 3) * 64
        return (red, green, blue)

    img = Image.new("RGB", (resolution, resolution), color = "red")

    for x in range(resolution):
        for y in range(resolution):
            img.putpixel((x, y), convert_8_to_24(byte_array2[x * resolution + y]))

    # building

    print("Creating file using compression method...")

    img.save("imgFromBimgc.gif", optimize=True)
    img.show()

finally:
    print("Done!")
