import socket            
 

s = socket.socket()
print ("Socket successfully created")

port = 5000
 

s.bind(('', port))
print ("socket binded to %s" %(port))

       

while True:
    s.listen(5)
    print ("socket is listening")
    while True:
        c, addr = s.accept()
        print ('Got connection from', addr )
        c.send('Thank you for connecting'.encode())
        c.close()
        print("Sent parameters to", addr)
        break