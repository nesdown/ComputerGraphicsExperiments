from PIL import Image
import scipy.ndimage
from scipy import misc
import numpy as np 
# from keras.preprocessing.image import save_img

def mean_filter(im):
    k = np.ones((5,5))/25
    b = scipy.ndimage.filters.convolve(im, k)
    b = scipy.misc.toimage(b)
    b.show()

def min_filter(im):
    b = scipy.ndimage.filters.minimum_filter(im, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
    b = scipy.misc.toimage(b)
    b.show()

def max_filter(im):
    b = scipy.ndimage.filters.maximum_filter(im, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
    b = scipy.misc.toimage(b)
    b.show()

def median_filter(im):
    b = scipy.ndimage.filters.median_filter(im, size=5, footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
    b = scipy.misc.toimage(b)
    b.show()

if __name__ == "__main__":
    file_name = input("Enter the photo name: ")
    a = Image.open(file_name).convert('L')

    mean_filter(a)
    min_filter(a)
    median_filter(a)
 