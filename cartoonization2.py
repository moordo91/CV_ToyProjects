import cv2 as cv
import numpy as np

img = cv.imread("stark.jpg")

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)

img_blur = cv.medianBlur(img_gray, 3)
edges = cv.adaptiveThreshold(img_blur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 3)

img_bb = cv.bilateralFilter(img_blur, 15, 75, 75)
kernel = np.ones((1, 1), np.uint8)
img_erode = cv.erode(img_bb, kernel, iterations=3)
img_dilate = cv.dilate(img_erode, kernel, iterations=3)
img_style = cv.stylization(img, sigma_s=150, sigma_r=0.25)
cv.imshow("Cartoon", img_style)
cv.waitKey(0)
cv.destroyAllWindows()