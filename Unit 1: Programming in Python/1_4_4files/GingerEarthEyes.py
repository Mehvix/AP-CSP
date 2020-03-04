import matplotlib.pyplot as plt  # This is the class that has the image stuff
# in it. I use this to work with pixels
# in an image
import os.path
import PIL
import numpy as np

plt.ion()

directory = os.path.dirname(os.path.abspath(__file__))
scarf = os.path.join(directory, 'doRag.jpg')
gingerpic = os.path.join(directory, 'gingersmall.jpg')
earth_file = os.path.join(directory, 'earth.jpg')
earth_img = PIL.Image.open(earth_file)
coolhat = plt.imread(scarf)
PILcoolhat = PIL.Image.open(scarf)
out = earth_img.resize((20, 20))  # I looked at the picture and got the size of the eye
# so I could resize the image
img = plt.imread(gingerpic)  # I have to use this to work with the pixels
# This is my picture of ginger note: I don't really
# use img for anything in this program
# to resize the hat (which is very big) I have to turn it into a PIL:
pilHat = PIL.Image.fromarray(coolhat)
smallHat = PILcoolhat.resize((250, 250))
# and now I want to look at each pixel in this pic
# so I am going to put it back in numpy form
pixelHat = np.array(smallHat)
justHat = smallHat.convert("RGBA")  # I need an alpha channel so I can do transparency
# and now I have to make justHat a 2d array:
justHat = np.array(justHat)
new_img = PIL.Image.open(gingerpic)  # I have to use this to manipulate the
# whole picture
new_img.paste(out, (105, 95), mask=out)  # this should paste the little earth at this spot on the gingerpic
# new_img.paste(smallHat, (50,170),mask = smallHat)
# get just the hat
hatWidth = len(coolhat)
hatLength = len(coolhat[0])
# Now I am looking for the pixels that make up the hat and copying
# them over, the rest of that picture I am making into a white full transparency
for r in range(len(pixelHat)):
    for c in range(len(pixelHat[0])):
        if pixelHat[r][c][0] < 130 and pixelHat[r][c][1] < 130 and pixelHat[r][c][2] < 130:
            justHat[r][c][0] = pixelHat[r][c][0]
            justHat[r][c][1] = pixelHat[r][c][1]
            justHat[r][c][2] = pixelHat[r][c][2]
            justHat[r][c][3] = 255
        else:
            justHat[r][c][0] = 0
            justHat[r][c][1] = 0
            justHat[r][c][2] = 0
            justHat[r][c][3] = 0
# Now that I have the scarf as a fully transparent picture, I am ready to mask it
# but paste only works with PIL images so first I have to make this a PIL
myMask = PIL.Image.fromarray(justHat)
new_img.paste(myMask, (-30, 0), mask=myMask)  # puts the myMask, the dorag, onto the gingerpic as a mask
# and I can put it on Gingers head:
fig, ax = plt.subplots(1, 2)
ax[0].set_title("Original scarf")
ax[0].imshow(PILcoolhat)  # the original dog pic
# ax[1].set_title("resized and transparencied")
# ax[1].imshow(justHat)
plt.show()
ax[0].imshow(new_img)
plt.show(block=True)  # this just keeps it open. wasn't doing this properly in pycharm
'''
1.  What is the difference between how the earth_file is being 'read' and 
how the ginger file is being read?
2.  Why am I resizing the earth image to be 10X10?  How did I get those
dimensions?
3.  What is the name of the smaller earth file?
4.  What is the line of code that is putting the small earth image over
the eye on the left?  Exactly what point is the program using to locate this?
5.  What does ax[0]1] refer to (line24) why am I using [0][1]?
6.  Add a line of code that will change the right eye also
.  Now take your own picture(s) and play around with this idea of 
'masking' to make something creative and unique to you.
'''
