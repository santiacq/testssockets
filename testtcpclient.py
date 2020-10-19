import socket 
 
IPSERVER = "192.168.1.46"
PORT = 2424
MSGstr = "Vamo peniarol y bokita"
MSG = MSGstr.encode()
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IPSERVER, PORT))
s.send(MSG)
data = s.recv(1024)
s.close()
print("Received data:", data)