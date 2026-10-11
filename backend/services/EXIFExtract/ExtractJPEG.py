from Utility.HexToDec import hexToDec
from Utility.extractIFD import extractIFD
def validAPP1Segment(pos, data):
    app1_header = data[pos+8:pos+20]
    app1_header2 = data[pos+8:pos + 64]
    if app1_header == "457869660000":
        return 1
    elif app1_header2 == "687474703a2f2f6e732e61646f62652e636f6d2f7861702f312e302f":
        return 2
    else: return -1
    
def extractExifData(pos, data):
    hex_exif_Length = data[pos+4:pos+8]
    exif_Length = hexToDec(hex_exif_Length) - 2
    return (data[pos+8+(exif_Length*2):pos+8+(exif_Length*2)+4])

def extractTIFFHeader(pos, data):
    byte_order = data[pos+20:pos+24]
    hex_offset_byte_IFD = data[pos+28:pos+36]
    offset_byte_to_IFD0 = hexToDec(hex_offset_byte_IFD,byte_order)
    tiff_header_pos = pos + 20
    ifd0_pos = tiff_header_pos + (offset_byte_to_IFD0 * 2)
    return {"byte_order":byte_order, "ifd0_pos":ifd0_pos, "tiff_header_pos":tiff_header_pos}

def findMetadataSegment(data):
    metadataPosArray = {
        "exif_pos": -1,
        "xmp_pos": -1,
        "iptc_pos": -1
    }
    index = 0
    condition = 20
    while condition > 0:
        app1_pos = data.find("ffe1",index)
        app13_pos = data.find("ffed",index)
        if app1_pos == -1 and app13_pos == -1: 
            break
        if app1_pos != -1:
            if validAPP1Segment(app1_pos,data) == 1:
                metadataPosArray["exif_pos"] = app1_pos
                index = index + 4 + (hexToDec(data[app1_pos + 4: app1_pos + 8],"1")) * 2
            elif validAPP1Segment(app1_pos,data) == 2:
                metadataPosArray["xmp_pos"] = app1_pos
                index = index + 4 + (hexToDec(data[app1_pos + 4: app1_pos + 8],"1")) * 2
            else: 
                index = app1_pos + 4
        if app13_pos != -1: 
            app13_pos = -1
        condition -= 1
    return metadataPosArray

def extractJPEG(file):
    file.seek(0)
    byte_data = file.read()
    data = byte_data.hex()
    exif_pos = -1
    xmp_pos = -1
    result = []
    metadataPosArray = findMetadataSegment(data)
    for key, value in metadataPosArray.items():
        if key == "exif_pos" and value != -1:
            exif_pos = value
        if key == "xmp_pos" and value != -1:
            xmp_pos = value
    if exif_pos != -1:
        tiff_header_data = extractTIFFHeader(exif_pos,data)
        ifd0_pos = tiff_header_data["ifd0_pos"]
        byte_order = tiff_header_data["byte_order"]
        tiff_header_pos = tiff_header_data["tiff_header_pos"]
        result = extractIFD(ifd0_pos,byte_order,data, tiff_header_pos)
    if xmp_pos != -1:
        result.append({"name":"xmp","value":"Known"})
    if result:
        return result
    else:
        return [{"name": "Metadata", "value": "Not found"}]
    
        