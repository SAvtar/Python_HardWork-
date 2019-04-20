from cv2 import *
import os

class Camera:

# initialize the camera
    def capture_pic():
        cam = VideoCapture(0)   # 0 -> index of camera
        s, img = cam.read()
        if s:    # frame captured without any errors
            namedWindow("cam-test", flags=WINDOW_AUTOSIZE)
            imshow("cam-test",img)
            waitKey(0)
            destroyWindow("cam-test")
            imwrite('test_pic.jpg', img) #save image (os.path.join('D:\currency-detector-opencv-master\Test_Pic')
            cv2.imshow('test_pic.jpg', img)


Camera.capture_pic()
