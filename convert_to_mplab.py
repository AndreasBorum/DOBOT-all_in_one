
def convert(instrucktion):
    s = instrucktion[0]
    groups = s.split()
    temp = ""
    for group in groups:
        temp += "0x" + group + ", "
    res = temp.strip()
    res += " 0xFF"
    return res

def make_lookuptable(s, x):
    look_string = f"LOOK{x}\n\taddwf\tPCL, F\n\tDT\t\t{s}"
    return look_string


def make_all_make_lookuptables(data):
    res = ""
    for row in data:

        res +=f";{row[0]}\n"+row[2]+"\n\n"
    return res

