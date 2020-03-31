import json
from datetime import datetime
import numpy as np
from json import JSONEncoder

class NumpyArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NumpyArrayEncoder, self).default(obj)

def save_img(img_enc, name):

    now = datetime.now()
    att = now.strftime("%m/%d/%Y, %H:%M:%S")
    attrib = json.dumps(att)
    
    with open("data.json", "r+") as file:
        numPyData = {"name": name, "img_data": img_enc}
        a_dictionary = json.dumps(numPyData,cls=NumpyArrayEncoder)  # use dump() to write array into file
        a_dictionary = {attrib: a_dictionary}
        data = json.load(file)
        data.update(a_dictionary)
        file.seek(0)
        json.dump(data, file)
        return


    # Deserialization
    with open("data.json", "r") as read_file:
        decodedArray = json.load(read_file)
    
    #numPyFloat = np.asarray(decodedArrays["img_data"])
    print("numPy Float")
    print(decodedArray)
