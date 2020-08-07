import cv2
import numpy as np

#Defining a function to get the contours

def getContours(img):
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #choosing exrnl to get the entire contour
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500:
            cv2.drawContours(imgContours, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True) # Defining perimeter
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)  # approximating corner points
            print(len(approx))
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCor == 3: objectType = "Tri"
            elif objCor==4:
                aspRatio = w/float(h)    # We are using an elif condition because both square and rect has contour 4
                if aspRatio > 0.95 and aspRatio< 1.05: objectType="Sqare" # for square w/h=1 sice both sides are equal
                else:objectType="Rectangle"
            elif objCor>4 : objectType="circle"

            else:objectType = "None"

            cv2.rectangle(imgContours, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(imgContours, objectType,(x+(w)-5, y+(h)-5),cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)








ghh = "Resources/SHAPEZ.jpg"
img=cv2.imread(ghh)
imgContours= img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny= cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgBlank= np.zeros_like(img)


cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Blank", imgBlank)
cv2.imshow("Contour", imgContours)
cv2.waitKey(0)








































