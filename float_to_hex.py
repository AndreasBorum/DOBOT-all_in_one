import struct

def IEEE754(n: float) :
    # Use struct module to convert float to bytes
    bytes = struct.pack('>f', n)
    # Use int.from_bytes() to convert bytes to int
    # and convert to hex
    hex_str = hex(int.from_bytes(bytes, byteorder='big'))[2:]
    hex_str = hex_str.zfill(8)
    #print(hex_str)
    return hex_str