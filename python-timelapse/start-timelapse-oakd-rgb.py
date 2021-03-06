#!/usr/bin/env python3

import cv2
import depthai as dai
import time

nframes = 100
interval = 1

# Create pipeline
pipeline = dai.Pipeline()

# Define source and output
camRgb = pipeline.createColorCamera()
xoutRgb = pipeline.createXLinkOut()

xoutRgb.setStreamName("rgb")

# Properties
camRgb.setPreviewSize(300, 300)
camRgb.setInterleaved(False)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)

# Linking
camRgb.preview.link(xoutRgb.input)

# Connect to device and start pipeline
with dai.Device(pipeline) as device:

    print('Connected cameras: ', device.getConnectedCameras())
    # Print out usb speed
    print('Usb speed: ', device.getUsbSpeed().name)

    # Output queue will be used to get the rgb frames from the output defined above
    qRgb = device.getOutputQueue(name="rgb", maxSize=4, blocking=False)

    while True:
        inRgb = qRgb.get()  # blocking call, will wait until a new data has arrived

        for i in range(nframes):
            frame = qRgb.get()
            img = frame.getCvFrame()
            cv2.imwrite('./img_'+str(i).zfill(4)+'.png', img)
            time.sleep(interval)
        ## Retrieve 'bgr' (opencv format) frame
        #cv2.imshow("rgb", inRgb.getCvFrame())

        #if cv2.waitKey(1) == ord('q'):
        #    break
