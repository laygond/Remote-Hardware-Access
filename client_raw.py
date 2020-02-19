import pickle

import socket, traceback
import csv

import pyaudio
import wave
import struct
import math
import os
import numpy as np

import pygame
from pygame.locals import *             #This enhances all keybord inputs

import threading

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1243))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print("new msg len:",msg[:HEADERSIZE])
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        print(f"full message length: {msglen}")

        full_msg += msg

        print(len(full_msg))

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])
            print(pickle.loads(full_msg[HEADERSIZE:]))
            new_msg = True
            full_msg = b""


# import socket

# HEADERSIZE = 10

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(), 1241))

# while True:
#     full_msg = ''
#     new_msg = True
#     while True:
#         msg = s.recv(16)
#         if new_msg:
#             print("new msg len:",msg[:HEADERSIZE])
#             msglen = int(msg[:HEADERSIZE])
#             new_msg = False

#         print(f"full message length: {msglen}")

#         full_msg += msg.decode("utf-8")

#         print(len(full_msg))


#         if len(full_msg)-HEADERSIZE == msglen:
#             print("full msg recvd")
#             print(full_msg[HEADERSIZE:])
#             new_msg = True

                
                
# # Streaming Data via UDP setup
# host = ''
# port = 5555

# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# s.bind((host, port))



#Keyboard setup through Pygame
pygame.init()                        #Initializes queue of keyboard inputs
pygame.display.set_mode((400,400))   #A window must be created in order for pygame to work
condition1True = 0                   #List of Bool variables based on keyboard inputs
condition2True = 0
condition3True = 0
condition4True = 0
condition5True = 0
    


# Go through wave file 
print ('* Playing...')
for i in range(0, num_blocks): # Until end of Song 

    # Get block of samples from wave file
    input_string = wf.readframes(BLOCKSIZE)     # BLOCKSIZE = number of frames read

    # Convert binary string to tuple of numbers    
    input_tuple = struct.unpack('h' * BLOCKSIZE, input_string)
            # (h: two bytes per sample (WIDTH = 2))
    
    #************************ READ DATA FROM SENSORS ****************************
    try:
        message, address = s.recvfrom(8192)
        message = message[:-1] # -1 index gives the last element which is a # based on the app we are using
        
        #Read data element-wise from sensors
        reader = csv.reader(message.split('\n'), delimiter=',')
        for lineData in reader:
            xGyro = float(lineData[0])
            yGyro = float(lineData[1])
            zGyro = float(lineData[2])
            xG = float(lineData[3])
            yG = float(lineData[4])
            zG = float(lineData[5])
            xLinAcc = float(lineData[6])
            yLinAcc = float(lineData[7])
            zLinAcc = float(lineData[8])
            xRot = float(lineData[9])
            yRot = float(lineData[10])
            zRot = float(lineData[11])
                        
    except (KeyboardInterrupt, SystemExit):# set KeyboardInterrupt, SystemExit in "try clause" if needed
        raise
    except:
        traceback.print_exc()
    
    #print zGyro, zG
    
    #************************** END OF SENSOR DATA ****************************
    #************************** READ KEYBOARD DATA ****************************
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a: condition1True = 1
            if event.key == pygame.K_v: condition2True = 1
            if event.key == pygame.K_e: condition3True = 1
            if event.key == pygame.K_f: condition4True = 1
            if event.key == pygame.K_r: condition5True = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a: condition1True = 0
            if event.key == pygame.K_v: condition2True = 0
            if event.key == pygame.K_e: condition3True = 0
            if event.key == pygame.K_f: condition4True = 0
            if event.key == pygame.K_r: condition5True = 0
            
    
    
    #************************** END OF KEYBOARD DATA ****************************
    #************************ APPLY EFFECTS & CONDITIONS ************************
    
    #Initialize output block to ADD effects
    output_block1 = [0.0 for i in range(BLOCKSIZE)]   # Initialize to zero
    output_block2 = [0.0 for i in range(BLOCKSIZE)]   # Initialize to zero
    output_block3 = [0.0 for i in range(BLOCKSIZE)]   # Initialize to zero
    output_block4 = [0.0 for i in range(BLOCKSIZE)]   # Initialize to zero
    output_block5 = [0.0 for i in range(BLOCKSIZE)]   # Initialize to zero
    
    
    noCondition = 1             #Since Multiples conditions might happen keep track if no condition occurs
    countConditions = 0    
    
    #Condition 1    --for-->  AMPLITUDE MODULATION
    if (zG > 7 or condition1True):
        duckFreq = 400          # AM frequency
        output_block1 = func_duck(input_tuple, RATE, duckFreq)
        noCondition = 0
        countConditions += 1
    
    #Condition 2    --for-->        VIBRATO
    if (zGyro > 0.5 or condition2True):
        vibratoFreq = 10            
        vibratoAmplitude = 0.6      # Keep < 1
        output_block2 = func_vibrato(input_tuple, RATE, vibratoFreq, vibratoAmplitude)
        noCondition = 0
        countConditions += 1
    
    #Condition 3    --for-->        ECHO
    if ((abs(xRot)+abs(zRot)) > 2 or condition3True):
        Gdp = 1            
        Gff = 2      
        echo = int(buffer_MAX/2)  #1/2 of the distance of its buffer
        output_block3 = func_echo(input_tuple, Gdp, Gff, echo)
        noCondition = 0
        countConditions += 1
    
    #Condition 4    --for-->        FEEDBACK
    if (math.sqrt(xLinAcc**2 + zLinAcc**2) > 3 or condition4True):
        Gdp = 1            
        Gff = 2      
        Gfb = 0.4
        output_block4 = func_feedback(input_tuple, Gdp, Gff, Gfb)
        noCondition = 0
        countConditions += 1

    #Conditon 5 --for-->        ROBOTIZATION
    if(yG > 7 or condition5True):
        output_block5 = robotization(input_tuple)
        noCondition = 0
        countConditions += 1
        
    
    #NO Condition
    if noCondition:
        output_block = input_tuple
    else:
        output_block = [output_block1, output_block2, output_block3, output_block4, output_block5]
        output_block = [sum(x) for x in zip(*output_block)]
        output_block = [clip16(x) for x in output_block]
        
    #*********************** END OF EFFECTS & CONDITIONS **********************
    
    # Convert values to binary string
    output_string = struct.pack('h' * BLOCKSIZE, *output_block)

    # Write binary string to audio output stream
    stream.write(output_string)
    


print('* Done *')
stream.stop_stream()
stream.close()
p.terminate()
wf.close()


    
# if keys[pygame.K_LEFT]:
#     x -= vel
# win.fill((0,0,0))  # Fills the screen with black
#pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
#pygame.display.update() 
