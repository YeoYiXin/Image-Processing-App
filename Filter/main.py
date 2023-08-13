import urllib.request
from PIL import Image
from pathlib import Path
import cv2
import cartoon as f1
# from Filter import impressionism as f2
import watercolour as f3
import noise_removal as noise

query1 = int(input("Upload image from desktop or browser?\n1. Desktop \n2. Browser (Link with https) \nChoice (Please enter 1 or 2): "))
if query1 == 1:
    query2 = str(input("Please enter file path to image (Eg, Filter/flower.jpg): "))
    # filename = Path("Filter/flower.jpg")
    filename = Path(query2)
elif query1 == 2:
    query2 = str(input("Please enter file path to image (Eg, https://www.snowmonkeyresorts.com/wp-content/uploads/2019/07/58f2c6d1b886f3eae6707d9404232cd9_m.jpg): "))
    # filename = "https://www.snowmonkeyresorts.com/wp-content/uploads/2019/07/58f2c6d1b886f3eae6707d9404232cd9_m.jpg"
    filename = "image.jpg"
    urllib.request.urlretrieve(query2, filename)
else:
    print("No such choice.")

# filename = Path("Filter/flower.jpg")
img = Image.open(filename)
grey = img.convert("L")
brush_size = noise.radius_size(grey)

query = int(input("Which filter do you want to try?\n1. Cartoon\n2. Watercolour \nChoice (1 or 2): "))

if query == 1:
    f1.filter1(img, grey, brush_size)
elif query == 2:
    f3.filter3(img, grey, brush_size)
else:
    print("\nNo such filter")

cv2.waitKey(0)  # waits until a key is pressed  
cv2.destroyAllWindows()  # destroys the window showing image  