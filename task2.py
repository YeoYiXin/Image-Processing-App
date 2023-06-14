from PIL import Image

img = Image.open('/Users/rin/Desktop/ragdoll.jpeg') #store the open image operation in variable img

img = img.convert('HSV') #convert to HSV to change values of pixels, such as saturation

width, height = img.size

h , s, v = img.getpixel((3, 3))

newIm = Image.new("HSV", (width, height)) 

for m in range(width):
    for n in range(height):
        h = img.getpixel((m,n))[0]
        s = int( img.getpixel((m,n))[1] / 7) # reduce the saturation of the image
        v = ( img.getpixel((m,n))[2] ) 
        newIm.putpixel((m,n), (h,s,v)) 
        
newIm.show()
print('success')
