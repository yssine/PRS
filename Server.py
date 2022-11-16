import socket
import threading
import pickle
import os
import platform
from glob import glob as g




DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
FORMAT="utf-8"
PORT = 8080
HEADER = 1024
CONNECTIONS=1024
PORTS=[0]*CONNECTIONS

PATH="./DB/"
if platform.system()=="Windows":
    PATH= ".\\DB\\"

# print(PORTS[:5])
 
def create_socket(port):
    PORTS[port-8081]=1
    s=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.bind((SERVER, port))
    filename,conn=s.recvfrom(HEADER)
    local_path=PATH+filename.decode(FORMAT)
    print(g(local_path))
    if g(local_path):
        s.sendto( "ACK_FILENAME".encode(FORMAT),conn)
    else:
        s.sendto( "DOES NOT EXIST".encode(FORMAT),conn)
        disc=s.recvfrom(HEADER)[0].decode(FORMAT)
        if disc==DISCONNECT_MESSAGE:
            print(disc)
            s.sendto( "ACK_DISC".encode(FORMAT),conn)
            s.close()
            PORTS[port-8081]=0
    # files=g(filename.decode(FORMAT))
    # s.sendto( pickle.dumps(files),conn)



def get_port():
    for i in range(CONNECTIONS):
        if not PORTS[i]:
            return 8081+i



# Create a datagram socket
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
server.bind((SERVER, PORT))



# def rec(s):
#     msg_length = s.recvfrom(HEADER)[1].decode(FORMAT)
#     if msg_length:
#         msg_length = int(msg_length)
#         msg = s.recvfrom(msg_length)[1].decode(FORMAT)
#         return msg

# def snd(s,conn,msg):
#     s.sendto(len(msg),conn)


# def handle_client(conn, addr):
#     print(f"[NEW CONNECTION] {addr} connected.")

#     connected = True
#     while connected:
#         msg_length = conn.recv(HEADER).decode(FORMAT)
#         if msg_length:
#             msg_length = int(msg_length)
#             msg = conn.recv(msg_length).decode(FORMAT)
#             if msg == DISCONNECT_MESSAGE:
#                 connected = False

#             print(f"[{addr}] {msg}")
#             conn.send("Msg received".encode(FORMAT))

#     conn.close()
        

def start():
    # server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}...")
    while True:
        msg,conn=server.recvfrom(HEADER)
        msg=msg.decode(FORMAT)
        # print(msg)
        if msg=="SYN":
            port=get_port()
            thread = threading.Thread(target=create_socket, args=(port,))
            thread.start()
            server.sendto(f"ACK_SYN {port}".encode(FORMAT),conn)
            msg=server.recvfrom(HEADER)[0].decode(FORMAT)
            # print(msg)
            if msg=="ACK":
                pass






        
        
        # print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")



print(f"PWD: {os.getcwd()}")

print("[STARTING] server is starting...")
start()
