from gpiozero import LED
import os
from picamera import PiCamera
cselect=LED(4)
cenable1=LED(17)
cenable2=LED(18)
i2c='i2cset -y 1 0x70 0x00 0x04'
os.system(i2c)
cselect.off()
cenable1.off()
cenable2.on()
camera=PiCamera()
camera.resolution=(640,480)
def camera1():
    cselect.off()
    cenable1.off()
    cenable2.on()
    i2c='i2cset -y 1 0x70 0x00 0x04'
    os.system(i2c)
    
def camera2():
    cselect.on()
    cenable1.off()
    cenable2.on()
    i2c='i2cset -y 1 0x70 0x00 0x05'
    os.system(i2c)
    
def camera3():
    cselect.off()
    cenable1.on()
    cenable2.off()
    i2c='i2cset -y 1 0x70 0x00 0x06'
    os.system(i2c)
    
def camera4():
    cselect.on()
    cenable1.on()
    cenable.off()
    i2c='i2cset -y 1 0x70 0x00 0x07'
    os.system(i2c)

def ccheck():
    camera._check_camera_open()
    
def cpreview():
    camera.start_preview(fullscreen=False,window=(0,0,640,480))
    print("camera active")
    
def cstop():
    camera.stop_preview()
    
def main():
    userin=""
    while userin != "end":
        userin=input("Command: ")
        if userin=='c1':
            camera1()
        if userin=='c2':
            camera2()
        if userin=='c3':
            camera3()
        if userin=='c4':
            camera4()
        if userin=='p':
            cpreview()
        if userin=='s':
            cstop()
        if userin=='cc':
            ccheck()
        if userin=='h':
            print ("c1 - select camera 1")
            print ("c2 - select camera 2")
            print ("c3 - select camera 3")
            print ("c4 - select camera 4")
            print ("cc - Camera check")
            print ("p - Preview")
            print ("s - Stop Preview")
    
    camera.close()

    
if __name__ == "__main__":
    main()