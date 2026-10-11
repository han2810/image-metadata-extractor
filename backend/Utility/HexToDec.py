from Utility.ReverseByte import reverseByte
def hexToDec(string, byte_order):
    if byte_order  == "4949" and len(string) > 2:
        string = reverseByte(string)
    leng = len(string)
    sum = 0
    index = 0
    for i in range(leng - 1, -1, -1):
        number = ord(string[i])
        if number >= 48 and number <= 57:
            number -= 48
            sum += number * 16**index
            index += 1
        else:
            number -= 87
            sum += number * 16**index
            index += 1
    return sum
       
    