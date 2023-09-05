
def revers_h_string(hex_piece: str) -> str:
    """
    function creates revers string (hex piece of code)

    :param hex_piece: str
    :return: str - revers string
    """
    l = len(hex_piece)
    z = '0'
    if(l != 10):
        dl = 10-l-1
        for i in range(0, dl, 1):
            z = z + '0'
        hex_piece = hex_piece[0:2] + z + hex_piece[2:]
    
    l = len(hex_piece)
    revers = ""
    for i in range(l,0,-2):
        tmp=i-2
        revers= revers + hex_piece[tmp:i]
    
    return revers[:-2]

#hex_p = '0x6dfaa'
#h = revers_h_string(hex_p)

