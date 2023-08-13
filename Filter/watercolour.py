#combine with test.py
from PIL import Image, ImageFilter
from pathlib import Path
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
    # return img
    # img = img.filter(ImageFilter.GaussianBlur(radius = 1))
    output_path = Path("Border.png")
    img.save(output_path, format="PNG", quality=95)  # Save as PNG to maintain transparency
    return output_path
    # with output_path.open(mode="wb") as f:
    #     img.save(f, format="PNG", quality=95)
    # return output_path

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

def filter3(img, grey, brush_size): #send brush_size from main
    #Convert image and blur
    img_filter = grey.filter((ImageFilter.GaussianBlur(radius = brush_size))) #blur it according to the brush_size
    img_filter = img_filter.filter((ImageFilter.GaussianBlur(radius = brush_size*2))) 
    img_filter = img_filter.filter((ImageFilter.GaussianBlur(radius = brush_size*3))) 
    img_filter.save("img.JPG")

    #creating sketch
    img_filter = cv2.imread("img.JPG", cv2.COLOR_BGR2GRAY)
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
    img = img.convert("HSV")

    width, height = img.size

    newIm = Image.new("HSV", (width, height)) 

    for m in range(width):
        for n in range(height):
            h = int(img.getpixel((m,n))[0])
            s = int(img.getpixel((m,n))[1]*2) #increase the saturation of the image
            v = int(img.getpixel((m,n))[2]*1.3) #increase the brightness of the image
            newIm.putpixel((m,n), (h,s,v)) 

    newIm = newIm.convert("RGB") 
    newIm.save("img1.JPG")

    #remove noise from the image
    newIm = cv2.imread("img1.JPG")
    bilateral_im = cv2.bilateralFilter(newIm, 15, 50, 50)
    bilateral_im = cv2.bilateralFilter(bilateral_im, 3, 75, 75)
    bilateral_im = cv2.bilateralFilter(bilateral_im, 5, 60, 60)
    bilateral_im = cv2.bilateralFilter(bilateral_im, 3, 75, 75)

    #combine the sketch and image
    watercolor = ((sketch/255.0)*bilateral_im).astype("uint8")  
    cv2.imwrite("watercolor_no_border.JPG", watercolor)

    #get the border
    border_path = transparent()
    background_path = Path("watercolor_no_border.JPG")
    preready_image_path = overlay_border(border_path, background_path)

    img = cv2.imread(str(preready_image_path))
    bilateral_im = cv2.bilateralFilter(img, 5, 60, 60)
    bilateral_im = cv2.bilateralFilter(bilateral_im, 3, 75, 75)
    name = Path("smoothen.png")
    cv2.imwrite(str(name), bilateral_im)

    waterc = Image.open("smoothen.png") #("final_with_border.png")
    paper = Image.open("Filter/apaper.jpg").convert(waterc.mode)
    paper = paper.resize(waterc.size)
    img = Image.blend(waterc,paper,0.3)
    img.show()
    img.save("final.png", format="PNG", quality=95) 