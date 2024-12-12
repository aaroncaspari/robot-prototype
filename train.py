#!/usr/bin/python3
import os
import sys
import cv2
import numpy as np
import time
import argparse
import threading as Thread
import roboctrl.libctrl.ctrl as ctrl
from tflite_runtime.interpreter import Interpreter
from tflite_runtime.interpreter import load_delegate

#from tflite_model_maker import image_classifier
#from tflite_model_maker.image_classifier import DataLoader

# Load input data specific to an on-device ML app.
#data = DataLoader.from_folder('flower_photos/')
#train_data, test_data = data.split(0.9)

# Customize the TensorFlow model.
#odel = image_classifier.create(train_data)

# Evaluate the model.
#loss, accuracy = model.evaluate(test_data)

# Export to Tensorflow Lite model and label file in `export_dir`.
#model.export(export_dir='/tmp/')