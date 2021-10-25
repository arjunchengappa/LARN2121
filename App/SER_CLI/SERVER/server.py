import socket
import os

def ensemble(video):
    return True

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 8080

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

s = socket.socket()
s.bind((SERVER_HOST, SERVER_PORT))

#while True:
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
# accept connection if there is any
client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected.")

# receive the file infos
# receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)
# remove absolute path if there is
filename = os.path.basename(filename)
# convert to integer
filesize = int(filesize)
# start receiving the file from the socket
# and writing to the file stream
f = open(filename, "wb")

while True:
    # read 1024 bytes from the socket (receive)
    bytes_read = client_socket.recv(BUFFER_SIZE)
    if not bytes_read:    
        # nothing is received
        # file transmitting is done
        break
    # write to the file the bytes we just received
    f.write(bytes_read)
    # update the progress bar

print(f"[+] Recieved {filename} from {address}\n")
f.close()
client_socket.sendall(bytes("Hello", 'utf-8'))
# close the client socket
client_socket.close()