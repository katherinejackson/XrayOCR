import pytesseract
import numpy as np
import skimage.io as io
import skimage.color as color
import matplotlib.pyplot as plt

image = io.imread('test.jpeg')

text = pytesseract.image_to_string(image)

print(text)

plt.figure()
plt.imshow(image,cmap='gray')
plt.show()