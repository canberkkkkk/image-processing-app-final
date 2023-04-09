# Numpy
import numpy as np

# PIL
from PIL import ImageEnhance

def enhanceContrast(imageView, outputImage, n = 1.25):
    constrastedImage = ImageEnhance.Contrast(outputImage.get(type="PIL")).enhance(n)
    imageView.setImage(img=outputImage.setPIL(constrastedImage).get())

def enhanceBrightness(imageView, outputImage, n = 1.25):
    brightnessImage = ImageEnhance.Brightness(outputImage.get(type="PIL")).enhance(n)
    imageView.setImage(img=outputImage.setPIL(brightnessImage).get())

def enhanceSaturation(imageView, outputImage, n = 1.25):
    saturatedImage = ImageEnhance.Color(outputImage.get(type="PIL")).enhance(n)
    imageView.setImage(img=outputImage.setPIL(saturatedImage).get())

def enhanceColorBalance(imageView, outputImage, r = 0, g = 0, b = 0):
    image = outputImage.get()
    
    if(len(image.shape) < 3):
        return False
    else:
        npImg = image.astype(np.float32)

        npImg[:,:,0] += b
        npImg[:,:,1] += g
        npImg[:,:,2] += r
        
        npImg = npImg.astype(np.uint8)
        npImg[npImg > 255] = 255
        
        imageView.setImage(img=outputImage.setPIL(npImg).get())
        
        return True