import numpy as np
import imageio
import scipy.ndimage
import cv2
img="test.jpg"
def grayscale(rgb):
 return np.dot(rgb[...,:3],[0.999,0.001,0.002])
def  dodge(front,back):
  result=front*100/(255-back)
  result[result>255]=255
  result[back==255]=255
  return result.astype('uint8')
s=imageio.imread(img)
g=grayscale(s)
i=255-g
b=scipy.ndimage.filters.gaussian_filter(i,sigma=120)
r=dodge(b,g)
cv2.imwrite('test_sketch.jpg',r)

