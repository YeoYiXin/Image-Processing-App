from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt
import numpy as np

def watermark():
    img = Image.open("Filter/emma.jpg")
    plt.imshow(img)
    words = "PainterLy"

    w,h = img.size #width, height of image
    x = int(w/6) #width of words
    y = int(h/6) #height of words
    if x>y: #always choose the smaller one
        font_size = y
    elif y>x:
        font_size = x
    else:
        font_size = x 
    
    font = ImageFont.truetype(font="arial.ttf", size=int(font_size/2))

    draw = ImageDraw.Draw(img)
    tw, th = font.getmask(words).size
    draw.rectangle([(0,0), (10+tw,10+th)],fill=(101, 160, 42), outline=None)
    draw.text((10, 0), words, fill=(0,0,0), font=font)
    print(tw+th)
    plt.imshow(img)
    plt.axis('off')
    plt.savefig("watermark.png", bbox_inches = 'tight', pad_inches = 0, dpi = 1200)
    plt.show()
    
watermark()
    