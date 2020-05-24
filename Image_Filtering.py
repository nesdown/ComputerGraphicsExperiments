from PIL import Image
from PIL import ImageFilter 
from matplotlib import *
import matplotlib.pyplot as plt
from pylab import *

# plt.figure(figsize=(15, 15))

# plt.subplot(3, 4, 1)

def original_image(im):
    plt.imshow(im)
    plt.title("Original")
    plt.show()

# plt.subplot(3, 4, 2)

def countour_image(im):
    im2 = im.filter(ImageFilter.CONTOUR)
    plt.imshow(im2)
    plt.title("Contour")
    plt.show()

# plt.subplot(3, 4, 3)

def detail_image(im):
    im3 = im.filter(ImageFilter.DETAIL)
    plt.imshow(im3)
    plt.title("Detail")
    plt.show()

# plt.subplot(3, 4, 4)

def edge_enhance_image(im):
    im4  = im.filter(ImageFilter.EDGE_ENHANCE)
    plt.imshow(im4)
    plt.title("Edge Enhance")
    plt.show()

# plt.subplot(3, 4, 5)

def edge_enhance_more_image(im):
    im5 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
    plt.imshow(im5)
    plt.title("Edge Enhance More")
    plt.show()

# plt.subplot(3, 4, 6)

def emboss_image(im):
    im6 = im.filter(ImageFilter.EMBOSS)
    plt.imshow(im6)
    plt.title("Emboss")
    plt.show()

# plt.subplot(3, 4, 7)

def find_edges_image(im):
    im7 = im.filter(ImageFilter.FIND_EDGES)
    plt.imshow(im7)
    plt.title("Find Edges")
    plt.show()

# plt.subplot(3, 4, 8)

def smooth_images(im):
    im8 = im.filter(ImageFilter.SMOOTH)
    plt.imshow(im8)
    plt.title("Lowpass 1")
    plt.show()

# plt.subplot(3, 4, 9)

def smooth_more_image(im):
    im9 = im.filter(ImageFilter.SMOOTH_MORE)
    plt.imshow(im9)
    plt.title("Lowpass 2")
    plt.show()

# plt.subplot(3, 4, 10)

def sharpen_image(im):
    im10 = im.filter(ImageFilter.SHARPEN)
    plt.imshow(im10)
    plt.title("Sharpen")
    plt.show()

# Custom Kernels
def kernel1_image(im):
    size = (3, 3)
    kernel1 = [1, 1, 1, 1, -1, 1, -1, -1, -1]
    ker1 = ImageFilter.Kernel(size, kernel1, scale=None, offset=0)
    # plt.subplot(3, 4, 11)
    im11 = im.filter(ker1)
    plt.show(im11)
    plt.title("Custom Filter 1") 
    plt.show()

def kernel2_image(im):
    size = (3, 3)
    kernel2 = [1, 0, -1, 1, 0, -1, 0, 0, -1]
    ker2 = ImageFilter.Kernel(size, kernel2, sale=None, offset=0)
    plt.subplot(3, 5, 12)
    im12 = im.filter(ker2)
    plt.imshow(im12)
    plt.title("Custom Filter 2")
    plt.show()

if __name__ == "__main__":
    image_name = input("Enter the image name: ")
    im0 = Image.open(image_name)

    mode = int(input("Select the mode (1-12): "))

    if mode == 1:
        original_image(im0)
    elif mode == 2:
        countour_image(im0)
    elif mode == 3:
        detail_image(im0)
    elif mode == 4:
        edge_enhance_image(im0)
    elif mode == 5:
        edge_enhance_more_image(im0)
    elif mode == 6:
        emboss_image(im0)
    elif mode == 7:
        find_edges_image(im0)
    elif mode == 8:
        smooth_images(im0)
    elif mode == 9:
        smooth_more_image(im0)
    elif mode == 10:
        sharpen_image(im0)
    elif mode == 11:
        kernel1_image(im0)
    elif mode == 12:
        kernel2_image(im0)
    




