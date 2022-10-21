import cv2
img1 = cv2.imread("images/gorsel1.jpg")
img2 = cv2.imread("images/gorsel2.jpg")

#img1 = cv2.resize(img1, (400,400))
#img2 = cv2.resize(img2, (400,400))

diff = cv2.subtract(img1, img2)

hsv = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(hsv, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

diff[mask != 255] = [0, 0, 255]

img1[mask != 255] = [0, 0, 255]
img2[mask != 255] = [0, 0, 255]

cv2.imwrite("diff1.png", img1)
cv2.imwrite("diff2.png", img2)
cv2.imwrite("difference.png", diff)