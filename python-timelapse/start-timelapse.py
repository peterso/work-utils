import cv2
import numpy as np
import time

def main():
    """ Main entry point of the app """
    nframes = 100
    interval = 1

    #cap = cv2.VideoCapture(2) #logitech
    cap = cv2.VideoCapture(1) #built-in cam
    for i in range(nframes):
        # cpature
        ret, img = cap.read()
        # save file
        cv2.imwrite('./img_'+str(i).zfill(4)+'.png', img)
        # wait interval
        time.sleep(interval)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
