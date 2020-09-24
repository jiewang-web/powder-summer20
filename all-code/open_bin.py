import struct

#file = open('bin_power1','rb')

#byte = file.read(1)
#while byte:
#    print(byte)
#    byte = file.read(1)

with open('bin_power1', mode='rb') as file:
    fileContent = file.read()
#    length = len(fileContent))
#    length2 = length // 4
    x = struct.unpack('f' * (len(fileContent) // 4), fileContent)
    print(x)
#    print(fileContent)
