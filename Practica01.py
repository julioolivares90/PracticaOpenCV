import cv2
from datetime import date
from datetime import datetime

#cv2.IMREAD_UNCHANGED = -1
#0 imagen en blanco y negro
#1 imagen a color
img = cv2.imread('lena.jpg',1)

print(img)
cv2.imshow('image',img)

key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
    pass
elif key == ord('s'):
    name_file = 'lena_copy.png'
    cv2.imwrite(name_file,img)
    cv2.destroyAllWindows()