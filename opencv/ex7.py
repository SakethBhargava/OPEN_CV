import cv2

img = cv2.imread("pspk.jpg")
cv2.imshow("Normal_img",img)
rotational_90=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
rotational_180=cv2.rotate(img,cv2.ROTATE_180)
cv2.imshow("Rotational Img:",rotational_90)
cv2.imshow("Rotational Img1:",rotational_180)
cv2.waitKey(0)