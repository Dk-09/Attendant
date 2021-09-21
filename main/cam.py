import cv2
import os

def camera(name):

    cam = cv2.VideoCapture(-1)

    cv2.namedWindow("test")

    while True:

        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)

        if k%256 == 32:
            path = os.getcwd()
            os.chdir(path)
            img_name = name + ".jpg"
            cv2.imwrite(img_name, frame)
            break

    
    cam.release()

    cv2.destroyAllWindows()
