# import urllib.request
from PIL import Image
from pathlib import Path
import cv2
import cartoon as f1
# from Filter import impressionism as f2
import watercolour as f3
import noise_removal as noise

filename = Path("/Users/Yeo Yi Xin/Documents/Design/Copy of Law Invitation/2.png")
img = Image.open(filename)
grey = img.convert("L")

query = int(input("Which filter do you want to try?\n1. Cartoon\n2. Watercolour \nChoice (1 or 2): "))

if query == 1:
    f1.filter1(img, grey)
elif query == 2:
    f3.filter3(img, grey)
else:
    print("\nNo such filter")

cv2.waitKey(0)  # waits until a key is pressed  
cv2.destroyAllWindows()  # destroys the window showing image  