def convert(var):
    binary_int = int(var, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    return ascii_text

import socket

host = socket.gethostname()
port = 5555  

socket_server = socket.socket()
socket_server.bind((host, port))

socket_server.listen(2)

while True:

    conn, address = socket_server.accept()

    while True:
        packet_data = conn.recv(1024).decode()

        if not packet_data:
            break
        var=packet_data
        Key ='1001'
        print(var)

        def xor(a, b):
 
            result = []

            for i in range(1, len(b)):
                 if a[i] == b[i]:
                    result.append('0')
                 else:
                    result.append('1')
 
            return ''.join(result)
        def mod2div(divident, divisor):
 
            pick = len(divisor)

            tmp = divident[0 : pick]
 
            while pick < len(divident):
 
                if tmp[0] == '1':
 
           
                    tmp = xor(divisor, tmp) + divident[pick]
 
                else:
                    tmp = xor('0'*pick, tmp) + divident[pick]
 
                pick += 1
 
            if tmp[0] == '1':
                tmp = xor(divisor, tmp)
            else:
                tmp = xor('0'*pick, tmp)
 
            checkword = tmp
            return checkword
        key2=mod2div(var , Key)
        print(key2)
        var1=len(key2)
        count=0
        i=0
        while i<var1:
            if key2[i]=='0':
                count+=1

            i+=1
        if count==var1:
            print("YES")
            # print(var)
            var6=var[0:len(var)-(len(Key)-1)]
            var5=convert(var6)
            print(var5)
        else:
            print("NO")

    conn.close()