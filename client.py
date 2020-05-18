import socket

host = '169.254.56.207'
port = 2304

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter command: ")
    if command == 'EXIT':
        # EXIT request
        s.send(str.encode(command)) 
        break
    elif command == 'KILL':
        # KILL command
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply.decode('utf-8'))

s.close()