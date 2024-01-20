import cv2
import sys
import time
import os

capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("unable to access camera")
while True:
    rel, frame = capture.read()

    if not rel:
        print("not all frame captured")
        break
    convert = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if os.path.exists("D:/YOMTECH PROJECTS/my python/test/new.jpg"):
        ans = input("File name already exist, Will you love to replace it? Y/N")
        if ans == "Y":
            os.remove("D:/YOMTECH PROJECTS/my python/test/new.jpg")
        elif ans == "N":
            exit()

    def func():
        cv2.imwrite("D:/YOMTECH PROJECTS/my python/test/new.jpg",convert)

        key = cv2.waitKey(0)

        time.sleep(5)
        
    func()
    break
    # end def

capture.release()

cv2.destroyAllWindows()

