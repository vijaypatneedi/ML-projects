import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

#def draw():
    

def takeScreenshot():
    image=ImageGrab.grab()
    image.show()
    return image

if __name__=="__main__":
    time.sleep(1)
    image= takeScreenshot()
    data= image.load()
    print(data)
    for i in range(34,45):
        for j in range(45,67):
            data