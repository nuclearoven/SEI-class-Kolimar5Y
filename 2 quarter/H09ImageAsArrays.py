
import numpy as np
import matplotlib.pyplot as plt
import random
from skimage import io

def singleDot():
    """creates a 2D numpy array "single_dot" with all values corresponding to 0
    assigns the X10 Y10 element the value of 1
    renders the array in a greyscale"""
    single_dot = np.zeros((20,20))
    single_dot[10,10] = 1
    return single_dot
def randomDots():
    """creates a 2D numpy array "random_dots" with all values corresponding to 0
    loops through every pixel and assigns them a random integer between 0 and 255
    renders the array in a greyscale"""
    random_dots = np.zeros((20,20))
    for x in range(20):
        for y in range(20):
            random_dots[x, y] = random.randrange(0,255)
    print(random_dots)
    return random_dots

#reads the url via skimage
image = io.imread('13901.tif')
#confirms shape and image type
print(image.shape)
print(type(image))

def crop_image(image, r1, r2, c1, c2):
    """this function crops the image to the specified dimensions r1, r2, c1, c2"""
    return image[r1:r2, c1:c2]
#new array made from the returned cropped "image" array
cropped = crop_image(image, 100, 300, 100, 300)

#adds a number 5 to the original array?
image = image + 5

#renders the image
plt.imshow(singleDot(), cmap='gray')
plt.show()
plt.imshow(randomDots(), cmap='gray')
plt.show()
plt.imshow(cropped, cmap='gray')
plt.axis('off')
plt.show()

