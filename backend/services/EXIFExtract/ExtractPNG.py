from Utility.HexToDec import hexToDec
def extractPNG(file):
    data = file.read()
    data = bytes.hex(data)
    pos = data.find("65584966")
    if pos != -1:
        length = data[pos-8:pos-1]
        size = hexToDec(length)
        return {"exif-size":size}
    else: return {"result":"false"}
    