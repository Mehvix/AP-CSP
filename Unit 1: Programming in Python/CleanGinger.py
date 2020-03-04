import matplotlib.pyplot as plt  # This is the class that has the image stuff
# in it. I use this to work with pixels
# in an image
import os.path
import random
import sys

directory = os.path.dirname(os.path.dirname(sys.argv[0]) + r"/images/")
filename = os.path.join(directory, 'ginger.png')

img = plt.imread(filename)  # I have to use this to work with the pixels
originalDog = plt.imread(filename)  # I will not change this
# I just want to be able to show the original at the end

# Now I want to clean up that messy dogs face!
# I want to take all of the pixels on her snout and
# turn them back into the color of her regular fur.
#  To do this, I will find the rgb of the dirt and
# replace it with the rgb of her normal fur.
#  I will have to be careful not to change her
#  actual nose though!

# Because I don't want it to look too uniform, I pick a random
# shade of gingers fur.  This spans from R = 200 to 230, G= 153 to 186, B=110-140


# first, I will zoom in on her snout.  To find out that exact
# dirt color I am using the print command on one of the pixels
# (or several) in that general area.  This should give me a pretty
# good idea about the range of color.
#  I will do the same thing to find out the rgb of her fur
# what color is her fur?
# print( )

# Then I headed to http://www.javascripter.net/faq/rgbtohex.htm
# online to see if my guess of [200-225, 175-190, 150-170] was accurate
#  I noticed that they were all pretty light.  So I tried again...and again...
# I decided to go with the 135-225 range for red, 69-134 for green and 0-63 for blue
# and replace it with a shade made up from a range which is a nice shade
# of her normal color

# I will need a for loop to walk through the pixels in that area
# I decided to do this in chunks so I don't accidentally get her eyes, eyelids,
# or nose...
fig1, ax = plt.subplots(1, 2)  # This sets up the sub plots
'''
#To get these parts, I can 'zone in' on particular things, but using set_xlim
# and set_ylim like this:

ax[0].imshow(img) #shows the original pic on right
ax[1].imshow(img) #shows the original pic on left
ax[1].set_xlim(955,1300) #looks at only 600-1000 on the x axis
ax[1].set_ylim(1190,986) #looks at only 1000-1800 on the y axis
                    ######NOTICE THIS GOES BACKWARDS!!!#######

'''
for r in range(682, 899):  # y values this is in the proper order
    for c in range(857, 1183):  # x values
        if img[r][c][0] > 72 and img[r][c][0] < 225 and img[r][c][1] > 0 and img[r][c][1] < 184 and img[r][c][2] >0 and img[r][c][2]<150:
            img[r][c][0] = random.randint(214, 232)
            img[r][c][1] = random.randint(171, 186)
            img[r][c][2] = random.randint(145, 155)

ax[0].set_title("Good doggy!!")
ax[1].set_title("Naughty doggy!!")
ax[1].plot(50, 150, 'ro')
ax[0].imshow(img)  # the new improved clean doggy
ax[1].imshow(originalDog)
plt.show()

'''
1.  Look at the picture and write down some of the rgb values of gingers
fur as given by the image


2.  Look at the picture and write down some of the rgb values of the dirt

3.  What range could you change the amount of red, the range for green, and
the range for blue that would make the color in gingers range


4.  What range of rgb values do you want to replace in the dirt?

5.  Find a spot on Ginger's face that you can clean up and practice cleaning

6.  Now find your own image and change some of the colors in a similar way
to make something interesting and unique to you!

'''