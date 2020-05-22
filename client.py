import socket
import csv
from datetime import datetime

host = '169.254.153.172'
port = 2304

temp = "" # Unit: Celsius
pH = ""  
lumin = "" # Unit: Lux
press = ""  # Unit: atm

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
    
    with open('output.csv', 'a', newline='') as csvfile:
        datawriter = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        datawriter.writerow([datetime.now(), reply.decode('utf-8')])

s.close()