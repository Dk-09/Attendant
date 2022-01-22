import socket
import os
import datetime

d = datetime.datetime.now()
d = d.strftime("%d %B %Y")

host = socket.gethostname()
port = 2222
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)

if not os.path.isdir('db'):
    os.system("mkdir db")
    os.chdir('db')
else:
    os.chdir('db')

f = open(d,'ab')
while True:
    msg, add = s.accept()
    while True:
        data = msg.recv(2000)
        while data:
            f.write(data)
            data = msg.recv(2000)
        f.close()
        break

