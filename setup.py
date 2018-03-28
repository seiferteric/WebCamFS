from setuptools import setup, find_packages

ver = "0.0.1"

setup(
      name = "WebCamFS",
      version = ver,
      packages = find_packages(),
      author = "Eric Seifert",
      author_email = "seiferteric@gmail.com",
      description = "Linux FUSE Filesystem for live webcam image",
      keywords = "webcam FUSE",
      url = "https://github.com/seiferteric/WebCamFS",
      zip_safe = True,
      install_requires = ['opencv-python', 'scipy'],
      scripts=['webcamfs']
)

