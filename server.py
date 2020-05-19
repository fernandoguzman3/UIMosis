import socket

host = ''
port = 2304

status = "UNKNOWN"
temp = 30 # Unit: Celsius
pH = 7.6  
lumin = 0.1 # Unit: Lux
press =  4  # Unit: atm
leak = False

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

def UPDATE():
    global temp
    global pH
    global lumin
    global press
    global leak

    reply = str(temp) + ", "
    reply = reply + str(pH) + ", "
    reply = reply + str(lumin) + ", "
    reply = reply + str(press) + ", "
    reply = reply + str(leak)
    return reply

def GET(dataMessage):
    request = dataMessage[1]
    global temp
    global pH
    global lumin
    global press
    global leak

    if request == 'TEMPERATURE':
        reply = str(temp)
    elif request == 'PH':
        reply = "," + str(pH)
    elif request == 'LUMINOSITY':
        reply = ",," + str(lumin)
    elif request == 'PRESSURE':
        reply = ",,," + str(press)
    elif request == 'LEAK':
        reply = ",,,," + str(leak)
    else:
        reply = "Unknown parameter"

    return reply

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
        elif command == 'UPDATE':
            reply = UPDATE()
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