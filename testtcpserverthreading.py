# import socket programming library 
import socket   
# import thread module 
from _thread import start_new_thread
import threading 
  
# thread function 
def threaded(conn): 
    while True: 
        data = conn.recv(1024)
        if not data:
            break
        #print("Received data: ", data) PARA ESTO SE PRECISA SEMAFORO
        respuestastr = data.decode() + " xd"
        respuestabytes = respuestastr.encode()
        conn.send(respuestabytes)

    # connection closed 
    conn.close() 
  
  
def Main(): 
    HOST = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
    PORT = 2424

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    while True: 
        # establish connection with client 
        conn, addr = s.accept()

        print('Connected to: ', addr[0], ':', addr[1]) 
  
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (conn,)) 
    s.close() 
  
  
if __name__ == '__main__': 
    Main() 
