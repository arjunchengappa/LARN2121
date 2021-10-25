import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 1024 * 4 #4KB
CLIENT_ADDR = socket.gethostbyname(socket.gethostname())

def send_file(filename, host, port):
    # get the file size
    filesize = os.path.getsize(filename)
    # create the client socket
    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{CLIENT_ADDR}{SEPARATOR}{filename}{SEPARATOR}{filesize}".encode())
    # start sending the file
    progress = tqdm.tqdm(range(filesize), f"Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024, leave=False)
    with open(filename, "rb") as f:
        while True:
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                # file transmitting is done
                break
            # we use sendall to assure transimission in 
            # busy networks
            s.sendall(bytes_read)
            # update the progress bar
            progress.update(len(bytes_read))
    # close the sockets
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((CLIENT_ADDR, 8040))
    data, addr = s.recvfrom(1024)
    print(data.decode())

if __name__ == "__main__":
    send_file("D002.mp4", "127.0.0.1", 8080)