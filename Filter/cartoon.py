from PIL import Image, ImageFilter, ImageOps    
import numpy as np
import matplotlib.pyplot as plt
import cv2 as openCV

def filter(img, grey, brush_size):
    
    #Blur image
    img_filter = grey.filter((ImageFilter.GaussianBlur(radius = brush_size))) #blur it according to the brush_size
    img_filter.save("img.JPG")
    img_filter = openCV.imread("img.JPG")  
    gray = openCV.cvtColor(img_filter, openCV.COLOR_BGR2GRAY)  #convert to grayscale in openCV
    
    #Finding Edges    
    ret, _ = openCV.threshold(gray, 50, 255, openCV.THRESH_BINARY) #ret is the threshold
    edges = openCV.Canny(gray, ret/2, ret) #Canny Method
    invert = openCV.bitwise_not(edges) #to invert the black and white of the image, so color doesn't appear as the edges

    img = img.convert('HSV') #convert to HSV to change values of pixels, such as saturation
    width, height = img.size
    newIm = Image.new("HSV", (width, height)) 

    for m in range(width):
        for n in range(height):
            h = int( img.getpixel((m,n))[0]) 
            s = int( img.getpixel((m,n))[1] * 1.5) 
            v = int( img.getpixel((m,n))[2] * 1.2) 
            newIm.putpixel((m,n), (h,s,v)) 
            
    newIm = newIm.convert('RGB') #convert to HSV to change values of pixels, such as saturation
    newIm.save("img.JPG")

    newIm = openCV.imread("img.JPG")     
    K = 10
    Z = np.float32(newIm).reshape((-1, 3))
    # convert to np.float32
    Z = np.float32(Z)

    #notes on criteria
    #1st parameter: criteria for epsilon and criteria for max iteration, if reached then terminate 
    #default value of esp is 2 and iter is 1
    #2nd parameter: maximum number of iterations or the maximum number of times a particular operation will be performed
    #3rd parameter: represents the epsilon or the required accuracy for the operation. It specifies the 
    #               minimum change in a parameter value to continue the iteration process.
    criteria = (openCV.TERM_CRITERIA_EPS + openCV.TERM_CRITERIA_MAX_ITER, 15, 0.0001)  
    # print(criteria)
    ret2,label,center= openCV.kmeans(Z,K,None,criteria,4,openCV.KMEANS_RANDOM_CENTERS) #understand this
    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((newIm.shape))
        
    #Convert to a cartoon version
    cartoon = openCV.bitwise_and(res2, res2, mask= invert)
    openCV.imshow("CARTOON", cartoon)
    openCV.imwrite("Cartoon.JPG", cartoon)
 
# filter()
