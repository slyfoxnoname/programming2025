def binary_to_hex(binary):
    hex_map = {
        "0000": "0", "0001": "1", "0010": "2", "0011": "3",
        "0100": "4", "0101": "5", "0110": "6", "0111": "7",
        "1000": "8", "1001": "9", "1010": "A", "1011": "B",
        "1100": "C", "1101": "D", "1110": "E", "1111": "F"
    }
    while len(binary) % 4 != 0:
        binary = '0' + binary

    stack = []
    for i in range(0, len(binary), 4):
        chunk = binary[i:i+4]
        stack.append(hex_map[chunk])

    hex_number = ''.join(stack).lstrip('0')
    return hex_number if hex_number else '0'

binary_input = input().strip()
print(binary_to_hex(binary_input))
