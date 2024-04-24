import sys
import cv2
from matplotlib import pyplot as plt

file_name = sys.argv[1]
img = cv2.imread(file_name)

plt.figure(file_name)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()