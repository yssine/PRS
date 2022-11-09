import socket

DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
FORMAT="utf-8"
PORT=8080
HEADER = 1024

syn, ack = "SYN".encode(FORMAT), "ACK".encode(FORMAT)

ADDR   = (SERVER, PORT)

def extract_port(s):
    return int(s.split()[-1])


def create_socket(port):
    addr=(SERVER, port)
    c=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    filename=input("Enter the filename you are looking for").encode(FORMAT)


    
 

# Create a UDP socket at client side
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 
# Send to server using created UDP socket
client.sendto(syn,ADDR)
servermsg = client.recvfrom(HEADER)
message=servermsg[0].decode("utf_8")
port=extract_port(message)
if message.split()[0][:7]=="ACK_SYN":
    create_socket(port)
 

msg = f"Message from Server: {message}"

print(msg)