# TCP

import socket

# esto da la ip local // fuente: https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
HOST = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
PORT = 2424

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(True)

conn, addr = s.accept()
print("Connection address: ", addr)
while True:
    data = conn.recv(1024)
    if not data: break
    print("Received data: ", data)
    respuestastr = data.decode() + " xd"
    respuestabytes = respuestastr.encode()
    conn.send(respuestabytes)
conn.close()
