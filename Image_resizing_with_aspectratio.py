import cv2
import numpy as np 
import glob


def resize(image, size, interpolation): #To resize the image to a square and maintain aspect ratio
  height, width = image.shape[:2]
  c = None if len(image.shape) < 3 else image.shape[2]
  if height == width: return cv2.resize(image, (size, size), interpolation)
  if height > width: diff = height
  else:     diff = width
  x_pos = int((diff - width)/2.)
  y_pos = int((diff - height)/2.)
  if c is None:
    mask = np.zeros((diff, diff), dtype=image.dtype)
    mask[y_pos:y_pos+height, x_pos:x_pos+width] = image[:height, :width]
  else:
    mask = np.zeros((diff, diff, c), dtype=image.dtype)
    mask[y_pos:y_pos+height, x_pos:x_pos+width, :] = image[:height, :width, :]
  return cv2.resize(mask, (size, size), interpolation)



i=1
for filename in glob.glob(r" "):
    print("Processing %s" % filename)
    inp_image = cv2.imread(filename)
    img = cv2.cvtColor(inp_image, cv2.COLOR_BGR2GRAY)
    resized = resize(inp_image,420, cv2.INTER_AREA)
    cv2.imwrite(r'image.{0}.png'.format(i),resized)
    i=i+1
      
print('All images resized')