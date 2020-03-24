import socket
import pickle

# ------------- CONSTANTS -------------------
HEADERSIZE = 10        # pre-allocates in header the length of msg: max (10 digit number)
SERVER_IP  = socket.gethostname()
PORT       = 2383      # (+1000 Recommended) Must match with client port

# ---------------- INITIAL SETUP -----------------
# Create Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
server_socket.bind((SERVER_IP, PORT))  # notifies os that it's going to use given IP and port.For a server using IP 0.0.0.0 means to listen on all available interfaces, useful to connect locally to 127.0.0.1 and remotely to LAN interface IP
server_socket.listen(5)                # Can queue up to 5 clients, in general leave blank for more than 1
print(f'Listening for connections on Server {SERVER_IP}:{PORT}...')


# ------------- RUN LOOP STARTS HERE -------------
while True:
    try:
        # now our endpoint knows about the OTHER endpoint.
        client_socket, address = server_socket.accept()      #freezes here until connection 
        print(f"Connection from Client: {address} has been established.")

        full_msg = b''
        new_msg = True
        while True:
            msg = client_socket.recv(512)   #freezes here until it receives from client, When a recv returns 0 bytes, it means the other side has closed
            if new_msg:
                print("new msg len:",msg[:HEADERSIZE])
                msglen = int(msg[:HEADERSIZE])
                new_msg = False

            full_msg += msg
            #print(len(full_msg)-HEADERSIZE)

            if len(full_msg)-HEADERSIZE == msglen:
                print("full msg recvd")
                print(full_msg[HEADERSIZE:])
                print(pickle.loads(full_msg[HEADERSIZE:]))
                new_msg = True
                full_msg = b""

    except:
        pass
