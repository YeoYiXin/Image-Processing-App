from PIL import Image, ImageFilter, ImageOps    
import numpy as np
import matplotlib.pyplot as plt
import cv2 as openCV

def check_noise(img,filter_image): #to return the noise level - using gaussian noise
    mse = np.mean((np.array(img) - np.array(filter_image)) ** 2)
    return mse

def radius_size(img):
    brush_sizes = [1,2,3,4,5,6,7,8,9] #just to test

    best_brush_size = None #set it to null value first
    least_noise_level = float('inf') #actual value (pixels/matrix) - filtered image (pixels/matrix) = noise value (matrix)

    for size in brush_sizes:
        filter_image = img.filter(ImageFilter.GaussianBlur(radius = size))

        noise_level = check_noise(img,filter_image)
        if noise_level < least_noise_level:
            least_noise_level = noise_level
            best_brush_size = size
    print(best_brush_size)
    return best_brush_size 

def filter():
    
    #Convert image and blur
    img1 = Image.open("/Users/rin/Desktop/human.png").convert("L") 
    brush_size = radius_size(img1)
    img_filter = img1.filter((ImageFilter.GaussianBlur(radius = brush_size))) #blur it according to the brush_size
    img_filter.save("img.png")
    img_filter = openCV.imread("img.png")  
    gray = openCV.cvtColor(img_filter, openCV.COLOR_BGR2GRAY)  #convert to grayscale in openCV
    
    #Finding Edges    
    ret, thresh = openCV.threshold(gray, 50, 255, openCV.THRESH_BINARY) #ret is the threshold
    edges = openCV.Canny(gray, ret/2, ret) #Canny Method
    invert = openCV.bitwise_not(edges) #to invert the black and white of the image, so color doesn't appear as the edges

    img2 = Image.open("/Users/rin/Desktop/human.png")
    img2 = img2.convert('HSV') #convert to HSV to change values of pixels, such as saturation
    width, height = img2.size
    newIm = Image.new("HSV", (width, height)) 

    for m in range(width):
        for n in range(height):
            h = int( img2.getpixel((m,n))[0]) 
            s = int( img2.getpixel((m,n))[1] * 1.5) 
            v = int( img2.getpixel((m,n))[2] * 1.2) 
            newIm.putpixel((m,n), (h,s,v)) 
            
    newIm = newIm.convert('RGB') #convert to HSV to change values of pixels, such as saturation
    newIm.save("img.png")
    newIm = openCV.imread("img.png") 
        
    K = 10
    Z = np.float32(newIm).reshape((-1, 3))
    # convert to np.float32
    Z = np.float32(Z)

    #notes on criteria
    #1st parameter: criteria for epsilon and criteria for max iteration, if reached then terminate
    #2nd parameter: maximum number of iterations or the maximum number of times a particular operation will be performed
    #3rd parameter: represents the epsilon or the required accuracy for the operation. It specifies the 
    #               minimum change in a parameter value to continue the iteration process.
    criteria = (openCV.TERM_CRITERIA_EPS + openCV.TERM_CRITERIA_MAX_ITER, 15, 0.0001)  
    print(criteria)
    ret2,label,center= openCV.kmeans(Z,K,None,criteria,4,openCV.KMEANS_RANDOM_CENTERS) #understand this
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((newIm.shape))
        
    #Convert to a cartoon version
    cartoon = openCV.bitwise_and(res2, res2, mask= invert)

    openCV.imshow("CARTOON", cartoon)

    # openCV.imshow('Dilation Cartoon', cartoon)
    openCV.waitKey(0)  # waits until a key is pressed  
    openCV.destroyAllWindows()  # destroys the window showing image   
 
filter()
