import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#CONSTANTS
INPUT_IMAGE = '/u/mlamkin/Desktop/unicorn.png' #file in current working directory or absolute path
OUTPUT_COLOR_IMAGE = '/u/mlamkin/Desktop/unicorn1.png'
OUTPUT_GRAY_IMAGE = '/u/mlamkin/Desktop/unicornGray.png'


#read the image in
def read_image(image_file = INPUT_IMAGE):
    img = mpimg.imread(image_file)
    return img


#create and save a grayscale version of the image (should pass in an image stored in a numpy array)
def rgb_to_gray(img):
    gray_img = np.empty([img.shape[0], img.shape[1]])


    for row in range(img.shape[0]):
        for column in range(img.shape[1]):
            gray_img[row][column] = img[row][column][0] * 0.299 + img[row][column][1] * 0.587 + img[row][column][2] * 0.114


    #save grayscale image
    mpimg.imsave(OUTPUT_GRAY_IMAGE, gray_img, cmap = plt.get_cmap('gray'))

    return gray_img


#remove all color except for blue and save image
def keep_blue(img):

    for color in range(2):
        for row in range(img.shape[0]):
            for column in range(img.shape[1]):
                img[row][column][color] = 0
        
        
    #save new image
    mpimg.imsave(OUTPUT_COLOR_IMAGE, img)
    
    return img

 
##########################################################
    
img = read_image()

#create the gray image
gray_img = rgb_to_gray(img)

#create the blue image
img = keep_blue(img)    


        
