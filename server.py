# USAGE
#python3 server.py -s 10.0.0.7 -p 9000 

import pickle
import socket
import argparse
import time
import RPi.GPIO as GPIO

ap=argparse.ArgumentParser()
ap.add_argument("-s","--server", required=True,
    help="server ip address or hostname" )
ap.add_argument("-p","--port", required=True,
	help="port number, it must mtch with client port" )
args = vars(ap.parse_args())

# ------------- CONSTANTS -------------------
HEADERSIZE = 10        		   # pre-allocates in header the length of msg: max (10 digit number)
BATCHSIZE  = 512               # read incoming data in chunks of this size
SERVER_IP  = args["server"]    # socket.gethostname() assigns a 127.0.0. address equivalent in the background
PORT       = int(args["port"]) # (+1024 Recommended) Must match with client port
KEYBOARD_Tx_PIN = 22           # GPIO 22 (physical pin 15) 

# ---------------- INITIAL SETUP -----------------
# Create Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((SERVER_IP, PORT))  # notifies os that it's going to use given IP and port.For a server using IP 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
server_socket.listen(5)                # Can queue up to 5 clients, in general leave blank for more than 1
print(f'Listening for connections on Server {SERVER_IP}:{PORT}...')

# Raspberry Pi GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(KEYBOARD_Tx_PIN, GPIO.OUT)

# ------------- RUN LOOP STARTS HERE -------------
while True:
    try:
        # Accept Client
        client_socket, address = server_socket.accept()      #freezes here until connection 
        print(f"Connection from Client: {address} has been established.")

        # Initialize msg variable
        full_msg = b''
        new_msg = True
        
        while True:
            msg = client_socket.recv(BATCHSIZE)   #freezes here until it receives from client, When a recv returns 0 bytes, it means the other side has closed
            # Read msg Header
            if new_msg:
                print("new msg len:",msg[:HEADERSIZE])
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            # Attach chunks of msg
            full_msg += msg
            #print(len(full_msg)-HEADERSIZE)

            # Complete msg received
            if len(full_msg)-HEADERSIZE == msglen:
                print("full msg recvd")
                print(full_msg[HEADERSIZE:])
                print(pickle.loads(full_msg[HEADERSIZE:]))
                
                # Reset msg variables
                new_msg = True
                full_msg = b""
                
                # Process info 
                GPIO.output(KEYBOARD_Tx_PIN, True)
                time.sleep(3)
                GPIO.output(KEYBOARD_Tx_PIN, False)
                
    except:
        #GPIO.output(KEYBOARD_Tx_PIN, False)
        #GPIO.cleanup()
        pass
