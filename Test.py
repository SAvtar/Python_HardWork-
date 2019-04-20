from cv2 import *
import os
from skimage.measure import compare_ssim
import imutils
# initialize the camera
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


imageA = capturing_pic()
imageB = cv2.imread('20.jpg')
cv2.imshow("Compared", imageB)
# convert the images to gray-scale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# Calculating SSIM of two images of same size and dimensions
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")
print("SSIM: {}".format(score))

# while True:
#     rootDir = 'files'
#     for dirName, subdirList, fileList in os.walk(rootDir):
#         print('Found directory: %s' % dirName)
#         for fname in fileList:
#             print('\t%s' % fname)
#         # Remove the first entry in the list of sub-directories
#         # if there are any sub-directories present
#         if len(subdirList) > 0:
#             del subdirList[0]
#     break