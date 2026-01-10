import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io

#reads the url via skimage
image = io.imread('skeleton.jpg')
print(image.shape)
def crop_image(image, y1, y2, x1, x2):
    """this function crops the image to the specified dimensions y1, y2, x1, x2"""
    return image[y1:y2, x1:x2]

#--------------------------------------Filtering-------------------------------------------------------
def medianSmooth(img,X,Y):
    """duplicates the image "ker" into "duplicate"
    loops through every pixel and adds it and its neighbours into the array arr
    it then averages the central pixel and the array arr"""
    duplicate=img.copy()
    for yy in range(1,Y-1):
        for z in range(1,X-1):
            arr =np.array(img[yy - 1:yy + 2, z - 1:z + 2].copy())
            # averaging
            a = np.array([0, 0, 0])
            for y in range(3):
                for x in range(3):
                    a = a + arr[x, y]
            duplicate[yy, z] = a/9
    return duplicate

def gausianSmooth(img):
    """uses the inbuilt skimage gaussian filter and returns the processed image"""
    filtered = skimage.filters.gaussian(img)
    return filtered

#--------------------------------------Thresholding-------------------------------------------------------
def Threshold(img,X,Y,threshold):
    """duplicates the image "img" into "duplicate"
    loops through every pixel determines if its brightness is above or below the threshold
    if above, it colors it white, otherwise it colors it black
    returns duplicate"""
    duplicate=img.copy()
    for yy in range(1,Y-1):
        for z in range(1,X-1):
            brightness = img[yy,z]
            if brightness.sum() >= threshold:
                duplicate[yy,z] = np.array([255, 255, 255])
            else:
                duplicate[yy, z] = np.array([0, 0, 0])
    return duplicate

def Invert(img,X,Y):
    """duplicates the image "img" into "duplicate"
    loops through every pixel and subtracts its color values from their max possible value
    returns duplicate"""
    duplicate=img.copy()
    for yy in range(1,Y-1):
        for z in range(1,X-1):
            duplicate[yy,z] = np.array([255, 255, 255]) - np.array(img[yy,z])
    return duplicate

#--------------------------------------Final showing-------------------------------------------------------
#renders the image
plt.imshow(image, cmap='gray')
plt.show()
plt.imshow(crop_image(image, 0, 250, 250, 500), cmap='gray')
plt.show()
plt.imshow(Threshold(image,477, 600,100), cmap='gray')
plt.show()
plt.imshow(medianSmooth(image,477, 600), cmap='gray')
plt.show()
plt.imshow(gausianSmooth(image), cmap='gray')
plt.show()
plt.imshow(Invert(image,477, 600), cmap='gray')
plt.show()

