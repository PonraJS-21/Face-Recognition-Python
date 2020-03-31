import numpy as np
from PIL import ImageGrab
import face_recognition
import cv2
from read_json  import find_distance
import time

import dlib

def screen_capture():
    previous_time = 0
    while(True):
        printscreen = np.array(ImageGrab.grab(bbox = (0,30,800,640)))
        image = cv2.cvtColor(printscreen, cv2.IMREAD_ANYCOLOR)
        bbox = face_recognition.face_locations(image,number_of_times_to_upsample=0, model="hog")
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        for top, right, bottom, left in bbox:
            # Draw a box around the face
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 1)
            faceEnc = face_recognition.face_encodings(image,([(top,right,bottom, left)]))
            name = find_distance(faceEnc[0])
            cv2.putText(image,name,(left, top-10), font, 1, (0,255,0),thickness=1) 
    
        framerate = 'fps: %.1f' % ( 1./( time.time() - previous_time ))
        cv2.putText(image,framerate,(0, 30), font, 1, (0,0,250),thickness=2) 

        # Display the resulting image
        cv2.imshow('Video', image)
    
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        previous_time = time.time()

screen_capture()