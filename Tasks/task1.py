# Create a programme that takes in an input image and replicate it, whereby keeping its original colours.
from PIL import Image
try:
    dog= Image.open("dog.png") #the file of the image to be replicated
except FileNotFoundError:
    print("Image not found")

width, height = dog.size #get the width and height of the image
# print(width) #print the width of the picture
# print(height) #print the height of the image

#create a new image (initially black) using the same dimension and the mode in which the information of image is being extracted
output_image = Image.new("RGB", (width, height)) 

for w in range(width): #set the range to search until width-1
    for h in range(height): #set the range to search until height-1
        red = dog.getpixel((w,h))[0] #get the value of red 
        green = dog.getpixel((w,h))[1] #get the value of green
        blue = dog.getpixel((w,h))[2] #get the value of blue
        output_image.putpixel((w,h), (red,green,blue)) #set the value RGB at the current pixels at square (w,h)

output_image.show() #print the image