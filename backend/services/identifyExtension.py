def identifyExtension(file):
    magic_byte = file.read(8)
    magic_byte = bytes.hex(magic_byte)
    if magic_byte[:4] == "ffd8":
        return "JPEG"
    elif magic_byte == "89504e470d0a1a0a":
        return "PNG"
    elif magic_byte[:8] == "47494638":
        return "GIF"
    elif magic_byte[:10] == "255044462d":
        return "PDF"
    elif magic_byte[:8] == "504b0304":
        return "ZIP"
    elif magic_byte[8:16] == "ftypheic":
        return "HEIF"
    else: return "None"

