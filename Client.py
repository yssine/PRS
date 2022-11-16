import socket
import pickle
import sys



SERVER = "127.0.0.1"
FORMAT="utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT".encode(FORMAT)
PORT=8080
HEADER = 1024
FILE = sys.argv[1].encode(FORMAT)


syn, ack = "SYN".encode(FORMAT), "ACK".encode(FORMAT)

ADDR   = (SERVER, PORT)

def extract_port(s):
    return int(s.split()[-1])


def disconnect(c,addr):
    while True:
        c.sendto(DISCONNECT_MESSAGE,addr)
        disc=c.recvfrom(HEADER)[0].decode(FORMAT)
        print(disc)
        if disc=="ACK_DISC":
            c.close()
            client.close()
            break
            sys.exit()

def create_socket(port):
    print(port)
    addr=(SERVER, port)
    c=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    c.settimeout(3)
    c.sendto(FILE,addr)
    resp=c.recvfrom(HEADER)[0].decode(FORMAT)
    print(resp)
    if resp=="DOES NOT EXIST":
        print("File doesn't exist... Exiting client!")
        disconnect(c,addr)
    elif resp=="ACK_FILENAME":
        print("horaay")
        disconnect(c,addr)


    # filename=input("Enter the filename you are looking for").encode(FORMAT)
    # files=c.recvfrom(HEADER)
    # files=pickle.loads(files)
    # print("\3"*3)
    # for file in files


    
 

# Create a UDP socket at client side
client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
client.settimeout(5)

 
# Send to server using created UDP socket
client.sendto(syn,ADDR)
servermsg = client.recvfrom(HEADER)
message=servermsg[0].decode("utf_8")
port=extract_port(message)
if message.split()[0][:7]=="ACK_SYN":
    create_socket(port)
 

# msg = f"Message from Server: {message}"

# print(msg)
