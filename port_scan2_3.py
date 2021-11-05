from socket import *
import time
import os
import os.path
from os import path

host = ''
port = 10088 #接口必须一致
bufsize = 2048
addr = (host,port) 

udpServer = socket(AF_INET,SOCK_DGRAM)
udpServer.bind(addr) #开始监听


while True:
    print('Waiting for connection...')
    data,addr = udpServer.recvfrom(bufsize)  #接收数据和返回地址

    #print(data)
    # create a new file name
    timer = time.ctime()
    # Converting the string to a time object
    t_obj = time.strptime(timer)
    # Transforming the time object to a timestamp
    # of ISO 8601 format
    form_t = time.strftime("%Y-%m-%d_%H-%M-%S", t_obj)

    fl2wrt = open('tmp.txt', 'w')
    #处理数据
    
    barr = bytearray(20)
    strarr = []
    cn = 0

    for byts in data:
        barr[cn] = byts
        print(byts)
        strarr.append(byts)
        cn += 1
    
    for elem in strarr:
        fl2wrt.write(str(elem) + "\n")
    fl2wrt.close()

    cpath = os.getcwd()
    # If the file already exists, skip renaming
    if path.exists(form_t + '.txt'):
        continue
    else:
        os.rename(cpath +'/tmp.txt',  cpath + '/' + form_t + '.txt' )

    #print(timer)
    #udpServer.sendto(data.encode(encoding='utf-8'),addr)
    #发送数据
    #f_path, os.path.split(f_path)[0] + '/' + form_t + os.path.splitext(f_path)[1])
    #print('...recevied from and return to :',addr)

udpServer.close()
