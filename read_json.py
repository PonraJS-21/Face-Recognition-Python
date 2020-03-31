import json
import numpy as np
import operator

def find_distance(img_enc):
    with open("data.json", "r") as read_file:
        decodedArray = json.load(read_file)
    x = {}
    for itr in decodedArray:
        value = decodedArray[itr]
        value = json.loads(value)
        known_face = value['img_data']
        know_face_name = value['name']
        sum_data = 0

        for i in range(len(img_enc)):
            sum_data = sum_data + (known_face[i]-img_enc[i])**2

        euc_dist = np.sqrt(sum_data)

        x[know_face_name] = euc_dist
        tuple_x = sorted(x.items(), key=operator.itemgetter(1))
        dict_x = dict((x,y) for x,y in tuple_x)
        key = list(dict_x.keys())
        name = key[0]
        if(dict_x[name] < 0.6):
            name = name
        else:
            name = "Unknown"
    return name