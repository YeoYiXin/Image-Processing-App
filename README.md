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
    g. Add watermark <br />
    
    Original Image: <br/>
    <img src="https://github.com/YeoYiXin/Image-Processing-App/assets/89788614/9c24d033-754d-4682-b498-cc5a0db09090" width="600" height="338">
 
    Filtered Image: <br/>
    <img src="https://github.com/YeoYiXin/Image-Processing-App/assets/89788614/3c9c5608-49c6-4815-984c-689583b8abe2" width="600" height="338">

 2. <b>Impressionism </b>



 3. <b>Watercolour</b> <br/>
    The filter is implemented according to these steps:<br />
    a. Noise removal through Gaussian Blur<br />
    b. Histogram equalisation for contrast improvement<br />
    c. Creating outline (sketch lines) of the image<br />
    d. Maniplating the saturation and brightness<br />
    e. Noise removal of the coloured image<br />
    f. Applying the sketch and coloured image<br />
    g. Add border to (f.) <br/>
    h. Add watermark <br />

    Filtered Image: <br />
    <img src="https://github.com/YeoYiXin/Image-Processing-App/assets/89788614/6c80efe1-3535-46bb-b845-137d0a680f68" width="600" height="338"> <br />

 The website may have these functionalities:
 1. User shall upload the image and choose the style that they want. (Restriction: only allow png/jpg/jpeg)
 2. User can download the image in png
