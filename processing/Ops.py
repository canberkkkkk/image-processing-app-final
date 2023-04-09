# Numpy
import numpy as np

# Scikit-image
from skimage.util import random_noise

# PIL
from PIL import Image as PILImage, ImageOps

def opsReverseColors(imageView, outputImage):
    reversedColorImage = ImageOps.invert(outputImage.get(type="PIL"))
    imageView.setImage(img=outputImage.setPIL(reversedColorImage).get())

def opsFlipImage(imageView, outputImage):
    flippedImage = ImageOps.flip(outputImage.get(type="PIL"))
    imageView.setImage(img=outputImage.setPIL(flippedImage).get())

def opsMirrorImage(imageView, outputImage):
    mirroredImage = ImageOps.mirror(outputImage.get(type="PIL"))
    imageView.setImage(img=outputImage.setPIL(mirroredImage).get())

def opsRotateImage(imageView, outputImage, n = 90):
    rotatedImage = outputImage.get(type="PIL").rotate(n, PILImage.NEAREST, expand=1)
    imageView.setImage(img=outputImage.setPIL(rotatedImage).get())

def opsCropImage(imageView, outputImage, top = 1, right = 1, bottom = 1, left = 1):
    imageView.setImage(img=outputImage.setPIL(outputImage.get(type="PIL").crop((
        left,
        top,
        right,
        bottom
    ))).get())

def opsAddNoise(imageView, outputImage, n = 0.25):
    # Add gaussian noise to the image.
    noiseImg = random_noise(outputImage.get(), mode='gaussian', var=n)
    noiseImg = np.array(255 * noiseImg, dtype='uint8')
    imageView.setImage(img=outputImage.setPIL(noiseImg).get())