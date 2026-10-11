with open ("test3.pdf","rb") as file:
    magic_byte = file.read(8)
magic_byte = bytes.hex(magic_byte)
if magic_byte[:4] == "ffd8":
    print("File is JPG/JPEG")
elif magic_byte == "89504e470d0a1a0a":
    print("File is PNG")
elif magic_byte[:8] == "47494638":
    print("File is GIF")
elif magic_byte[:10] == "255044462d":
    print("File is PDF")

