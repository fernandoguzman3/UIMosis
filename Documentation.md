# OCUSISTCP
OCUSIS Communication Protocol
Author: Eduardo F. Santiago Vargas
Reference Code: Alexander Baran-Harper 

SERVER:

    Contains the information that is going to be served. This script simulates the code that will be running in the TI TIVA sensory unit. 

    Variables:

        str host - Binds with the client's address.
        str port - Port used to communicate. Same as client.
        str status - Unknown if no succesful connection, OK if succesful connection.
        int temp - Variable used to store the temperature
        int pH - Variable used to store the pH level
        int lumin - Variable used to store the luminosity
        int press - Variable used to store the pressure

    Methods:

        Socket setupServer() - Creates a socket binding used to communicate with the client
        Socket setupConnection() - Establishes a connection with the client
        str STATUS() - Function that returns if a the connection is valid
        str GET(String dataMessage) - Function used to get a specific parameter. i.e: GET TEMPERATURE
        void dataTransfer(String conn) - Function that decides action that needs to be taken depending on the instruction.

CLIENT:

    Code that will run on the Raspberry PI 4 that will communicate and get data from the server.

    Variables:

        String host - server's Ethernet port address.
        String port - Port used to communicate. Same as server.