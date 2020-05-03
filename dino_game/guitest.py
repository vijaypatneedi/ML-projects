import pyautogui
from PIL import Image, ImageGrab
#from numpy import asarray
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    for i in range(270,335):
         for j in range(543,650):
            if data[i,j]<100:
                hit("up")
                return 

    for i in range(250,300):
         for j in range(410,543):              
            if data[i,j]<171:
                hit("down")
                return 
    return 

    

if __name__=="__main__":
    print("Game starts in 3sec")
    time.sleep(3)
    hit("up")
    while True:
        image=ImageGrab.grab().convert("L")
        data= image.load()
        isCollide(data)
        
        ###print (asarray(image))
        # for i in range(270,315):
        #     for j in range(543,650):
        #         data[i,j]=0

        # for i in range(250,300):
        #     for j in range(410,543):
        #         data[i,j]=171

        # image.show()
        # break