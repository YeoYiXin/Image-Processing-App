from PIL import Image
from pathlib import Path
import cv2
import cartoon as f1
#import impressionism as f2
import watercolour as f3
import noise_removal as noise

filename = Path("flower.jpg")
img = Image.open(filename)
grey = img.convert("L")
brush_size = noise.radius_size(grey)

query = str(input("Which filter do you want to try?\n1. Cartoon\n2. Watercolour \nChoice: "))
query = query.replace(" ", "")
lower_query = query.lower()

if lower_query == "cartoon":
    f1.filter(img, grey, brush_size)
elif lower_query == "watercolour":
    f3.filter3(img, grey, brush_size)
else:
    print("\nNo such filter")

cv2.waitKey(0)  # waits until a key is pressed  
cv2.destroyAllWindows()  # destroys the window showing image  