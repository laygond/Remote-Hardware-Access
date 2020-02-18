import pickle

import socket, traceback
import csv
import time
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

def create_text(text, font_size, bold, text_color):
    """ Returns surface with text written on """
    myfont = pygame.font.SysFont("Courier", font_size, bold)
    surface =  myfont.render(text,True,text_color)
    return surface 

# --------- CONSTANTS --------
WINDOW_SIZE= 400  
BOX_THICKNESS = 3
BLUE = (0,0,255)  
BLACK = (0,0,0)
WHITE = (255,255,255)
BOLD = True

# Create Window Display 
pygame.init()                      
win = pygame.display.set_mode((WINDOW_SIZE,WINDOW_SIZE))  
pygame.display.set_caption("Remote Hardware Access")


#----------------START MENU WINDOW SETUP---------------
start_menu_bg = pygame.image.load(os.path.join("images","rha_intro2.PNG"))
start_menu_bg = pygame.transform.scale(start_menu_bg,(WINDOW_SIZE,WINDOW_SIZE))

text = ["Welcome","Click Anywhere to Start", "Remote Access", "by", "Laygond"]

txt_0 = create_text(text[0], 20, BOLD, BLUE)
x_txt_0, y_txt_0 = 0.4*WINDOW_SIZE, 0.35*WINDOW_SIZE

txt_1 = create_text(text[1], 12, not BOLD, BLACK)
x_txt_1, y_txt_1 = 0.3*WINDOW_SIZE, 0.43*WINDOW_SIZE

txt_2 = create_text(text[2], 20, BOLD, BLUE)
x_txt_2, y_txt_2 = 0.3*WINDOW_SIZE, 0.54*WINDOW_SIZE

txt_3 = create_text(text[3], 11, not BOLD, BLUE)
x_txt_3, y_txt_3 = 0.59*WINDOW_SIZE, 0.6*WINDOW_SIZE

txt_4 = create_text(text[4], 11, BOLD, BLUE)
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
main_menu_bg = pygame.image.load(os.path.join("images","rha_intro3.JPG"))
main_menu_bg = pygame.transform.scale(main_menu_bg,(WINDOW_SIZE,WINDOW_SIZE))

img_power_on = pygame.image.load(os.path.join("images","rha_power_on.PNG"))
w,h = img_power_on.get_size()
a = w/h      #aspect ratio
img_power_on = pygame.transform.scale(img_power_on,(int(1.5/12*a*WINDOW_SIZE), int(1.5/12*WINDOW_SIZE)))

img_power_off = pygame.image.load(os.path.join("images","rha_power_off2.PNG"))
w,h = img_power_off.get_size()
a = w/h      #aspect ratio
img_power_off = pygame.transform.scale(img_power_off,(int(1.5/12*a*WINDOW_SIZE), int(1.5/12*WINDOW_SIZE)))

img_keyboard_on = pygame.image.load(os.path.join("images","rha_keyboard_on2.PNG"))
w,h = img_keyboard_on.get_size()
a = w/h      #aspect ratio
img_keyboard_on = pygame.transform.scale(img_keyboard_on,(int(1.5/12*a*WINDOW_SIZE), int(1.5/12*WINDOW_SIZE)))

img_keyboard_off = pygame.image.load(os.path.join("images","rha_keyboard_off2.PNG"))
w,h = img_keyboard_off.get_size()
a = w/h      #aspect ratio
img_keyboard_off = pygame.transform.scale(img_keyboard_off,(int(1.5/12*a*WINDOW_SIZE), int(1.5/12*WINDOW_SIZE)))

img_cmd_on = pygame.image.load(os.path.join("images","rha_cmd_on.PNG"))
w,h = img_cmd_on.get_size()
a = w/h      #aspect ratio
img_cmd_on = pygame.transform.scale(img_cmd_on,(int(1.5/12*a*WINDOW_SIZE), int(1.5/12*WINDOW_SIZE)))

img_cmd_off = pygame.image.load(os.path.join("images","rha_cmd_off.PNG"))
w,h = img_cmd_off.get_size()
a = w/h      #aspect ratio
img_cmd_off = pygame.transform.scale(img_cmd_off,(int(1.5/12*a*WINDOW_SIZE), int(1.5/12*WINDOW_SIZE)))

# text2 = ["Real Time Power Switch","One Click equals 2 seconds", "Press & Hold for longer time"\
#         "Real Time Keyboard", "Click to Toggle"\
#         "Paste and Send","Click to Toggle","Send long strings (500 char)"\
#         "© 2020 Laygond Github, Remote Hardware Access"]

x,y,w,h = int(2.1/12*a*WINDOW_SIZE), int(2.6/12*WINDOW_SIZE), int(6.5/12*WINDOW_SIZE), int(2.5/12*WINDOW_SIZE)
rectPower = pygame.Rect(x,y,w,h)  
x,y,w,h = int(2.1/12*a*WINDOW_SIZE), int(5.1/12*WINDOW_SIZE), int(6.5/12*WINDOW_SIZE), int(2.5/12*WINDOW_SIZE)
rectKeyboard = pygame.Rect(x,y,w,h)  
x,y,w,h = int(2.1/12*a*WINDOW_SIZE), int(7.6/12*WINDOW_SIZE), int(6.5/12*WINDOW_SIZE), int(3/12*WINDOW_SIZE)
rectCmd = pygame.Rect(x,y,w,h) 

mouse_over_power = False
mouse_over_keyboard = False
mouse_over_cmd = False
mouse_click = False
click_power = False
click_keyboard = False
click_cmd = False
hold_power = False
timer_start = 0

def redraw_main_menu():  
    win.blit(main_menu_bg, (0,0))  # This will draw our background image at (0,0)
    
    #    elapse = time.time()-timer if time.time()-timer < 60 else 0 
    if click_power:
        win.blit(img_power_on, (3/12*WINDOW_SIZE,3/12*WINDOW_SIZE))
        txt_0 = create_text("Processing...", 18, BOLD, WHITE)
        x_txt_0, y_txt_0 = 0.4*WINDOW_SIZE, 0.35*WINDOW_SIZE
        win.blit(txt_0, (x_txt_0, y_txt_0)) 
    elif hold_power:
        win.blit(img_power_on, (3/12*WINDOW_SIZE,3/12*WINDOW_SIZE))
        timer_disp = int((time.time()- timer_start)*100)/100.0
        print(timer_disp)
        txt_0 = create_text(str(timer_disp)+" seconds", 20, BOLD, WHITE)
        x_txt_0, y_txt_0 = 0.4*WINDOW_SIZE, 0.35*WINDOW_SIZE
        win.blit(txt_0, (x_txt_0, y_txt_0))  
    else:
        win.blit(img_power_off, (3/12*WINDOW_SIZE,3/12*WINDOW_SIZE))

    if click_keyboard:
        win.blit(img_keyboard_on, (3/12*WINDOW_SIZE,5.5/12*WINDOW_SIZE)) 
    else: 
        win.blit(img_keyboard_off, (3/12*WINDOW_SIZE,5.5/12*WINDOW_SIZE))
    
    if click_cmd:
        win.blit(img_cmd_on, (3/12*WINDOW_SIZE,8/12*WINDOW_SIZE))
    else:
        win.blit(img_cmd_off, (3/12*WINDOW_SIZE,8/12*WINDOW_SIZE)) 

    if mouse_over_power: 
        pygame.draw.rect(win, BLUE, rectPower, BOX_THICKNESS)
    if mouse_over_keyboard: 
        pygame.draw.rect(win, BLUE, rectKeyboard, BOX_THICKNESS)
    if mouse_over_cmd: 
        pygame.draw.rect(win, BLUE, rectCmd, BOX_THICKNESS)

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
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                start_menu = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button ==1:
            #         start_menu = False

        redraw_start_menu()


    #------------------MAIN MENU--------------
    mouse_pos = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        #If red X from window is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        #If power option is pressed then start timer
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rectPower.collidepoint(mouse_pos):
                timer_start = time.time()
                hold_power = True  
                click_power = False
                click_keyboard = False
                click_cmd = False
        # if mouse is clicked over options
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            hold_power = False
            if rectPower.collidepoint(mouse_pos):
                timer_end = time.time() - timer_start
                if timer_end <0.7:      # click threshold in seconds 
                    click_power = True  # will be turned off after 2.5 seconds
                click_keyboard = False
                click_cmd = False
            if not click_power: # cannot change option while powering on
                if rectKeyboard.collidepoint(mouse_pos):
                    click_power = False
                    click_keyboard = False if click_keyboard else True
                    click_cmd = False
                elif rectCmd.collidepoint(mouse_pos):
                    click_power = False
                    click_keyboard = False
                    click_cmd = False if click_cmd else True

    #Turn off power click option after 2.5 seconds
    if click_power:
        if time.time()- timer_start > 2.5:
            click_power = False

    # If mouse over options then display box
    if rectPower.collidepoint(mouse_pos):
        mouse_over_power = True
    else: 
        mouse_over_power = False
    if rectKeyboard.collidepoint(mouse_pos):
        mouse_over_keyboard = True
    else: 
        mouse_over_keyboard = False
    if rectCmd.collidepoint(mouse_pos):
        mouse_over_cmd = True
    else: 
        mouse_over_cmd = False


    # if rectPower.collidepoint(pygame.mouse.get_pos()):
    #     mouse_over_power = True
    #     if mouse_click:
    #         click_power = True
    #         mouse_click = False
    # else: 
    #     mouse_over_power = False
    
    # if rectKeyboard.collidepoint(pygame.mouse.get_pos()):
    #     mouse_over_keyboard = True
    #     if mouse_click:
    #         click_keyboard = True
    #         mouse_click = False
    # else: 
    #     mouse_over_keyboard = False
    
    # if rectCmd.collidepoint(pygame.mouse.get_pos()):
    #     mouse_over_cmd = True
    #     if mouse_click:
    #         click_cmd = True
    #         mouse_click = False
    # else: 
    #     mouse_over_cmd = False

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
