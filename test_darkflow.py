import cv2
import numpy as np

from darkflow.net.build import TFNet


options = {"model": "cfg/tiny-yolo-voc-3c.cfg",
           "load": -1,
           "labels": "labels.txt",
           "threshold": 0.1,
           "gpu": 0.1}
img = cv2.imread("C:/Users/Hafiz_Araken/PycharmProjects/darkflow/hippocampal/test/000438.jpg")
tfnet = TFNet(options)
results = tfnet.return_predict(img)

def boxing(img, predictions):
    newImage = np.copy(img)

    for result in predictions:
        top_x = result['topleft']['x']
        top_y = result['topleft']['y']

        btm_x = result['bottomright']['x']
        btm_y = result['bottomright']['y']

        confidence = result['confidence']
        label = result['label'] + " " + str(round(confidence, 3))

        if confidence > 0.1:
            newImage = cv2.rectangle(newImage, (top_x, top_y), (btm_x, btm_y), (255, 0, 0), 3)
            newImage = cv2.putText(newImage, label, (top_x, top_y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8,
                               (0, 230, 0), 1, cv2.LINE_AA)
    return newImage
print(results)

import matplotlib.pyplot as plt

_, ax = plt.subplots(figsize=(20, 10))
im = ax.imshow(boxing(img, results))
plt.show(im)