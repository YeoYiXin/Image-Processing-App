from PIL import Image, ImageFilter
import cv2
import numpy as np

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

def filter2():
    #Convert image and blur
    img = Image.open("flower.jpg").convert("L") 
    brush_size = radius_size(img)
    img_filter = img.filter((ImageFilter.GaussianBlur(radius = brush_size))) #blur it according to the brush_size
    img_filter = img_filter.filter((ImageFilter.GaussianBlur(radius = brush_size*2))) 
    img_filter = img_filter.filter((ImageFilter.GaussianBlur(radius = brush_size*3))) 
    img_filter.save("img.jpg")

    #creating sketch
    img_filter = cv2.imread("img.jpg", cv2.COLOR_BGR2GRAY)
    img_filter = cv2.equalizeHist(img_filter)

    invert = cv2.bitwise_not(img_filter)

    bilateral = cv2.bilateralFilter(invert, 10, 50, 50)
    bilateral = cv2.bilateralFilter(bilateral, 7, 55, 55)
    bilateral = cv2.bilateralFilter(bilateral, 5, 60, 60)
    bilateral = cv2.bilateralFilter(bilateral, 3, 75, 75)

    invert1 = cv2.bitwise_not(bilateral)

    divide = cv2.divide(img_filter, invert1, scale=265.0)

    sketch = cv2.merge([divide,divide,divide])

    #manipulating the brightness and saturation of pixels
    img = Image.open("flower.jpg").convert("HSV")

    width, height = img.size

    newIm = Image.new("HSV", (width, height)) 

    for m in range(width):
        for n in range(height):
            h = int(img.getpixel((m,n))[0])
            s = int(img.getpixel((m,n))[1]*2) #increase the saturation of the image
            v = int(img.getpixel((m,n))[2]*1.5) 
            newIm.putpixel((m,n), (h,s,v)) 

    newIm = newIm.convert("RGB") 
    newIm.save("img1.jpg")

    #remove noise from the image
    newIm = cv2.imread("img1.jpg")
    bilateral_im = cv2.bilateralFilter(newIm, 15, 50, 50)

    #combine the sketch and image
    watercolor = ((sketch/255.0)*bilateral_im).astype("uint8")  
    cv2.imwrite("watercolor.jpg", watercolor)

    #appplying paper texture to the image
    waterc = Image.open("watercolor.jpg")
    paper = Image.open("apaper.jpg").convert(waterc.mode)
    paper = paper.resize(waterc.size)
    img = Image.blend(waterc,paper,0.3)
    img.show()
    img.save("final.jpg")
    cv2.waitKey(0)  # waits until a key is pressed  
    cv2.destroyAllWindows()  # destroys the window showing image  


filter2()