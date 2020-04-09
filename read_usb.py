import usb.core

ID_VENDOR  = 0x1a2c
ID_PRODUCT = 0x2124

dev = usb.core.find(idVendor=ID_VENDOR ,idProduct=ID_PRODUCT)

# first interface, first endpoint
i0_ep0  = dev[0].interfaces()[1].endpoints()[0]
i   = dev[0].interfaces()[1].bInterfaceNumber
dev.reset()

print(dev)
print("DONE 1")
print(i0_ep0)

print("DONE 2")
print(i)

print("DONE 3")
if dev.is_kernel_driver_active (i):
    dev.detach_kernel_driver(i)
if dev.is_kernel_driver_active (1):
    dev.detach_kernel_driver(1)

dev.set_configuration()
eaddr = i0_ep0.bEndpointAddress
print(eaddr)
print("DONE4")

r = dev.read(eaddr,16,timeout=5000)
print(len(r))
