# Image-Processing-Website
 To create a website that can transform image into art.
 Painterly rendering using Python
 
 Style includes:
 1. Cartoon
    The filter is implemented according to these steps:<br />
    a. Noise removal through Gaussian Blur<br />
    b. Determine threshold for edge detection<br />
    c. Edge detection through Canny edge detection<br />
    d. Manipulating the saturation and brightness<br />
    e. Applying K-means clustering to the image<br />
    f. Converting the image to cartoon<br />
    
    Original Image:<br />
    ![flower](https://github.com/YeoYiXin/Image-Processing-App/assets/89788614/9c24d033-754d-4682-b498-cc5a0db09090)

    <br />
    Filtered Image: <br />
    ![cartoon](https://github.com/YeoYiXin/Image-Processing-App/assets/89788614/3f98a970-fe2d-4625-ba54-939778a65593)

    <br />
    
 3. Watercolour
 4. Impressionism
 The website may have these functionalities:
 1. User shall upload the image and choose the style that they want. (Restriction: only allow image of certain extension - TBA)
 2. User can download the image. (Restriction: only allow image of certain extension - TBA)
 3. User can manipulate saturation and brightness of the image.

 Future Implementation (may/may not):
 1. Mobile app that has the same functionalities as the website - operable on both Android and iOS.


