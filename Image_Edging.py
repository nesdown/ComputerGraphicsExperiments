import cv2 
from skimage import img_as_ubyte, img_as_int
from scipy import ndimage
import numpy as np 
from matplotlib import pyplot as plt

def prewitt_edge(image_name):
    img_file = cv2.imread(image_name, 0)
    img = img_as_int(img_file)

    prewitt_vertical = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype="float64")
    prewitt_vertical_out = img_as_ubyte(ndimage.convolve(img, prewitt_vertical, mode='constant', cval=0.0))
    
    plt.imshow(prewitt_vertical_out)
    plt.title("Prewitt Edge Detection")
    plt.show()

def sobel_edge(image_name):
    img_file = cv2.imread(image_name, 0)
    sobel_x = cv2.Sobel(img_file, -1, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(img_file, -1, 0, 1, ksize=5)

    plt.imshow(sobel_x, cmap = 'gray')
    plt.title("Sobel-X Edge Detection")
    plt.show()

    plt.imshow(sobel_y, cmap = 'gray')
    plt.title("Sobel-Y Edge Detection")
    plt.show()

def laplassian_edge(image_name):
    img_file = cv2.imread(image_name)

    output = cv2.Laplacian(img_file, -1)

    plt.imshow(output)
    plt.title("Laplassian Edge")
    plt.show()


if __name__ == "__main__":
    image_name = input("Enter the image name: ")
    mode = int(input("Select the mode (1 - Prewitt, 2 - Sobel, 3 - Laplassian): "))

    if mode == 1:
        prewitt_edge(image_name)
    elif mode == 2:
        sobel_edge(image_name)
    elif mode == 3:
        laplassian_edge(image_name)

