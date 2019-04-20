# import the necessary packages
from skimage.measure import compare_ssim
import argparse
import imutils
import cv2
from cv2 import *
import os

# construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument('D:\currency-detector-opencv-master\\files\\test_20_1.jpg', required=True,
#                 help="first input image")
# ap.add_argument('D:\currency-detector-opencv-master\\files\\test_20_2.jpg', required=True,
#                 help="second")
# args = vars(ap.parse_args())
#
def capturing_pic():
    cam = VideoCapture(0)  # 0 -> index of camera
    s, img = cam.read()
    if s:  # frame captured without any errors
        namedWindow("cam-test", flags=WINDOW_AUTOSIZE)
        imshow("cam-test", img)
        waitKey(0)
        destroyWindow("cam-test")
        imwrite("CheckNote.jpg", img)  # save image
        cv2.imshow('CheckNote.jpg', img)


# img = capturing_pic()

def second_img():
    rootDir = 'files'
    for dirName, subdirList, fileList in os.walk(rootDir):
        print('Found directory: %s' % dirName)
        for fname in fileList:
            print('\t%s' % fname)
            continue
    # Remove the first entry in the list of sub-directories
    # if there are any sub-directories present
    #         if len(subdirList) > 0:
                # del subdirList[0]


# img2 = second_img()
# load the two input images
imageA = cv2.imread('D:\currency-detector-opencv-master\\50.jpg')
# imageA = cv2.imread('img')
imageB = cv2.imread('D:\currency-detector-opencv-master\\50_1.jpg')
# imageB = cv2.imread('img')

# convert the images to grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))
if score == 0.2724187997794332 :
    print("20 Rupee !")
if score == 0.4019294162751568:
    print("100 Rupee !")
if score == 0.3537505444886377:
    print("500 Rupee !")
if score == 0.3074555881850163 or 0.5182453897595715:
    print("50 Rupee !")
else:
    print("It's not !")

# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
thresh = cv2.threshold(diff, 0, 255,
	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]

# loop over the contours
for c in cnts:
    # compute the bounding box of the contour and then draw the
    # bounding box on both input images to represent where the two
    # images differ
    (x, y, w, h) = cv2.boundingRect(c)
    cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

# show the output images
cv2.imshow("Original_1", imageA)
cv2.imshow("Original _2", imageB)
cv2.imshow("Diff", diff)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)