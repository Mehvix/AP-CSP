import matplotlib.pyplot as plt
# For a complete list of pyplot commands: https://matplotlib.org/2.0.2/api/pyplot_summary.html
import os.path
import sys
import numpy as np

# Get the directory of this python script
directory = os.path.dirname(os.path.dirname(sys.argv[0]) + r"/images/")

# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'ginger.png')

# read the image data into an array
img = plt.imread(filename)

# Here I just print out some values for you to see:
print("The type of image is: " + str(type(img)))
print("The height of the image is: " + str(len(img)))
print("The length of the image is: " + str(len(img[0])))
print("The [6][8] spot is: ", img[6][8])

print("The amount of red in that spot is ", img[4][10])
print("The amount of green in that spot is ", img[6][8][1])

# To show the image data:

fig, ax = plt.subplots(1, 1)  # This creates a figure with 1 subplot (1X1 grid)
# (1,2) would create 1 X 2 grid of pics
# (2,2) would create a 2 by 2 grid of pics

height = len(img)
width = len(img[0])

# show the image data in the subplot
ax.imshow(img)
# if I had more than 1 picture, I would use
# hard brackets like this: ax[0].imshow(img)
# Show the figure on the screen
fig.show()

'''
1.  What type of data does my computer see img as?
An 2D array containing each pixel of each line, in which contains 

2.  What is the size of this image? (height and width?)
Mine photo is 604 x 453

3.  How much red is in the (6,8) spot?
Mine photo is 0.6

4.  In the code, what is the 3rd bracketed item in img[6][8][0]  ?
The color, in this case red, at the (6,8)th pixel (formatted RBG)

5.  How would you find out how much blue is in that spot?
img[6][8][2]

6.  What if I wanted to put 2 images next to each other on the screen?
fig, ax = plt.subplots(1, 2)

7.  What if we wanted to clean up my doggies face?
First identify the dirt color by rgb, and then replace all values that are close to it in a certain area

8.  Think of the algorithm we might use to make the image darker 
(recall the video we watched with the lizard)
How can we write code to either make the image sharper or black
and white?  
If we wanted to make the image lighter we could raise all of the rgb values, and if we wanted to make the image darker we'd lower all of the rbg values

9.  Look at some of the pixels in your own picture.
Note the size and colors, etc.
Oops I already did this, so the original image is 3264 x 2448, the RGB at [4,10] is [0.8627451  0.85882354 0.8784314 ]
'''