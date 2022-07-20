
# https://www.py4e.com/lessons/network
import socket
import tim

HOST = 'data.pr4e.org' #linking another website
PORT = 80 #for http constant
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#takes the data
mysock.connect((HOST, PORT))#connecting the host and the port
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')#takes all the data from the website or url
count = 0
picture = b""#b meaning break

while True:
    data = mysock.recv(5120)#5120 is no. of characters allowed to be entered
    if len(data) < 1: break # if its >1 it cant input 5120 characters
    #time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data

mysock.close()

pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos].decode())

picture = picture[pos+4:]
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()
