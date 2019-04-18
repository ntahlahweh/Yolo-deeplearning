import cv2

img = cv2.imread('C:/Users/Hafiz_Araken/PycharmProjects/darkflow/hippocampal/test/000585.jpg')

cv2.imshow('sample image', img)

cv2.waitKey(0)  # waits until a key is pressed
cv2.destroyAllWindows()  # destroys the window showing image
