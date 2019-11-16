import cv2
import numpy as np
import matplotlib.pyplot as plt
img =cv2.imread ('hqdefault.jpg', cv2.IMREAD_GRAYSCALE)
plt.imshow (img, cmap='gray', interpolation='bicubic')
plt.plot([50,100],[80,100],'c', linewidth=5)
plt.show()
cv2.waitKey(0)
cv2.imwrite ('gray.png',img)
cv2.destroyAllWindows()