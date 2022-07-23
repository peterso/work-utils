import cv2
import numpy as np
import pyrealsense2 as rs
import time

nframes = 20
interval = 1

pipe = rs.pipeline()
profile = pipe.start()

try:
  for i in range(0, nframes):
    frames = pipe.wait_for_frames()
    color_frame = frames.get_color_frame()
    for f in frames:
        color_image = np.asanyarray(color_frame.get_data())
        cv2.imwrite('img_'+str(i).zfill(4)+'.png', cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB))
        print(f.profile)
        time.sleep(interval)
finally:
    pipe.stop()

