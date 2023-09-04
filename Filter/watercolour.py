#combine with test.py
from PIL import Image, ImageFilter
from pathlib import Path
import noise_removal as nr
import cv2
import numpy as np

#create the border
def erosion():
    img = cv2.imread('border_water.jpg')
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, image_black  = cv2.threshold(grey, 170, 255, cv2.THRESH_BINARY) #change the image to black and white
    # Taking a matrix of size 3 as the kernel
    kernel = np.ones((3, 3), np.uint8)
    # The first parameter is the original image,
    # kernel is the matrix with which image is
    # convolved and third parameter is the number
    # of iterations, which will determine how much
    # you want to erode a given image.
    img_erosion = cv2.erode(image_black, kernel, iterations=1) 
    # cv2.imshow('Input', img)
    cv2.imwrite("Dil.jpg", img_erosion)
# cv2.waitKey(0)

def transparent():
    img = Image.open("Dil.jpg")
    img = img.convert("L")
    img = img.convert("RGBA")

    datas = img.getdata()
    new_data = []

    for item in datas: #change those which are not white to transparent
        if item[:3] != (255,255,255):  # Condition is true if pixel is not white. Change all pixels which are not white to transparent
            new_data.append((255, 255, 255, 0))  # Set alpha to 0 for white pixel - to get transparency
        else:
            new_data.append(item) #continue if its white

    img.putdata(new_data)
    img = img.filter(ImageFilter.ModeFilter(size=6)) 
    output_path = Path("Border.png")
    img.save(output_path, format="PNG", quality=95)  # Save as PNG to maintain transparency
    return output_path

def overlay_border(border1, background1):
    background = Image.open(background1)
    border = Image.open(border1)

    # Resize the border image to match the dimensions of the background image
    border = border.resize(background.size)

    # Create a new image for the output
    output = Image.new("RGBA", background.size)

    # Paste the background image onto the output
    output.paste(background, (0, 0))
    border_thickness = 0 #the position of the border on the background image
    # Paste the border image onto the output with the desired border thickness
    output.paste(border, (border_thickness, border_thickness), border)
    # output.show()
    image_with_border_path = Path("final_with_border.png")
    output.save(image_with_border_path, format="PNG", quality=95)  # Save the final image with the border
    return image_with_border_path

def filter3(img, grey): 
   #Convert image and blur
    img_filter = grey.filter((ImageFilter.GaussianBlur(radius = 1))) #blur it according to the brush_size
    img_filter = img_filter.filter((ImageFilter.GaussianBlur(radius = 2))) 
    img_filter = img_filter.filter((ImageFilter.GaussianBlur(radius = 3))) 
    img_filter.save("img.JPG")

    #creating sketch
    img_filter = cv2.imread("img.JPG", cv2.COLOR_BGR2GRAY)
    img_filter = cv2.equalizeHist(img_filter)
    img_filter = cv2.bilateralFilter(img_filter, 9, 75, 75)

    invert = cv2.bitwise_not(img_filter)

    for i in range(3):
        bilateral = cv2.bilateralFilter(invert, 3, 50, 50)

    for i in range(3):
        bilateral = cv2.bilateralFilter(bilateral, 5, 55, 55)
    
    for i in range(3):
        bilateral = cv2.bilateralFilter(bilateral, 7, 60, 60)
    
    # bilateral = cv2.bilateralFilter(bilateral, 3, 75, 75)

    invert1 = cv2.bitwise_not(bilateral)
    invert1 = cv2.bilateralFilter(invert1, 3, 75, 75)

    divide = cv2.divide(img_filter, invert1, scale=300.0)

    sketch = cv2.merge([divide,divide,divide])

    #manipulating the brightness and saturation of pixels
    img = img.convert("HSV")
    width, height = img.size
    newIm = Image.new("HSV", (width, height)) 

    for m in range(width):
        for n in range(height):
            h = int(img.getpixel((m,n))[0])
            s = int(img.getpixel((m,n))[1]*1.7) #increase the saturation of the image
            v = int(img.getpixel((m,n))[2]*1.2) #increase the brightness of the image
            newIm.putpixel((m,n), (h,s,v)) 

    newIm = newIm.convert("RGB") 
    newIm.save("img1.JPG")

    #remove noise from the image
    newIm = cv2.imread("img1.JPG")
    bilateral_im = cv2.bilateralFilter(newIm, 15, 50, 50)
    bilateral_im = cv2.bilateralFilter(bilateral_im, 3, 55, 55)
    bilateral_im = cv2.bilateralFilter(bilateral_im, 5, 60, 60)
    bilateral_im = cv2.bilateralFilter(bilateral_im, 7, 65, 65)

    #combine the sketch and image
    watercolor = ((sketch/255.0)*bilateral_im).astype("uint8")   
    cv2.imwrite("watercolor_no_border.JPG", watercolor)

    watercolor = Image.open("watercolor_no_border.JPG")
    watercolor = watercolor.filter(ImageFilter.ModeFilter(size=3))
    watercolor.save("Modefilter.JPG")

    #get the border
    border_path = Path("Border.png")
    background_path = Path("Modefilter.JPG")
    preready_image_path = overlay_border(border_path, background_path)

    img = cv2.imread(str(preready_image_path))
    for i in range(7):
        bilateral_im = cv2.medianBlur(img, 3)

    preserved = cv2.edgePreservingFilter(bilateral_im, sigma_s=5)
    name = Path("smoothen.png")
    cv2.imwrite(str(name), preserved)

    waterc = Image.open("smoothen.png") 
    paper = Image.open("Filter/apaper.jpg").convert(waterc.mode)
    paper = paper.resize(waterc.size)
    img = Image.blend(waterc,paper,0.2)
    img.show()
    img.save("final.png", format="PNG", quality=95) 



img = Image.open("Filter/emma.JPG")
grey = img.convert("L")
filter3(img, grey)

cv2.waitKey(0)  # waits until a key is pressed  
cv2.destroyAllWindows()  # destroys the window showing image 