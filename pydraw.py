from turtle import shape
from sketchpy import canvas
import cv2

im = cv2.imread("ataturk.jpg")
print(im.shape)
obj = canvas.sketch_from_image("ataturk.jpg")
obj.draw(threshold=50)