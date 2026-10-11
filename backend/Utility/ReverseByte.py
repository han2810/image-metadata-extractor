def reverseByte(string):
    length = len(string)
    correct_order = ""
    index = length - 2
    while index >= 0:
        correct_order += string[index:index+2]
        index -= 2
    return correct_order
