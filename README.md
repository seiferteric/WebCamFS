# WebCamFS
Linux FUSE Filesystem for live webcam image

Frustrated that I could not find a quick way to upload webcam images to the web, I made this FUSE file system. If you are using a smartphone to deposit a check for example, you can use the camera natively to upload the image. Why can't this functionality be added to GNOME? This is my first attempt, all it does is:

- It only has one readonly file
- When the file is read a new image is taken
- If you run the script when you log into gnome it will show up in the file chooser


Notes:
- Currently saves image as a .bmp because it is a constant size given a constant resolution, whereas jpg for example will change. This causes an issue when opening the file, because it takes the image when you open, so the size changes from underneath it and it will either not read the whole file, or past the end.
- Uses a fixed resolution of 1280x720 currently, will add a config option to the script
- Not sure if colors will be right for all webcams, I had to convert mine with cv2.COLOR_BGR2RGB