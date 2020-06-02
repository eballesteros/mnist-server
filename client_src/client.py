import json
import requests

import numpy as np

HEADERS = {"content-type": "application/json"}
SERVER_ADDRESS = 'http://server:8501'
MODEL_VERSION = 1

def mnist_request(im):
    '''
    '''
    instance = np.expand_dims(im, -1) #add 'color' dim
    
    single_image = False
    if instance.ndim == 3:
        single_image = True
        instance = np.expand_dims(instance, 0) # batch of 1
    
    data = json.dumps({"signature_name": "serving_default", "instances": instance.tolist()})
    json_response = requests.post(f'{SERVER_ADDRESS}/v{MODEL_VERSION}/models/mnist:predict',
                                  data=data,
                                  headers=HEADERS)

    prediction =  np.argmax(np.array(json.loads(json_response.text)['predictions']), axis=1)
    
    if single_image:
        return prediction[0]
    return prediction
