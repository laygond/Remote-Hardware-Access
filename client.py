import pickle

import socket, traceback
import csv

import wave
import struct
import math
import os
import numpy as np

import pygame
from pygame.locals import *             #This enhances all keybord inputs

import threading

# HEADERSIZE  = 10
# SERVER_IP   = socket.gethostname()
# SERVER_port = 1243

# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# client_socket.connect((SERVER_IP, SERVER_port))

# while True:
#     full_msg = b''
#     new_msg = True
#     while True:
#         msg = s.recv(16)
#         if new_msg:
#             print("new msg len:",msg[:HEADERSIZE])
#             msglen = int(msg[:HEADERSIZE])
#             new_msg = False

#         print(f"full message length: {msglen}")

#         full_msg += msg

#         print(len(full_msg))

#         if len(full_msg)-HEADERSIZE == msglen:
#             print("full msg recvd")
#             print(full_msg[HEADERSIZE:])
#             print(pickle.loads(full_msg[HEADERSIZE:]))
#             new_msg = True
#             full_msg = b""




#Keyboard setup through Pygame
pygame.init()                        
win = pygame.display.set_mode((300,300))  #A window must be created in order for pygame to work
pygame.display.set_caption("Remote Hardware Access")

run = True
while run:
    pygame.time.delay(100)

    events = pygame.event.get()
    for event in events:

        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN: 
            keys = pygame.key.get_pressed()
            print(keys)


    
    # if keys[pygame.K_LEFT]:
    #     x -= vel
    # win.fill((0,0,0))  # Fills the screen with black
    #pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    #pygame.display.update() 
    
pygame.quit()

# while True:
#     #************************** READ KEYBOARD DATA ****************************
#     events = pygame.event.get()
#     for event in events:
#         if event.type == pygame.KEYDOWN:
#             print(event.key) 
