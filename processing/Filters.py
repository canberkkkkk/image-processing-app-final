# CV
import cv2

# PIL
from PIL import ImageFilter

def filterToGrayscale(imageView, outputImage):
    if(outputImage.channels == 1):
        return False
    else:
        grayscaleImage = cv2.cvtColor(outputImage.get(), cv2.COLOR_BGR2GRAY)
        imageView.setImage(img=outputImage.set(grayscaleImage).get())
        return True

def filterBlur(imageView, outputImage, n = 5):
    blurredImage = outputImage.get(type="PIL").filter(ImageFilter.GaussianBlur(n))
    imageView.setImage(img=outputImage.setPIL(blurredImage).get())

def filterDeblur(imageView, outputImage, n = 7.5):
    deblurredImage = outputImage.get(type="PIL").filter(ImageFilter.UnsharpMask(n))
    imageView.setImage(img=outputImage.setPIL(deblurredImage).get())

def filterDetectEdges(imageView, outputImage):
    edges = outputImage.get(type="PIL").filter(ImageFilter.FIND_EDGES)
    imageView.setImage(img=outputImage.setPIL(edges).get())