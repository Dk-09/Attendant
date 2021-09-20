import cv2

def camera(name):

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
        if img_counter == 1:
            break

        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)

        k = cv2.waitKey(1)

        if k%256 == 32:
            img_name = "img/" + name + '.jpg'
            print(img_name)
            cv2.imwrite(img_name, frame)
            # print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()

name = "dhruv"
camera(name)