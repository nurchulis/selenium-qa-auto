# Blood-Iron-deficiency-Detection-With-OpenCV
How to detect iron blood deficiency with python

#Proses Operasi Morfologi
- Erosi
  erosion = cv2.erode(dilation,kernel,iterations = 1)
- Dilasi
  dilation = cv2.dilate(img,kernel,iterations = 1)
- Filling Holes Objek
  
```
import cv2
import numpy as np

##Membuat Ke GrayScale
img = cv2.imread('Data/Defisiensi/19(Defisiensi).jpg', cv2.IMREAD_GRAYSCALE)

##Melakukan Dilasi
kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(img,kernel,iterations = 1)
erosion = cv2.erode(dilation,kernel,iterations = 1)

##img = cv2.imread("darah4.jpg", cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(erosion, 240, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

font = cv2.FONT_HERSHEY_COMPLEX
nilai_c=1
nilai_e=1
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(erosion, [approx], 0, (0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1]

    if 6 < len(approx) < 13:
        cv2.putText(erosion, "Pupil", (x, y), font, 1, (0))
        nilai_e=nilai_e+1
    else:
        cv2.putText(erosion, "Normal", (x, y), font, 1, (0))
        nilai_c=nilai_c+1

cv2.imshow("shapes", img)
cv2.imshow("Threshold", erosion)
if nilai_e < nilai_c:
    print "Sel Darah Normal"
else:
    print "Sel Darah Defisiensi Besi"

print "Jumlah Shell berbentuk Pupil adalah =",nilai_e-1
print "Jumlah Shell berbentuk Normal adalah =",nilai_c-1
print "Jumlah Total Sel Adalah =",nilai_c+nilai_e-2
cv2.waitKey(0)
cv2.destroyAllWindows()
```

- Testing Result
- Result
------------------------
<img src="https://raw.githubusercontent.com/nurchulis/Blood-Iron-deficiency-Detection-With-OpenCV/master/Result_testing.png" width="1000" height="790">
