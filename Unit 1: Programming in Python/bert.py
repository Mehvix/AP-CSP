import matplotlib.pyplot as plt  # This is the class that has the image stuff
# in it. I use this to work with pixels
# in an image
import os.path
import PIL
import io
from pylab import *
from PIL import ImageOps
from PIL import Image
import numpy as np

plt.ion()
image_dir = os.path.dirname(os.path.abspath(__file__)) + r'/images'


bertpic = os.path.join(image_dir, 'bert.png')
bertpic = PIL.Image.open(bertpic)  # I have to use this to manipulate the


tophat = os.path.join(image_dir, 'tophat.png')
tophat = PIL.Image.open(tophat)
resizedHat = tophat.resize((750, 750))
mirroredHat = PIL.ImageOps.mirror(resizedHat)
bertpic.paste(mirroredHat, (50, -300), mask=mirroredHat)

monacle = os.path.join(image_dir, 'monacle.png')
monacle = PIL.Image.open(monacle)
bertpic.paste(monacle, (50, 350), mask=monacle)

moustache = os.path.join(image_dir, 'moustache.png')
moustache = PIL.Image.open(moustache)
moustache = moustache.resize((350, 200))
bertpic.paste((35, 35, 35), (150, 525), mask=moustache)


fig, ax = plt.subplots(1, 1)
ax.set_title("Fancy Bert")
ax.imshow(bertpic)  # the original dog pic

fout = io.BytesIO()
# plt.imsave(fout, bertpic, format='png')
plt.show()
