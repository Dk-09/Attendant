import cv2
import numpy as np
import face_recognition
import os
import datetime
import csv
import threading

def start_face_recognition(): 
    def box(faceLoc,img,name):
        y1,x2,y2,x1 = faceLoc
        y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
        cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
        cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,255,255),2)

    path = os.getcwd() + "/main/img"
    images = []
    names = []
    marked = []
    myList = os.listdir(path)
    print(myList)
    for element in myList:
        print("[+] Loading Images : ", element)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        names.append(os.path.splitext(cl)[0])
    print("[+] Loadig Names : " ,names)

    def findEncoding(images):
        encodeList = []
        for img,name in zip(images,names):
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # converting stored image to RGB
            try:
                encode = face_recognition.face_encodings(img)[0] # finding face encoding
                encodeList.append(encode)
            except:
                print("[-] Error finding face retake the image : " + name)
            
        return encodeList

    encodeListKnown = findEncoding(images)
    print("[+] Encoding done")

    cap = cv2.VideoCapture(0) # starting stream

    filename = datetime.datetime.now()
    path2 = os.getcwd() + "/main/db1/"
    path3 = os.getcwd() + "/main/db2/"
    with open(path2+filename.strftime("%d %B %Y"),"a") as db1:

        while True:
            success, img = cap.read()
            imgS = cv2.resize(img,(0,0),None,0.25,0.25)
            imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace,faceLoc in zip(encodeCurFrame,facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)            
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = names[matchIndex]
                    t1 = threading.Thread(target=box,args=(faceLoc,img,name))
                    t1.start()
                    
                    if name not in marked:                                
                        writer1 = csv.writer(db1)
                        date1 = datetime.datetime.today().strftime("%d %B %Y")
                        time1 = datetime.datetime.today().strftime("%I:%M %p")
                        writer1.writerow((date1, time1, name))
                        with open(path3 + name + ".csv","a") as db2:
                            writer2 = csv.writer(db2)
                            date2 = datetime.datetime.today().strftime("%d %B %Y")
                            time2 = datetime.datetime.today().strftime("%I:%M %p")
                            writer2.writerow((date2, time2, name))
                        marked.append(name)
                        
                    else:
                        pass

            cv2.imshow("Webcam", img)
            k = cv2.waitKey(1)

            if k%256 == 27 or k%256 == 113:
                print("[-] Escape hit closing app...")
                t1.join()
                break   

    cap.release()
    cv2.destroyAllWindows()
