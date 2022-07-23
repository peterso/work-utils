This is a beginning of a python script to take timelapse images using opencv. Manually modify the python file to change the settings.

[TODO] make the file accept parameters for number of frames and interval

working:
    builtin
    logitech
    oakd with black and white and rbg
    intel realsense

## Quick Start

1. To start the camera captures use the following command `python3 python-timelapse.py`

2. To create the video timelapse from the series of generated images use the following command `ffmpeg -r 20 -i img_%04d.png -c:v libx264 -vf fps=24 -pix_fmt yuv420p out.mp4`. Change the `-r` to adjust the length (and speed) of the output video.
