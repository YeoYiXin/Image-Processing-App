# Image-Processing-Website
 To create a website that can transform image into art.
 Painterly rendering using Python
 
 Style includes:
 1. <b>Cartoon </b> <br/>
    The filter is implemented according to these steps:<br />
    a. Noise removal through Gaussian Blur<br />
    b. Determine threshold for edge detection<br />
    c. Edge detection through Canny edge detection<br />
    d. Manipulating the saturation and brightness<br />
    e. Applying K-means clustering to the image<br />
    f. Converting the image to cartoon<br />
    
    Original Image: <br/>
    <img src="https://github.com/YeoYiXin/Image-Processing-App/assets/89788614/9c24d033-754d-4682-b498-cc5a0db09090" width="600" height="338">
 
    Filtered Image: <br/>
    <img src="https://github.com/YeoYiXin/Image-Processing-App/assets/89788614/0d7da203-4c49-4f24-9f24-bc97ea70a00a" width="600" height="338">

 2. <b>Impressionism </b>




 3. <b>Watercolour</b> <br/>
    The filter is implemented according to these steps:<br />
    a. Noise removal through Gaussian Blur<br />
    b. Histogram equalisation for contrast improvement<br />
    c. Creating outline (sketch lines) of the image<br />
    d. Maniplating the saturation and brightness<br />
    e. Noise removal of the coloured image<br />
    f. Applying the sketch and coloured image<br />

    Filtered Image: <br />
    <img src="https://github.com/YeoYiXin/Image-Processing-App/assets/89788614/24cd0f4c-23d8-463b-99df-e8cf9df9ed50" width="600" height="338"> <br />
    
    
 The website may have these functionalities:
 1. User shall upload the image and choose the style that they want. (Restriction: only allow image of certain extension - TBA)
 2. User can download the image. (Restriction: only allow image of certain extension - TBA)
 3. User can manipulate saturation and brightness of the image.

 Future Implementation (may/may not):
 1. Mobile app that has the same functionalities as the website - operable on both Android and iOS.


