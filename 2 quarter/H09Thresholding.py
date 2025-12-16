import numpy
import matplotlib.pyplot as plt
import skimage
import skimage.io
import skimage.filters

#converts the image into an array and separates the layers
image_stack = skimage.io.imread('46658_784_B12_1.tif')
image_nuclei = image_stack[:,:,2]
image_cells =  image_stack[:,:,1]
image_others =  image_stack[:,:,0]

# Compute Otsu's threshold for each image layer
# that separates foreground from background
my_otsu_threshold2 = skimage.filters.threshold_otsu(image_nuclei)
my_otsu_threshold1 = skimage.filters.threshold_otsu(image_cells)
my_otsu_threshold0 = skimage.filters.threshold_otsu(image_others)
#Display the Nuclei layer in greyscale
plt.imshow(image_nuclei, cmap='gray')
plt.show()