#### Filipe Carvalho Silva, 2024

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from keras.datasets import cifar10
import requests
import cv2
import base64

url = 'http://172.17.0.2:5000/predict' # internal URL from the docker container
categories=['airplane','automobile'] 

def get_img(n):
    (trainX, trainy), (testX, testy) = cifar10.load_data()
    subset_testX = testX[np.isin(testy, [0,1]).flatten()]
    subset_testy = testy[np.isin(testy, [0,1]).flatten()]
    string_img = base64.b64encode(cv2.imencode('.jpg', subset_testX[n])[1]).decode()
    return subset_testX[n], string_img, subset_testy[n]

def plot_img(img):
    plt.subplots(figsize=(2, 2))
    plt.imshow(img) 
    plt.show(block=False)
    plt.pause(3)
    plt.close()

while True:
    n = np.random.randint(0,100)
    print('Image number:',n)
    img, img_encoded, true_class = get_img(n)
    plot_img(img)
    print(f'true_class = {categories[true_class[0]]}')

    response = requests.post(url, json={"image":img_encoded}).json()
    print(f'prediction = {response.pop("prediction")}','\n',response,'\n')
