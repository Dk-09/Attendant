import socket
import datetime

def send():
    server = '65.1.117.206'
    port = 2222
    socketTimeout = 5

    filename =  datetime.datetime.now()
    file_name = 'main/db1/' + filename.strftime("%d %B %Y")

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(socketTimeout)

    result = s.connect_ex((server,port))
    if result == 0:
        s.connect((server,port))

        f = open(file_name,'rb')
        data = f.read(2000)

        while data:
            s.send(data)
            data = f.read(2000)
        s.close()
    else:
        return 1


