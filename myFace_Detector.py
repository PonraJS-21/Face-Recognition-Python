from PIL import Image
import face_recognition
from datetime import datetime
import json
import numpy as np
from json import JSONEncoder
import json_write
    
start=datetime.now()
# Load the jpg file into a numpy array
image = face_recognition.load_image_file("images/trevor.jpg")

face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")
face_encode = face_recognition.face_encodings(image, face_locations)
print(face_encode)

array = np.asarray(face_encode[0])
json_write.save_img(array, 'Trevor')

print("I found {} face(s) in this photograph.".format(len(face_locations)))
print(datetime.now()-start)