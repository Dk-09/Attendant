import cv2
import os
import sys

def camera():
    cam = cv2.VideoCapture(-1)

    cv2.namedWindow("camera")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("\033[91m [-] failed to grab frame : Remove image and csv file from 'db1' and 'img' folder in main")
            break
        cv2.imshow("camera", frame)

        k = cv2.waitKey(25)

        if k%256 == 32:
            path = os.getcwd()
            path = path + "/main/img/"
            os.chdir(path)
            sys.argv.pop(0)
            sorted_name = " ".join(sys.argv)
            img_name = sorted_name + ".jpg"
            print("\033[92m [*] creating file: " + img_name)
            cv2.imwrite(img_name, frame)
            os.chdir("../../")
            break
    cam.release()
    cv2.destroyAllWindows()
    exit()

camera()
