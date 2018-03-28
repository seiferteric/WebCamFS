from setuptools import setup, find_packages

ver = "0.0.3"

setup(
      name = "webcamfs",
      version = ver,
      packages = find_packages(),
      author = "Eric Seifert",
      author_email = "seiferteric@gmail.com",
      description = "Linux FUSE Filesystem for live webcam image",
      keywords = "webcam FUSE",
      url = "https://github.com/seiferteric/WebCamFS",
      install_requires = ['opencv-python', 'scipy', 'fusepy'],
      scripts=['webcamfs']
)

