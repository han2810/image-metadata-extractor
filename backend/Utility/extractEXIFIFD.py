from Utility.HexToDec import hexToDec
from Utility.tagIDTable import tags
from Utility.tagIDTable import type_size
from Utility.ReverseByte import reverseByte
from Utility.extractValue import extractValue
def extractEntryCount(ifd_pos, byte_order, data):
    hex_entry_count = data[ifd_pos: ifd_pos + 4] # 2 byte cho so luong
    entry_count = hexToDec(hex_entry_count, byte_order)
    return entry_count

def extractIFDEntry(entry_pos, data, byte_order, tiff_header_pos):
    tagID = data[entry_pos: entry_pos + 4]
    if byte_order == "4949":
        tagID = reverseByte(tagID)
    tagIDName = tags["EXIF"].get(tagID.upper())
    if (tagIDName): 
        tagIDName = tagIDName.get("name")
    else: 
        return {"name": tagID, "value": "Unknown" }
    hex_type_entry = data[entry_pos + 4: entry_pos + 8]
    entry_type = hexToDec(hex_type_entry,byte_order)
    hex_count = data[entry_pos + 8: entry_pos + 16]
    count = hexToDec(hex_count, byte_order)
    entry_size = type_size.get(entry_type) * count
    entry_data = data[entry_pos + 16: entry_pos + 24]
    entry_data_pos = entry_pos + 16
    entry_value = extractValue(data,entry_data_pos ,entry_size, entry_data, entry_type, tiff_header_pos,byte_order, count)
    return {"name":tagIDName, "entry_size":entry_size, "value": entry_value, "entry_type":entry_type, "byte_order":byte_order, "entry_count":count}  

def extractEXIFIFD(ifd_pos, byte_order, data, tiff_header_pos):
    entry_count = extractEntryCount(ifd_pos, byte_order,data)
    tagIDNames =  []
    entry_pos = ifd_pos + 4
    for i in range(entry_count):
        tagIDNames.append(extractIFDEntry(entry_pos,data,byte_order, tiff_header_pos))
        entry_pos += 24
    return tagIDNames