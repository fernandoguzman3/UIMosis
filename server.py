import socket

host = ''
port = 2304

status = "UNKNOWN"
temp = 30 # Unit: Celsius
pH = 7.6  
lumin = 0.1 # Unit: Lux
press =  4  # Unit: atm

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created")
    
    try:
        s.bind((host,port))
    except socket.error as msg:
        print(msg)

    print("Socket bind complete.")

    return s

def setupConnection():
    global status
    s.listen(1) # Only one connection at a time
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    status = "OK"
    return conn

def STATUS():
    reply = status
    return reply

def GET(dataMessage):
    request = dataMessage[1]
    global temp
    global pH
    global lumin
    global press

    if request == 'TEMPERATURE':
        reply = temp
    elif request == 'PH':
        reply = pH
    elif request == 'LUMINOSITY':
        reply = lumin
    elif request == 'PRESSURE':
        reply = press
    else:
        reply = "Unknown parameter"

    return str(reply)

def dataTransfer(conn):
    # Send/Recieve
    while True:
        # Recieve data
        data = conn.recv(1024) 
        data = data.decode('utf-8') # Python 3 needs to decode the data
        # Split data to separate the command 
        dataMessage = data.split(' ', 1)
        command = dataMessage[0] # command is the first segment
        if command == 'STATUS':
            reply = STATUS()
        elif command == 'GET':
            reply = GET(dataMessage)
        elif command == 'EXIT':
            print("Client Exit")
            break
        elif command == 'KILL':
            print("Server shutdown")
            s.close()
            break
        else:
            reply = 'Unknown Command'

        # Send Reply to Client
        conn.sendall(str.encode(reply))
        print("Data has been sent")

    conn.close()

s = setupServer()

while True:
    try:
        conn = setupConnection()
        dataTransfer(conn)
    except:
        break