from PIL import Image 
from pylab import *
import numpy as np
import matplotlib.pyplot as plt


# NEGATIVE IMAGE

def make_negative(im):
    im2 = 255 - im 
    Image.fromarray(im2).show()

def clamp_intervals(im, start, end):
    diff = end - start
    im3 = (diff/255) * im + start # Clamp interval 100..200
    Image.fromarray(im3).show()

def image_darkener(im, level):
    im4 = 255.0 * (im/255.0) ** level # We are squaring the image in purpose of making the image darker.
    Image.fromarray(im4).show()

def bootstrap():
    photo_name = input("Enter the photo name: ")

    im = np.array(Image.open(photo_name).convert('L'))

    mode = input("Select mode: \n 1 - Negative \n 2 - Clamps \n 3 - Darkener \n\n")

    if mode == "1":
        make_negative(im)
    elif mode == "2":
        start = int(input("Enter the interval start: "))
        end = int(input("Enter te interval end: "))
        clamp_intervals(im, start, end)
    elif mode == "3":
        level = int(input("Enter the darkener level: "))
        image_darkener(im, level)
    
if __name__ == "__main__":
    bootstrap()