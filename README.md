# WebCamFS
Linux FUSE Filesystem for live webcam image

Frustrated that I could not find a quick way to upload webcam images to the web, I made this FUSE file system. If you are using a smartphone to deposit a check for example, you can use the camera natively to upload the image. Why can't this functionality be added to GNOME? This is my first attempt, all it does is:

- It only has one readonly file
- When the file is opened a new image is taken
- If you run the script when you log into gnome it will show up in the file chooser


Notes:
- Currently saves image as a .bmp because it is a constant size given a constant resolution, whereas jpg for example will change. This causes an issue when opening the file, because it takes the image when you open, so the size changes from underneath it and it will either not read the whole file, or past the end.
- Uses a fixed resolution of 1280x720 currently, will add a config option to the script
- Not sure if colors will be right for all webcams, I had to convert mine with cv2.COLOR_BGR2RGB
- Python3 tested only so far
- Have not implemented mount.webcamfs yet, so no fastab support, instead I launch command when I log into GNOME
- GNOME/Gtk File Chooser only seems to show mounts that are in your home directory, so choose somethings in there if you want to see it in the shortcut list.

INSTALL:

`sudo pip3 install git+https://github.com/seiferteric/WebCamFS.git`

USAGE:
Start:
`webcamfs ~/WebCam`
Stop:
`sudo umount ~/WebCam`
Add To GNOME startup with GUI:
`gnome-session-properties`
Make sure to put the full path to the mount root here, I had issues with `~/WebCam`, so put `/home/<username>/WebCam`

Demo:
![Demo](https://seiferteric.com/wp-content/uploads/2018/03/gtkfilechooser.png)
