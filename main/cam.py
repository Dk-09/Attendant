import cv2
import os
import sys

def camera():
    cam = cv2.VideoCapture(-1)

    cv2.namedWindow("camera")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("camera", frame)

        k = cv2.waitKey(1)

        if k%256 == 32:
            path = os.getcwd()
            path = path + "/main/img/"
            os.chdir(path)
            sys.argv.pop(0)
            sorted_name = " ".join(sys.argv)
            print("sorted = " + sorted_name)
            print(type(sorted_name))
            img_name = sorted_name + ".jpg"
            print("[*] creating file: " + img_name)
            cv2.imwrite(img_name, frame)
            os.chdir("../../")
            break
    cam.release()
    cv2.destroyAllWindows()

camera()