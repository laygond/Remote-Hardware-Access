# Remote-Hardware-Access
Manage remotely through Python the hardware inputs of a computer: power button &amp; keyboard to turn on your computer, log into your computer, and even access your BIOS.

# How it works?
The two network communication (say A and B) is done through 3 computers. 
- <b>The target computer</b>, which you would like to control remotely (In Network B)
- <b>The server computer</b>, which is attached to the target computer for hardware control (In Network B)
- <b>The client computer</b>, which is the one you will be sending information from (In Network A)

My target computer is the super powerful computer I would like to control from anywhere around the world. However, in order to use amazing services like TeamViewer you must have your computer on and you should already be logged into your OS user account. This two crucial initial steps requires hardware control of the power switch and keyboard to type your password. My solution consists in attaching a low powered cheap computer like a raspberry pi to control the hardware inputs of my target computer. The raspberry pi will act as a server to accomplish the tasks requested from a client computer located miles away. 

The whole communication is done thanks to python libraries: pyserial & socket

I have added an independent IPcam in network B to see whats going (those cheap WyzeCam). You can also just attach a webcam to your raspberry pi and set up the proper ip configuration if you wish. 

# Setup and Installation
### Server Computer (Raspberry Pi)
Install ...

### Client Computer 
Install ...



