# cartoonization
Simple codes to transfer a photo to cartoon

[Original Image]  
![stark](https://user-images.githubusercontent.com/82254758/228422133-4b83c9b0-2646-477b-90ec-174e6675c505.jpg)
  

- `Cartoonization1.py` is a code from ChatGPT.  
  
![Figure_2](https://user-images.githubusercontent.com/82254758/228422386-02262aeb-ad6c-4881-824e-6966d35cf045.png)  
  

- `Cartoonization2.py` is a code for an assignment of CV class.  
  
![Figure_1](https://user-images.githubusercontent.com/82254758/228422436-de81615b-657b-4eeb-8b63-3aec9496136a.png)
  
  
  
`Cartoonization1.py` reads an image and converts it to grayscale. It then applies a median blur filter to reduce noise, followed by an adaptive threshold to obtain edges in the image. The edges are then combined with a filtered color image using the bitwise and operation to create the cartoonized version.

`Cartoonization2.py` also reads an image and converts it to grayscale, but it uses a bilateral filter instead of a median blur filter to smooth the image while preserving edges. It then applies an adaptive threshold to obtain edges, which are further processed with erosion and dilation operations. Finally, the stylization function is used to create a cartoonized version of the image, which is displayed using Matplotlib.

In summary, both codes use similar techniques for edge detection and filtering, but the `Cartoonization2.py` uses more advanced operations to refine the edges and create a smoother cartoonized version of the image.



