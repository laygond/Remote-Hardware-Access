# USAGE
#python3 simple_client.py -s 10.0.0.7 -p 9000 

import pickle
import socket
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-s","--server", required=True,
    help="server ip address or hostname" )
ap.add_argument("-p","--port", required=True,
	help="port number, it must mtch with server port" )
args = vars(ap.parse_args())

# ------------- CONSTANTS -------------------
HEADERSIZE = 10        		   # pre-allocates in header the length of msg: max (10 digit number)
SERVER_IP  = args["server"]    # socket.gethostname() assigns a 127.0.0. address equivalent in the background
PORT       = int(args["port"]) # (+1024 Recommended) Must match with server port

# ---------------- INITIAL SETUP -----------------
# Create Client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, PORT))
#client_socket.setblocking(False)       # so .recv() call is not blocked

# ------------- RUN LOOP STARTS HERE -------------
run = True
while run:
	msg = input("Enter message: ")
	msg = pickle.dumps(msg)
	msg = bytes(f"{len(msg):<{HEADERSIZE}}", 'utf-8')+msg
	print(msg)
	client_socket.send(msg)
