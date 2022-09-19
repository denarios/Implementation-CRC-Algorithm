import random
temp=random.randint(0,9)
temp2=random.randint(0,9)
input_string = input("Enter message: ")
 
div = (''.join('0'+format(ord(x), 'b') for x in input_string))
Key ='1001'
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


def encodeData(data, key):
    appended_data = data + '0'*(key-1)
    return appended_data

ans = encodeData(div,len(Key)) 
key2=mod2div(ans , Key)
print(Key)
print("Remainder : ",key2)
key3=div+key2

print(key3)
myList=list(key3)
flag=0
if temp%2!=0 :
    flag=1

length=len(div)+len(Key)
temp3=0
if flag==1 :
    temp3=temp2%length
    
    if temp3!=0:
        if myList[temp3-1]=='1':
            myList[temp3-1]='0'
        else:
            myList[temp3-1]='1'
    key3=''.join(myList)
    print(key3)

import socket

host = socket.gethostname()
port = 5555

socket_client = socket.socket()
socket_client.connect((host, port))

message = key3
# while message.lower().strip() != 'quit':
socket_client.send(message.encode())
data = socket_client.recv(1024).decode()
while data=="NAK":
    if temp%2!=0 :
        flag=1
    temp4=0
    if flag==1 :
        temp4=temp2%length
    if temp4!=0:
        if myList[temp4-1]=='1':
            myList[temp4-1]='0'
        else:
            myList[temp4-1]='1'
        key5=''.join(myList)
    message1 = key5
    socket_client.send(message1.encode())
    data=socket_client.recv(1024).decode()
socket_client.close()
