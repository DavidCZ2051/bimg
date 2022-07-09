import zlib

file = open("test.txt", "r")
data = file.read()
file.close()

zip = zlib.compress(data.encode())

file = open("zip.txt", "wb")
file.write(zip)
file.close()

print(zlib.decompress(zip).decode())  # outputs original contents of a