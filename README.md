[//]: # (----Image References List ---)
[image1]: ./README_images/demo.gif
[image2]: ./README_images/general_diagram.PNG
[image3]: ./README_images/hardware_diagram.PNG
[image4]: ./README_images/hardware_pic.PNG

# Remote-Hardware-Access
![alt text][image1]

Manage remotely through Python the hardware inputs of a computer: power button &amp; keyboard to turn on your computer, log into your computer, and even access your BIOS.

This solution is OS independent as long as you have Python. The Python libraries take care of the OS specifics. This solution also allows you to toggle your keyboard between the local and remote computer. 

# How it works?
![alt text][image2]

The two network communication (say A and B) is done through 3 computers. 
- <b>The target computer</b>, which you would like to control remotely (In Network B)
- <b>The server computer</b>, which is attached to the target computer for hardware control (In Network B)
- <b>The client computer</b>, which is the one you will be sending information from (In Network A)

My target computer is the super powerful computer I would like to control from anywhere around the world. However, in order to use amazing services like TeamViewer, etc you must have your computer on and you should already be logged into your OS user account. This two crucial initial steps requires hardware control of the power switch and keyboard to type your password. My solution consists in attaching a low powered cheap computer like a raspberry pi to control the hardware inputs of my target computer. The raspberry pi will act as a server to accomplish the tasks requested from a client computer located miles away. 

The whole communication is done thanks to a python library: socket. The keyboard input and GUI is done in pygame.

I have added an independent IPcam in network B to see whats going (those cheap WyzeCam). You can also just attach a webcam to your raspberry pi and set up the proper ip configuration if you wish. You can also buy a video card and create a complete KVM over IP system but this repo is a variation that only deals with Keyboard and Power over IP + Video in an independent way.

# Hardware Requirements
For this project you will need:
* Raspberry Pi 4 Model B (Pi4 has OTG USB)
* Servo Motor or Relay board

![alt text][image3]

This repo uses a servo motor approach to turn ON/OFF the target computer for a complete isolated system. However, a relay can also be used instead. Connect the relay with the power signal cable that is attached to the target's motherboard. This is the final setup:

![alt text][image4]

# Directory Structure
```
.Turn-OFF-The-Lights
├── demo.ipynb                   # Main file
├── .gitignore                   # git file to prevent unnecessary files from being uploaded
├── README_images                # Images used by README.md
│   └── ...
├── README.md
├── hed_model                    # HED Neural Network information
│   ├── deploy.prototxt                   # Model (architecture)
│   └── hed_pretrained_bsds.caffemodel    # Weights of Model
├── Input_Videos                 # Input Video directory
│   └── sample.mp4
├── Output_Videos                # output directory generated automatically once you run demo.ipynb
    └── ...
```

# Setup and Installation
### Before Assembly
On the Pi4, flash the latest image of Raspbian. As of this writing I used Raspbian Buster version 2020-02-13 which is the version that works successfully. Make sure you can SSH to your Pi and that your Pi is connected to the internet either wired or wirelessly. There are plenty of tutorials on how to do this in youtube.

### Network B Router
* Set the IP address of your Pi as a DHCP reservation or a static IP
* Port forward a port number of your choice and link it to your Pi's IP 
NOTE: I have included under tools `simple_client.py` and `simple_server.py` to test your port configuration is working correctly. Try it locally with your Pi's IP address and externally with your public IP address.

### Server Computer (Raspberry Pi)
SSH to your Pi and run
```sh
$ git clone https://github.com/laygond/Remote-Hardware-Access.git
$ cd Remote-Hardware-Access
$ sudo chmod +x install_server.sh
$ source install_server.sh
```

### Client Computer 
Linux, Mac, or Windows
```sh
$ git clone https://github.com/laygond/Remote-Hardware-Access.git
$ cd Remote-Hardware-Access
$ pip3 install pygame
```

# Launch and Run
### Server Computer (Raspberry Pi in Network B)
The server side will be running all the time
```sh
$ python3 server.py -s <Pi_IP_address> -p <Server_Port>
```
### Client Computer (Network B: Local Connection)
```sh
$ python3 client.py -s <Pi_IP_address> -p <Server_Port>
```
### Client Computer (Network A: External Connection)
```sh
$ python3 client.py -s <NetworkB_Public_IP_address> -p <Server_Port>
```


# EXTRA
## How to set server to send its Network Public IP to your email weekly
Under `tools` there is `weekly_emails.py`. Open the file and set the proper changes whether you are using a Google or Microsoft email account. To run this file along with server.py the python scripts must run in parallel. To do this...


## Alternative Hardware Configurations
* Raspberry Pi 3 B+ and [FTDI Vinculum II](https://www.ftdichip.com/Support/Documents/AppNotes/AN_199_VNC2_SPI_SLAVE_to_HID_Class_Device_Bridge.pdf)
* Raspberry Pi 3 B+ and [MAX3421E](https://www.maximintegrated.com/en/products/interface/controllers-expanders/MAX3421E.html) inspired by this [video](https://www.youtube.com/watch?v=pwg39X9Imh0)
* [Raspberry Pi 3 B+ and Arduino (Idea video)](https://www.youtube.com/watch?v=wTbjmulNSlw&list=PL-l6K_RPZ_ebZydwerBPCYfzPzMOY6LcQ&index=5&t=0s)
* [Raspberry Pi 3 B+ and Raspberry Pi Zero](https://github.com/Fmstrat/diy-ipmi)
* Raspberry Pi Zero W

## Keywords and Reference
* Sending Data from Raspberri Pi to PC
* [Intro to USB Device](https://www.electronicdesign.com/technologies/boards/article/21801151/how-to-create-and-program-usb-devices)
* [Intro to Keyboard HID Class](https://www.youtube.com/watch?v=1unTKKGd8qs)
* [Read USB in Python with pyusb and libusb](https://www.youtube.com/watch?v=xfhzbw93rzw)
* [FTDA USB Bridge Solutions](https://www.ftdichip.com/USB.html)
* [Raspberry Pi I2C, SPI, and UART](https://www.mbtechworks.com/hardware/raspberry-pi-UART-SPI-I2C.html)
* HID 
* Remote Access
* IoT Keyboard
* KVM Over IP Variation
* Keyboard and Power over IP
* Menu option in Pygame
* [Socket Client & Sever](https://docs.python.org/3/howto/sockets.html)
* Device Tree Overlays
* [USB Vendor and Device ID List](http://www.linux-usb.org/usb.ids)
* USB Device [Setup](https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/) [Setup 2](https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition) [Setup 3](https://cdn-learn.adafruit.com/downloads/pdf/turning-your-raspberry-pi-zero-into-a-usb-gadget.pdf)
* [Correct Module Setup](https://wiki.archlinux.org/index.php/Kernel_module)
* [Connect to pi as a device](https://makezine.com/2014/02/28/talking-to-the-raspberry-pis-serial-console-with-an-ftdi-breakout-board/)
* WiFi Keyboard
* [USB HID Usage Table (page 53 for DEC codes)](https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf)

