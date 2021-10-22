import cv2 as cv
import numpy as np
import time

known_distance = 40
known_width = 14.3

intial_Time = 0
inital_Distance = 0
change_in_time = 0
change_in_distance = 0

list_Distance = []
list_Speed = []


def Focal_length(measured_dist,real_width,width_in_rf_image):
    focal_length = (width_in_rf_image*measured_dist)/(real_width)
    return focal_length

def Distance_finder(Focal_length,real_face_width,face_width_in_frame):
    distance = (real_face_width*Focal_length)/(face_width_in_frame)
    return distance

def speedFinder(converedDistance,timeTaken):
    speed = converedDistance/timeTaken
    return speed

def avgspeed(completeList,averageofitems):
    lengthoflist = len(completeList)
    selecteditems = lengthoflist - averageofitems
    selecteditemslist = completeList[selecteditems:]
    average = sum(selecteditemslist)/len(selecteditemslist)
    return average


def face_data(frame):
    face_width = 0
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    haar_cascade = cv.CascadeClassifier(r'D:\Python-Projects\OpenCV\haar_face.xml')
    faces = haar_cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5)
    for (x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            face_width = w
            # print("face width: ",w)
    return face_width

ref_image = cv.imread(r'D:\Python-Projects\OpenCV\ref.jpg')
ref_image_face_width = face_data(ref_image)
Focal_length_found = Focal_length(known_distance,known_width,ref_image_face_width)
print(Focal_length_found)
capture = cv.VideoCapture(0)

while True:
    _,frame = capture.read()
    # cv.imshow('Video', gray)
    
    face_width_in_frame = face_data(frame)
    if face_width_in_frame != 0:
        Distance = Distance_finder(Focal_length_found,known_width,face_width_in_frame)
        list_Distance.append(Distance)
        averDistance =avgspeed(list_Distance,6)
        distanceinMeter = averDistance/100


        if inital_Distance != 0:
            change_in_distance = inital_Distance - distanceinMeter
            change_in_time = time.time() - intial_Time
            speed = speedFinder(converedDistance=change_in_distance,timeTaken=change_in_time)
            list_Speed.append(speed)
            avgerageSpeed = avgspeed(list_Speed,10)*100
            if avgerageSpeed<0:
                avgerageSpeed = avgerageSpeed*-1
            cv.putText(frame,f"Speed = {round(avgerageSpeed,2)} cm/s",(50,85),cv.FONT_HERSHEY_PLAIN,2,(0,255,0),2)

            print(speed)
        cv.putText(frame,f"Distance = {int(Distance)} cm",(50,50),cv.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        cv.imshow("Final",frame)

        inital_Distance = distanceinMeter
        intial_Time = time.time()

    if cv.waitKey(5) & 0xFF == ord('d'):
        break  # d is the kill swich here
capture.release()
capture.destroAllWindows
