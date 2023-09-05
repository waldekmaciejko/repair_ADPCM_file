import os
from str_refers import revers_h_string

def repairADPCM_audio(n_iters=10, file_name='test.wav') -> None:
    """


    :param n_iters:
    :param file_name:
    :return:
    """

    flag = 1 # check if this is an initial run, 1 - yes, 0 - no

    p = os.path.join(os.getcwd(), file_name)
    file_name = os.path.basename(p)
    filen_name_no_ext = os.path.splitext(file_name)[0]
    only_path = os.path.dirname(p)

    for i in range(1, n_iters):
        if flag == 1:
            _filen_name = filen_name_no_ext+'_'+str(i)+'.wav'
            p_new = os.path.join(only_path, _filen_name)
            b = bytearray()
            with open(p, mode='rb') as file:
                fileContent = file.read()
                i = fileContent.find(b'\x64\x61\x74\x61') # find ascii: -data-, in hex: 64 61 74 61 atom in hex raw stream
                # b is the sum mof header from 0 offset to data offset  and from data to the end of file
                # without one sign after -data-
                b = fileContent[0:i+4] + fileContent[i+5:]

            roz = len(b)-8    # take the size of file without RIFF atom (4 bajts) and 4 bajts for size
            roz_h = hex(roz)  # take size of file in hex
            roz_bez_rev = revers_h_string(roz_h)  # do little endian
            bb = bytearray((bytes.fromhex(roz_bez_rev)))
            b = b[0:4] + bb + b[8:] # put the size file to byte array in right place

            with open(p_new, mode='wb') as newFile:
                newFile.write(b)
        else:
            p = p_new
            _filen_name = filen_name_no_ext +'_'+str(i)+'.wav'
            p_new = os.path.join(only_path, _filen_name)
            b = bytearray()
            with open(p, mode='rb') as file:
                fileContent = file.read()
                i = fileContent.find(b'\x64\x61\x74\x61')
                b = fileContent[0:i+4] + fileContent[i+5:]

            roz = len(b)-8    # 8 bo znacznik RIFF + aktualny rozmiar
            roz_h = hex(roz)
            roz_bez_rev = revers_h_string(roz_h)
            bb = bytearray((bytes.fromhex(roz_bez_rev)))
            b = b[0:4] + bb + b[8:]

            with open(p_new, mode='wb') as newFile:
                newFile.write(b)
        flag=0

if __name__ == "__main__":
    repairADPCM_audio()




    

    

    
