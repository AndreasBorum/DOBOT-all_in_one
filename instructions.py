from float_to_hex import IEEE754
import constants


def real_time_inst(data):
    type = type_func(data[0])
    ctrl = ctrl_func(data[0])
    id = id_func(data[0])
    params = params_func(data[1:])
    payload = payload_func(id, ctrl, type, params)
    payload_length = payload_length_func(payload)
    check_sum = check_sum_func(payload)
    return f"AA AA {payload_length} {payload} {check_sum}".upper()




def payload_length_func(payload):
    return hex(payload.count(' ')+1)[2:]


def ctrl_func(type):
    n= str(hex(0b1))[2:]
    if len(n)<2:
        n = "0"+n
    return n

def type_func(type:str):
    id=str(hex(constants.types.index(type)))[2:]
    if len(id)<2:
        id = "0"+id
    return id

def params_func(data):
    def add_space_func(n):
            res=f"{n[6:8]} {n[4:6]} {n[2:4]} {n[:2]}"
            return res

    x = add_space_func(IEEE754(float(data[0])))
    y = add_space_func(IEEE754(float(data[1])))
    z = add_space_func(IEEE754(float(data[2])))
    r = add_space_func(IEEE754(float(data[3])))
    return x+" "+y+" "+z+" "+r

    

def id_func(type:str):
    id=str(hex(constants.id[type]))[2:]
    return id

def check_sum_func(hex_string):
    hex_list = hex_string.split()
    decimal_list = [int(x, 16) for x in hex_list]
    sum_decimal = sum(decimal_list)
    two_compliment = (2**8 - sum_decimal) % (2**8)
    return hex(two_compliment)[2:]

def payload_func(id, ctrl, type, params):
    return id+" "+ctrl+" "+type+" "+params