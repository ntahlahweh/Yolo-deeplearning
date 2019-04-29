![alt text](https://camo.githubusercontent.com/e69d4118b20a42de4e23b9549f9a6ec6dbbb0814/687474703a2f2f706a7265646469652e636f6d2f6d656469612f66696c65732f6461726b6e65742d626c61636b2d736d616c6c2e706e67)

# Yolo-deeplearning
Deep Learning using YOLO to locate object

# What is YOLO v2 (aka YOLO 9000)
YOLO 9000 is a high speed, real time detection algorithm that can detect on OVER 9000! (object categories)
  - You can read it over here  (https://arxiv.org/pdf/1612.08242.pdf)
  - watch a talk on it here (https://www.youtube.com/watch?v=NM6lrxy0bxs)
  - and another talk here (https://www.youtube.com/watch?v=4eIBisqx9_g)

# YOLO Installation Requirement
  - Python 3.5 or Python 3.6
    - Python 3.5 (https://www.python.org/downloads/release/python-350/)
    - Python 3.6 (https://www.python.org/downloads/release/python-360/)
  - TensorFlow (https://www.tensorflow.org/install/source_windows)
    - It is recommended that you install everything under one environment
  - Anaconda (https://www.anaconda.com/)
  - Pycharm (https://www.jetbrains.com/pycharm/)
  
# Installing YOLO using Darkflow repo
  - https://github.com/thtrieu/darkflow
  - Follow the instruction carefully and you'll be good :)
 
# Build the library 
- Open up cmd or anaconda  prompt and:
```python setup.py build_ext --inplace```
OR
```pip install -e ```
Make sure to build it INSIDE your created environment

# Download weight file
- Download the YOLOv2 608x608 weights file here (https://pjreddie.com/darknet/yolov2/)
- NOTE: there are other weights files you can try if you like
- Create a bin folder within the darkflow-master folder
- Put the weights file in the bin folder

# Test Run YOLO - Processing video file
- Move a sample video into ```darkflow-master```
- From there, open a ```cmd``` window
- Use the command 
<br/> ```python flow --model cfg/yolo.cfg --load bin/yolov2.weights --demo videofile.mp4 --gpu 1.0 --saveVideo```
<br/> ```videofile.mp4``` is the name of your video.
<br/> NOTE if you do not have the GPU version of tensorflow, leave off the ```--gpu 1.0```
<br/> ```--saveVideo``` indicates to save a name video file, which has the boxes around objects
