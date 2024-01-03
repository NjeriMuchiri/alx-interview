#!/usr/bin/python3

def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    bytes_to_check = 0

    for num in data:
        if bytes_to_check == 0:
            if num >> 7 == 0b0:
                continue
            elif num >> 5 == 0b110:
                bytes_to_check = 1
            elif num >> 4 == 0b1110:
                bytes_to_check = 2
            elif num >> 3 == 0b11110:
                bytes_to_check = 3
            else:
                return False
        else:
            if num >> 6 != 0b10:
                return False
            bytes_to_check -= 1

    return bytes_to_check == 0


if __name__ == "__main__":
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False
