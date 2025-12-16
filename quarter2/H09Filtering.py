import numpy as np
import matplotlib.pyplot as plt
import random
from skimage import io
import skimage.io

def singleDot():
    """creates a 2D numpy array "single_dot" with all values corresponding to 0
    assigns the X10 Y10 element the value of 1
    renders the array in a greyscale"""
    single_dot = np.zeros((20,20))
    single_dot[10,10] = 255
    return single_dot

def randomDots():
    """creates a 2D numpy array "random_dots" with all values corresponding to 0
    loops through every pixel and assigns them a random integer between 1 and 100
    renders the array in a greyscale"""
    random_dots = np.zeros((20,20))
    for x in range(20):
        for y in range(20):
            random_dots[x, y] = random.randrange(0,255)
    return random_dots

def medianSmooth(ker,X,Y):
    """duplicates the image "ker" into "duplicate"
    loops through every pixel and adds it and its neighbours into the array arr
    it then averages the central pixel and the array arr"""
    duplicate=ker.copy()

    for yy in range(1, 19):
        for z in range(1, 19):
            arr = ker[yy - 1:yy + 2, z - 1:z + 2].copy()

            # averaging
            a = 0
            for y in range(3):
                for x in range(3):
                    a = a + arr[x, y]
            av = a / 9
            duplicate[yy, z] = av
    duplicate[10, 10] = 100
    return duplicate

def gausianSmooth(ker,X,Y):
    """duplicates the image "ker" into "duplicate"
    loops through every pixel and adds it and its neighbours into the array arr
    multiplies the array arr by the gaussian kernel
    it then averages the central pixel by the gaussian kernel"""
    duplicate=ker.copy()

    for yy in range(1,Y-1):
        for z in range(1,X-1):
            arr = ker[yy-1:yy+2, z-1:z+2].copy()
            gaus=np.array([
                [1,4,1],
                [4,16,4],
                [1,4,1]
            ])
            arr=arr*gaus
        #averaging
            a=0
            for y in range(3):
                for x in range(3):
                    a=a+arr[x,y]
            av=a/(36)
            duplicate[yy, z] =av
    return duplicate

#render everything
plt.imshow(medianSmooth(singleDot(),20, 20), cmap='gray')
plt.show()
plt.imshow(gausianSmooth(singleDot(), 20, 20), cmap='gray')
plt.show()
plt.imshow(medianSmooth(randomDots(),20, 20), cmap='gray')
plt.show()
plt.imshow(gausianSmooth(randomDots(), 20, 20), cmap='gray')
plt.show()

y1=1250
y2=1750
x1=300
x2=800

X = x2 - x1
Y= y2 - y1

#import testing image
image = skimage.io.imread('46658_784_B12_1.tif')
nuclei = image[y1:y2,x1:x2,2]
plt.imshow(medianSmooth(nuclei,X,Y), cmap='gray')
plt.show()
plt.imshow(gausianSmooth(nuclei,X,Y), cmap='gray')
plt.show()

