#drone detection in single images done
import cv2 as cv
import numpy as np

img=cv.imread("drone2.jpg")
resize=cv.resize(img,[img.shape[1]//5,img.shape[0]//5])
cv.imshow("drone",resize)

hsv=cv.cvtColor(resize,cv.COLOR_BGR2HSV)
bgr_black=np.uint8([[[0,0,0]]]) #create black color in bgr (np array)
hue_black=cv.cvtColor(bgr_black,cv.COLOR_BGR2HSV)[0][0][0] #extract that black color in hsv (row,column,hsv color space) 
lowerlimit = np.array([0,0,0])
upperlimit = np.array([180,255,50]) #hue=180(doesnt matter colors),#saturation=255(include grayscale),
                                    #brightness=50(very dark)
lower_limit=np.array(lowerlimit,dtype=np.uint8)
upper_limit=np.array(upperlimit,dtype=np.uint8)
mask=cv.inRange(hsv,lowerlimit,upperlimit)
cv.imshow("whitemask",mask)

masked=cv.bitwise_and(resize,resize,mask=mask)
cv.imshow("results",masked)


cv.waitKey(0)
cv.destroyAllWindows
