from math import floor

x = input("Press 1 to convert 8-bit color to 24-bit\nPress 2 to convert 24-bit color to 8-bit")

def convert_8_to_24(byte):
    byte = int(byte, 16)
    red = (byte >> 5) * 32
    green = ((byte & 28) >> 2) * 32
    blue = (byte & 3) * 64
    return (red, green, blue)

def convert_24_to_8(red, green, blue):
    byte = (floor((red / 32)) << 5) + (floor((green / 32)) << 2) + floor((blue / 64))
    byte = hex(byte)[2:]
    if len(byte) == 1:
        byte = "0" + byte
    return byte

if x == "1":
    x = input("Enter a byte: ")
    print(f"(red, green, blue): {convert_8_to_24(x)}")
    exit()
elif x == "2":
    red = int(input("Enter red: "))
    green = int(input("Enter green: "))
    blue = int(input("Enter blue: "))
    print(f"Byte: {convert_24_to_8(red, green, blue)}")
    exit()
else:
    print("Invalid input")
    exit()
