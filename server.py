import socket

host = ''
port = 2304


temp = 30 # Unit: Celsius
pH = 7.6  
lumin = 0.1 # Unit: Lux
press =  4  # Unit: atm
leak = False

status = "UNKNOWN"
tempStatus = "temp OK"
phStatus = "ph OK"
luminStatus = "lumin OK"
pressStatus = "press OK"
leakStatus = "leak OK"


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

def STATUS(dataMessage):
    command = dataMessage[1]

    if command == "TEMPERATURE":
        reply = tempStatus
    elif command == "PH":
        reply = phStatus
    elif command == "LUMINOSITY":
        reply = luminStatus
    elif command == "PRESSURE":
        reply = pressStatus
    elif command == "LEAK":
        reply = leakStatus
    else:
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
    request = dataMessage[1].split(' ')
    global temp
    global pH
    global lumin
    global press
    global leak
    reply = ""

    if 'TEMPERATURE' in request:
        reply = reply + str(temp)
    else:
        reply = reply + " - "
    
    if 'PH' in request:
        reply = reply + "," + str(pH)
    else:
        reply = reply + ", - "
    
    if 'LUMINOSITY' in request:
        reply = reply + "," + str(lumin)
    else:
        reply = reply + ", - "
    
    if 'PRESSURE' in request:
        reply = reply + "," + str(press)
    else:
        reply = reply + ", - "
    
    if 'LEAK' in request:
        reply = reply + "," + str(leak)
    else:
        reply = reply + ", - "

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
            reply = STATUS(dataMessage)
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