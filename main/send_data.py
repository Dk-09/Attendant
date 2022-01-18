import socket
import datetime

def send():
    server = '3.7.135.69'
    port = 2222
    
    filename =  datetime.datetime.now()
    file_name = 'main/db1/' + filename.strftime("%d %B %Y")

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((server,port))

    f = open(file_name,'rb')
    data = f.read(2000)

    while data:
        s.send(data)
        data = f.read(2000)
    s.close()


