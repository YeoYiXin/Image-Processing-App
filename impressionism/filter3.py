from PIL import Image, ImageFilter
from pathlib import Path
# import noise_removal as nr
import cv2
import numpy as np
import random, math
import bisect
from gradient import gradient
import color_palette
from sklearn.cluster import KMeans
from color_palette import color_palette

def filter(gradient, img, gray):   
    width = img.shape[0]
    height = img.shape[1]
    
    #increase brush stroke lengths
    stroke_scale = 3
    
    #color palette
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    palette_size = 20 #number of colors in the palette
    
    #get colors from the image
    palette = color_palette.from_image(img, palette_size)
    
    #extend the hue/saturation ranges of the extracted colors from the image
    palette = palette.extend([(0, 50, 0), (15, 30, 0), (-15, 30, 0)])
    
    cv2.imshow("palette", palette.to_image())
    cv2.waitKey(200)

    #gradient smoothing, similar to whats been done in the previous filters
    gradient = gradient.from_gradient(gray)
    gradient_smoothing_radius = int(round(max(img.shape) / 50)) #this may need to be modified later
    gradient.smooth(gradient_smoothing_radius)
    
    res = cv2.medianBlur(img, 11)
    grid = randomized_grid(img.shape[0], img.shape[1] ,scale= 3)
    batch_size = 10000
    
    for h in range(0, len(grid), batch_size):
        # get the pixel colors at each point of the grid
        pixels = np.array([img[x[0], x[1]] for x in grid[h:min(h + batch_size, len(grid))]])
        # precompute the probabilities for every pixel based on the palette       
        color_probabilities = color_palette.compute_color_probabilities(pixels, palette, 9)
        
        #this is where the "painting" occurs, we select a color, compute the angle of each brush stroke and the length.
        #for the most part, aspects regarding brush strokes and lengths are up to the coder to change as they see fit. Its not integral to
        #follow these specific calculations step by step.
        for i, (y, x) in enumerate(grid[h:min(h + batch_size, len(grid))]):
            color = color_palette.color_select(color_probabilities[i], palette)
            
            angle = math.degrees(gradient.direction(y, x)) + 90 
            length = int(round(stroke_scale + stroke_scale * math.sqrt(gradient.magnitude(y, x))))

            # We draw an ellipse on res(the canvas), by specifying the xy coordinates it will appear at, the angle, stroke lenght, color etc.
            cv2.ellipse(res,  (x, y), (length, stroke_scale), angle, 0, 360, color, -1, cv2.LINE_AA)
    
    cv2.imshow("res", color_palette.limit_size(res, 1080))
    cv2.waitKey(0)

#This is the grid we use to figure out where pixels will go when we do ellipse at the end.
def randomized_grid(h, w, scale):
    assert (scale > 0)

    r = scale//2

    grid = []
    for i in range(0, h, scale):
        for j in range(0, w, scale):
            y = random.randint(-r, r) + i
            x = random.randint(-r, r) + j

            grid.append((y % h, x % w))

    random.shuffle(grid)
    return grid

img = cv2.imread("/Users/rin/Desktop/NOTT/IP/IP images/landscape.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('gray image', gray)
# cv2.waitKey(0) 


filter(gradient, img, gray)