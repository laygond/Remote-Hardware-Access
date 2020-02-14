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
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect


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

def create_text(text, font_size, bold, text_color, bg_color):
    """ Returns surface with text written on """
    myfont = pygame.font.SysFont("Courier", font_size, bold)
    surface = myfont.render(text,True,text_color)#, fgcolor=text_color, bgcolor=bg_color)
    return surface#.convert_alpha()


# Create Window Display 
pygame.init()  
WINDOW_SIZE= 400                      
win = pygame.display.set_mode((WINDOW_SIZE,WINDOW_SIZE))  
pygame.display.set_caption("Remote Hardware Access")


#----------------START MENU WINDOW SETUP---------------
start_menu_bg = pygame.image.load(os.path.join("images","rha_intro2.PNG"))
start_menu_bg = pygame.transform.scale(start_menu_bg,(WINDOW_SIZE,WINDOW_SIZE))

text = ["Welcome","Click Anywhere to Start", "Remote Access", "by", "Laygond"]

font_size, bold, text_color, bg_color = 20, True, (0,0,255), (255,255,255)
txt_0 = create_text(text[0], font_size, bold, text_color, bg_color)
x_txt_0, y_txt_0 = 0.4*WINDOW_SIZE, 0.35*WINDOW_SIZE

font_size, bold, text_color, bg_color = 12, False, (0,0,0), (255,255,255)
txt_1 = create_text(text[1], font_size, bold, text_color, bg_color)
x_txt_1, y_txt_1 = 0.3*WINDOW_SIZE, 0.43*WINDOW_SIZE

font_size, bold, text_color, bg_color = 20, True, (0,0,255), (255,255,255)
txt_2 = create_text(text[2], font_size, bold, text_color, bg_color)
x_txt_2, y_txt_2 = 0.3*WINDOW_SIZE, 0.54*WINDOW_SIZE

font_size, bold, text_color, bg_color = 11, False, (0,0,255), (255,255,255)
txt_3 = create_text(text[3], font_size, bold, text_color, bg_color)
x_txt_3, y_txt_3 = 0.59*WINDOW_SIZE, 0.6*WINDOW_SIZE

font_size, bold, text_color, bg_color = 11,True,  (0,0,255), (255,255,255)
txt_4 = create_text(text[4], font_size, bold, text_color, bg_color)
x_txt_4, y_txt_4 = 0.59*WINDOW_SIZE, 0.625*WINDOW_SIZE

def redraw_start_menu():  
    win.blit(start_menu_bg, (0,0))  # This will draw our background image at (0,0)
    win.blit(txt_0, (x_txt_0, y_txt_0))
    win.blit(txt_1, (x_txt_1, y_txt_1))
    win.blit(txt_2, (x_txt_2, y_txt_2))
    win.blit(txt_3, (x_txt_3, y_txt_3))
    win.blit(txt_4, (x_txt_4, y_txt_4))
    pygame.display.update() 


#----------------MAIN MENU WINDOW SETUP---------------
main_menu_bg = pygame.image.load(os.path.join("images","rha_intro.JPG"))
main_menu_bg = pygame.transform.scale(main_menu_bg,(WINDOW_SIZE,WINDOW_SIZE))

def redraw_main_menu():  
    win.blit(main_menu_bg, (0,0))  # This will draw our background image at (0,0)
    pygame.display.update() 


run = True
start_menu = True 
while run:
    pygame.time.delay(100)

    #----------------START MENU---------------
    while start_menu:
        events = pygame.event.get()
        for event in events:
            #If red X from window is clicked
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #If mouse is clicked anywhere proceed to MAIN MENU
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    start_menu = False

        redraw_start_menu()


    #------------------MAIN MENU--------------
    events = pygame.event.get()
    for event in events:
        #If red X from window is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    redraw_main_menu()
        
        
    #     if event.type == pygame.KEYDOWN: 
    #         keys = pygame.key.get_pressed()
    #         print(keys)


    
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
