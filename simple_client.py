import pickle
import socket

# ------------- CONSTANTS -------------------
HEADERSIZE = 10        # pre-allocates in header the length of msg: max (10 digit number)
SERVER_IP  = socket.gethostname()
PORT       = 2383      # (+1000 Recommended) Must match with server port

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
