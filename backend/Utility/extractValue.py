from Utility.HexToDec import hexToDec
import struct
def hexToAscii(string):
    index = 0
    length = len(string)
    if length <= 2 or string == "0000":
        return "Empty"
    value = ""
    while index < length - 2:
        ascii_code = hexToDec(string[index: index + 2],"1")
        value += chr(ascii_code)
        index += 2
    return value

def hexToInt(string, byte_order, count, entry_size):
    if count == 1:
        value = hexToDec(string,byte_order)
        return value
    else: 
        values = []
        type_size = int(entry_size / count)
        index = 0
        for i in range(count):
            value = string[index : index + (type_size*2)]
            values.append(hexToDec(value,byte_order))
            index += type_size * 2
        return values

def hexToSignedInt(string, byte_order, count, entry_size,entry_type):
    exponent = {6:8, 8:16,9:32}
    if count == 1:
        value = hexToDec(string,byte_order) - 2**exponent[entry_type]
        return value
    else: 
        values = []
        type_size = int(entry_size / count)
        index = 0
        for i in range(count):
            value = string[index : index + (type_size*2)]
            value = hexToDec(value,byte_order) - 2**exponent[entry_type]
            values.append(value)
            index += type_size * 2
        return values

def hexToRational(string, byte_order, count):
    if count == 1:
        numerator   = hexToDec(string[0:8] ,byte_order)
        denominator = hexToDec(string[8:16],byte_order)
        return numerator / denominator
    else:
        results = []
        index = 0
        for i in range(count):
            numerator   = hexToDec(string[index:index + 8] ,byte_order)
            denominator = hexToDec(string[index + 8:index + 16],byte_order)
            results.append(numerator / denominator)
            index += 16
        return results

def hexToFloat(string, byte_order):
    string = bytes.fromhex(string)
    if byte_order == "4949":
        return struct.unpack("<f",string)
    else:
        return struct.unpack(">f",string)
    
def hexToDouble(string, byte_order):
    string = bytes.fromhex(string)
    if byte_order == "4949":
        return struct.unpack("<d",string)
    else:
        return struct.unpack(">d",string)
    
def hexToSRational(string, byte_order):
    string = bytes.fromhex(string)
    if byte_order == "4949":
        numerator,  denominator = struct.unpack("<ii",string)
        return numerator / denominator
    else:
        numerator, denominator = struct.unpack(">ii",string)
        return numerator / denominator

def extractValue(data,entry_data_pos ,entry_size, entry_data, entry_type, tiff_header_pos, byte_order, count):
    if (entry_size > 4):
        offset = hexToDec(entry_data,byte_order)
        value_pos = tiff_header_pos + (offset * 2)
        entry_data = data[value_pos: value_pos + (entry_size * 2)]
    else: 
        entry_data = data[entry_data_pos: entry_data_pos + (entry_size * 2)]
    if entry_type == 2:
        return hexToAscii(entry_data)
    elif entry_type == 5:
        return hexToRational(entry_data,byte_order,count)
    elif entry_type == 1  or entry_type == 3 or entry_type == 4:
        return hexToInt(entry_data, byte_order, count, entry_size)
    elif entry_type == 6 or entry_type == 8 or entry_type == 9:
        return hexToSignedInt(entry_data, byte_order, count, entry_size,entry_type)
    elif entry_type == 10:
        return hexToSRational(entry_data,byte_order)
    elif entry_type == 11:
        return hexToFloat(entry_data,byte_order)
    elif entry_type == 12:
        return hexToDouble(entry_data,byte_order)
    else: 
        return "None"
        
        